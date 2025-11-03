# Учебный проект по автоматизации

Проект эмулирует работу кассового софта в сети магазинов:
каждый день генерируются выгрузки чеков в формате CSV, а затем
эти данные загружаются в базу данных SQLite.

## Структура проекта

- `generate_data.py` — генерация CSV-файлов по магазинам и кассам.
- `load_to_db.py` — загрузка CSV-файлов в базу данных `sales.db`.
- `data/` — примеры сгенерированных файлов, по одному файлу на каждую кассу каждого магазина.
- `sql/create_tables.sql` — DDL c описанием таблицы `sales`.
- `img/` — скриншоты:
  - настройки планировщика (Планировщик заданий Windows) для `generate_data.py`;
  - настройки планировщика для `load_to_db.py`;
  - скриншот таблицы `sales` в БД.
- `requirements.txt` — список Python-зависимостей.

## Как запустить на новой машине

### 1. Клонировать репозиторий

`In bash`:
git clone <URL_ВАШЕГО_РЕПОЗИТОРИЯ>
cd auto_project

### 2. Создать и активировать виртуальное окружение
python -m venv venv
venv\Scripts\activate  # для Windows

### 3. Установить зависимости
pip install -r requirements.txt

### 4. Сгенерировать тестовые данные (CSV-файлы чеков)
python generate_data.py

### 5. Загрузить данные в базу данных
python load_to_db.py

```Скрипт:```
создаст файл базы данных sales.db (SQLite) в корне проекта;
создаст таблицу sales по DDL из create_tables.sql (или sql/create_tables.sql);
загрузит данные из всех файлов формата N_N.csv (например, 1_1.csv);
при настроенной логике — удалит успешно загруженные файлы.

### 6. Проверить, что данные действительно загрузились
- через SQLite (например, DB Browser for SQLite)
- bash: 
        python
        import sqlite3
        conn = sqlite3.connect("sales.db")
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM sales;")
        print(cur.fetchone())
        conn.close()





