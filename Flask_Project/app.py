from flask import Flask, render_template

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return render_template("index.html")

@app.route("/about") 
def about(): 
    return render_template("about.html")

@app.route("/contact")
def contact():
    return "Contact me on:" \
    "zd24152@my.westlake.school.nz"

if __name__ == "__main__": 
    app.run(debug=True)