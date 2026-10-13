from flask import Flask, render_template

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

if __name__ == "__main__": 
    app.run(debug=True) 