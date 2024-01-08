# import sqlite3
from database_connection import DatabaseConnection
#first build a connection with sqlite3, then create a cursor using connection and then execute the query in cursor
#then commit the connection and close the connection

def create_book_table():
    # connection = sqlite3.connect("data.db")
    # cursor= connection.cursor()

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE  IF NOT EXISTS books(name text primary key, author text, read integer);")
    #blob(binary image file),text, real(float), integer,null

    #
    # connection.commit()
    # connection.close()

def add_book(name, author):
    # connection = sqlite3.connect("data.db")
    # cursor = connection.cursor()

    # if using f string then it can be used for sql injection

    #cursor.execute(f"INSERT INTO books VALUES('{name}','{author}',0)")
    # blob(binary image file),text, real(float), integer,null

    #parameterized queries

    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES (?,?,0)',(name,author))

    # connection.commit()
    # connection.close()

def get_all_books():
    # connection= sqlite3.connect("data.db")
    cursor= connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books= [{'name':row[0],'author': row[1],"read":row[2]} for row in  cursor.fetchall()] #cursor upar s eneeche ayega fir upar chlajayega if fetchone krenge toh upar ka aayega ek bas

    # connection.close()
    return books

def mark_book_as_read(name):
    # connection = sqlite3.connect("data.db")
    # cursor= connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE books SET read=1 WHERE name= ?",(name,)) # make a tuple with comma
    #
    # connection.commit()
    # connection.close()

def delete_book(name):
    # connection = sqlite3.connect("data.db")
    # cursor = connection.cursor()
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM books WHERE name= ?", (name,))
    #
    # connection.commit()
    # connection.close()

