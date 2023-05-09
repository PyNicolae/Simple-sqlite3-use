import sqlite3

conn = sqlite3.connect('books.db')

conn.execute(''' CREATE TABLE IF NOT EXISTS Books
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                year INTEGER);''')

title = input("Insert book title: ")
year = int(input("Insert the year of publication: "))

conn.execute(f"INSERT INTO Books (title,year) VALUES ('{title}', {year})")
conn.commit()

def read_books():
    conn = sqlite3.connect('books.db')

    cursor = conn.execute("SELECT * FROM Books;")
    for row in cursor:
        print(f"{row[0]}-{row[1]} ({row[2]})")
    conn.close()

