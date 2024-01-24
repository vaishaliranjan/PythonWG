import pandas
import sqlite3
df= pandas.read_csv(r"C:\Users\vranjan\Downloads\ten_more_countries.txt")
connect= sqlite3.connect(r"C:\Users\vranjan\Downloads\database (1)\database.db")
cursor=connect.cursor()
for index,row in df.iterrows():
    print(row["Country"],row["Area"])
    cursor.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"],row["Area"]))
connect.commit()
connect.close()