from flask import Flask, render_template, request

import random  
#pip install Flask

app = Flask(__name__)

@app.route("/")

def hello_world():
    return render_template("index.html")
    

@app.route("/calcLove", methods=["POST"])
def calcLove():
    d = request.form
    ime1 = d.get("ime1")
    ime2 = d.get("ime2")
    
    
    #če ni nič za ime
    if len(ime1) == 0  or len(ime2) == 0:
        rez =  f"{ime1} + {ime2} = {0} %"

    #zase med 90 in 100
    elif ime1 == "Lovro" or ime2 == "Lovro":
        rez = f"{ime1} + {ime2} = {random.randint(90, 100)} %"

    #za prjatla med 0 in 5
    elif ime1 == "Gabriel" or ime2 == "Gabriel":
        rez = f"{ime1} + {ime2} = {random.randint(0, 5)} %"


    #normaln
    else:
        rez = f"{ime1} + {ime2} = {random.randint(0, 100)} %"


    return render_template("index.html", rezultat = rez)

app.run(debug = True)


