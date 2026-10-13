import sqlite3

conn = sqlite3.connect("school_library.db") 

conn.row_factory = sqlite3.Row 

cursor = conn.cursor()

wanted = input("Which genre? ") 

cursor.execute("SELECT * FROM books WHERE genre = ?", (wanted,)) 

for book in cursor: 

    print(book["title"]) 

conn.close()