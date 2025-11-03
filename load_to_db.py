import re
import sqlite3
from pathlib import Path

import pandas as pd

# БД, таблицы , и папка
BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "sales.db"          
DDL_PATH = BASE_DIR / "sql" / "create_tables.sql"
DATA_DIR = BASE_DIR / "data"       

FILE_PATTERN = re.compile(r"^\d+_\d+\.csv$")

#Класс для подключения к БД и загрузки данных
class SalesDatabase:
    def __init__(self, db_path: Path, ddl_path: Path):
        self.db_path = db_path
        self.ddl_path = ddl_path

        # Подключаемся к SQLite
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        # создаём таблицы по DDL
        self._init_tables()

        #создать таблицы через ddl file
    def _init_tables(self):
        
        with self.ddl_path.open("r", encoding="utf-8") as f:
            ddl = f.read()
        self.cursor.executescript(ddl)
        self.connection.commit()

    def post(self, query, args=()):
        #выполнения запросов
        try:
            self.cursor.execute(query, args)
            self.connection.commit()
        except Exception as err:
            print(repr(err))

    def close(self):
        #закрыть соединение
        if self.connection:
            self.connection.close()

def load_files(db: SalesDatabase, data_dir: Path):
        """Ищем все подходящие csv в data/ и загружаем в таблицу sales."""
        for path in data_dir.iterdir():
            if not (path.is_file() and FILE_PATTERN.match(path.name)):
                # пропускаем лишние файлы
                continue

            shop_str, cash_str = path.stem.split("_")
            shop_num = int(shop_str)
            cash_num = int(cash_str)

            # читаем csv в DataFrame
            try:
                df = pd.read_csv(path)

                # добавляем номер магазина и кассы
                df["shop_num"] = shop_num
                df["cash_num"] = cash_num

                # грузим в таблицу sales
                df.to_sql("sales", db.connection, if_exists="append", index=False)

                print(f"Загружен файл в БД: {path.name}")

                path.unlink()
                print(f"Файл удалён: {path.name}")
            
            except Exception as err:
            # если что-то пошло не так — файл не удаляем
                print(f"Ошибка при обработке файла {path.name}: {err}")


# основной метод для загрузки в базу
def main():
    db = SalesDatabase(DB_PATH, DDL_PATH)
    try:
        load_files(db, DATA_DIR)
        print("Готово! Все данные загружены в sales.db")
    finally:
        db.close()


if __name__ == "__main__":
    main()






