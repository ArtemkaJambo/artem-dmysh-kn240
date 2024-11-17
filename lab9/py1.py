import sqlite3 as db
# Створити або підєднатись до Бази
conn = db.connect('my_database.db')
# Створюємо курсор для роботи з базою
c = conn.cursor()

# Створюємо Таблицю
c.execute("CREATE TABLE students (empid INTEGER PRIMARY KEY, firstname NVARCHAR(20), lastname NVARCHAR(20))")
# Перевіряємо результат, та вивидимо його за допомогою команди print
c.execute("SELECT name FROM sqlite_master WHERE type='table';")

print(c.fetchall())