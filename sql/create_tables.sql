CREATE TABLE IF NOT EXISTS sales (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id    TEXT    NOT NULL,
    item      TEXT    NOT NULL,
    category  TEXT    NOT NULL,
    amount    INTEGER NOT NULL,
    price     REAL    NOT NULL,
    discount  REAL    NOT NULL,
    shop_num  INTEGER NOT NULL,
    cash_num  INTEGER NOT NULL
);