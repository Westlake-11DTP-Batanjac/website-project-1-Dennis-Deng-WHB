from flask import Flask, render_template
import sqlite3

DB = "DTL.db"

def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""CREATE TABLE IF NOT EXISTS DTL (
                        id INTEGER PRIMARY KEY,
                        email TEXT NOT NULL,
                        name TEXT NOT NULL)""")
    conn.commit()
    conn.close()
init_db()

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return render_template("index.html") 

@app.route("/about") 
def about(): 
    return render_template("about.html") 

@app.route("/contact") 
def contact(): 
    return render_template("contacts.html")

@app.route("/post", methods=["POST"]) 
def post(): 
    name = request.form["____"] 
    # read your other inputs the same way 
    print(name) 
    return "Got it!" 

if __name__ == "__main__": 
    app.run(debug=True) 