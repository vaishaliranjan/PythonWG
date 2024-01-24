import sqlite3
import pandas

connect= sqlite3.connect(r"C:\Users\vranjan\Downloads\database (1)\database.db")
cursor= connect.cursor()
cursor.execute("SELECT country FROM countries WHERE area >=2000000")
rows=cursor.fetchall()
connect.close()
print(rows)

df= pandas.DataFrame.from_records(rows)
df.columns=["Rank", "Country","Area","Population"]
print(df)
df.to_csv("countries_big.csv", index=False)
