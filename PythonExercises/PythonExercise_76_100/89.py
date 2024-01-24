import sqlite3

connect= sqlite3.connect(r"C:\Users\vranjan\Downloads\database\database.db")
cursor= connect.cursor()
cursor.execute("SELECT country FROM countries WHERE area >=2000000")
rows=cursor.fetchall()
connect.close()
for i in rows:
    print(i[0])