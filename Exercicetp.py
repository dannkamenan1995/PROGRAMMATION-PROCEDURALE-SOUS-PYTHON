import sqlite3

conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM clients")
rows = cursor.fetchone()
for row in rows :
    print(rows)

