import sqlite3

conn = sqlite3.connect("school_library.db")
print("Connected")

cursor = conn.cursor()
print(cursor)

cursor.execute("SELECT * FROM books") 
books = cursor.fetchall() 
for book in books: 
    print(book) 

conn.close()