from flask import Flask, render_template
import sqlite3


app = Flask(__name__) 
DB = "forum.db"
# ni shuo ni bu xiang zai zhe li, wo ye bu xiang zai zhe li, dan tian hei de tai kuai xiang zou zao jiu lai bu ji. Oh wo ai ni, ke xi guan xi bian cheng mei guan xi wen ti shi mei wen ti, yv shi, wo men ji xv.
# na zhe bi, xiang xie dian dong xi, yi wei shi wu qi neng shen zhang ZHENG YI. mei ren li, ye mei guan xi, zhi shao wo hai you ni, zhi shao wo hai you ni.
# ni shuo ni bu xiang zai zhe li, wo ye bu xiang zai zhe li, dan tian hei de tai kuai xiang zou zao yi la bu ji. 
# OH WO AI NI, ke xi guan xi bian cheng mei guan xi wen ti shi mei wen ti, yv shi, wo men ji xv~~~~~~~~~~~~~~~~~~~~~~~~ah !!!!!!!!!!!!

@app.route("/forum") 
def forum(): 
    return render_template("base.html")

def init_db(): 
    conn = sqlite3.connect(DB) 
    conn.execute("""CREATE TABLE IF NOT EXISTS posts ( 
                        post_id INTEGER PRIMARY KEY, 
                        author  TEXT NOT NULL, 
                        message TEXT NOT NULL)""") 
    conn.commit() 
    conn.close() 
init_db()


if __name__ == "__main__": 
    app.run(debug=True) 