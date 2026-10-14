from flask import Flask, render_template
import sqlite3

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "Welcome to the home page!" 

@app.route("/about") 
def about(): 
    return "This page is about me." 

@app.route("/contact") 
def contact(): 
    return "Email me at zd24152@my.westlake.school.nz" 

@app.route("/post", methods=["POST"]) 
def post(): 
    name = request.form["____"] 
    # read your other inputs the same way 
    print(name) 
    return "Got it!" 

if __name__ == "__main__": 
    app.run(debug=True) 