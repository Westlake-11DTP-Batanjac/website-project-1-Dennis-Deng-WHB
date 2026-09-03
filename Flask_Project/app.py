from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def home(): 
    return "<h1>Denn1s' D' Setup works!</h1>" 

@app.route("/about") 
def about(): 
    return "<h1>Denn1s's second page works.</h1>" 

@app.route("/contact")
def contact():
    return "Contact me on:" \
    "zd24152@my.westlake.school.nz"

if __name__ == "__main__": 
    app.run(debug=True) 