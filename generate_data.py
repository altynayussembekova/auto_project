from datetime import datetime, timedelta
import random
from pathlib import Path
import pandas as pd

# константы для генерации
N_SHOPS = 3
CASH_PER_SHOP = 2
ROWS_PER_FILE = 5

CATEGORIES = {
    "Бытовая химия": ["Средство для мытья посуды", "Порошок", "Чистящее средство"],
    "Текстиль": ["Полотенце", "Скатерть", "Наволочка"],
    "Посуда": ["Кружка", "Тарелка", "Сковорода"],
}
# сохраняем там же
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data" 
DATA_DIR.mkdir(exist_ok=True)

# файлы выгрузки
for shop in range(1,N_SHOPS+1):
    for cash in range(1,CASH_PER_SHOP+1):
        filename = DATA_DIR /f"{shop}_{cash}.csv"

        rows = []
   
        for i in range(1, ROWS_PER_FILE+1):
            doc_id = f"receipt_{shop}_{cash}_{i}"
            category = random.choice(list(CATEGORIES.keys()))
            item = random.choice(CATEGORIES[category])
            amount = random.randint(1,5)
            price = round(random.uniform(100,1000), 2)
            discount = random.choice([0,round(price*0.1,2)])

            rows.append({
                "doc_id": doc_id,
                "item": item,
                "category": category,
                "amount": amount,
                "price": price,
                "discount": discount, 
            })
        df = pd.DataFrame(rows)
        df.to_csv(filename, index=False)

        print(f"Создан файл: {filename}")





