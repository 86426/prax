from flask import Flask, request, render_template, session
from flask_session import Session
from datetime import date

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    session['name1'] = None
    session['pass1'] = None
    return render_template("login.html")


@app.route('/sluzby', methods=['GET', 'POST'])
def sluzby():
    session['name1'] = request.form.get("name1")
    session['pass1'] = request.form.get("pass1")

    if session['name1'] == "Peto" and session['pass1'] == "Silvia":
        return render_template("sluzby.html")

    else:
        return render_template("login2.html")


@app.route('/ponuka', methods=["GET","POST"])
def ponuka():

    session['dnesnydatum'] = date.today().strftime("%d.%m.%Y")
    session['sluzba1'] = request.form.get("sluzba1")
    session['metre1'] = request.form.get("metre1")
    session['yn1'] = request.form.get("yn1")
    session['cena1'] = request.form.get("cena1")
    session['sluzba2'] = request.form.get("sluzba2")
    session['metre2'] = request.form.get("metre2")
    session['yn2'] = request.form.get("yn2")
    session['cena2'] = request.form.get("cena2")
    session['sluzba3'] = request.form.get("sluzba3")
    session['metre3'] = request.form.get("metre3")
    session['yn3'] = request.form.get("yn3")
    session['cena3'] = request.form.get("cena3")
    session['sluzba4'] = request.form.get("sluzba4")
    session['metre4'] = request.form.get("metre4")
    session['yn4'] = request.form.get("yn4")
    session['cena4'] = request.form.get("cena4")
    session['sluzba5'] = request.form.get("sluzba5")
    session['metre5'] = request.form.get("metre5")
    session['yn5'] = request.form.get("yn5")
    session['cena5'] = request.form.get("cena5")
    session['menoklienta'] = request.form.get("menoklienta").capitalize()
    session['telefonklienta'] = request.form.get("telefonklienta")
    session['adresaklienta'] = request.form.get("adresaklienta").capitalize()


#Robim prvy riadok
    if session['yn1'] == "on":
        if len(session['sluzba1']) == 0:
            session['sluzba1'] = 'Zameranie pozemku'
        if len(session['metre1']) == 0:
            session['metre1'] = 100
        if len(session['cena1']) == 0:
            session['cena1'] = 2.00
        else:
            session['cena1'] = "{:.2f}".format(float(session['cena1']))

    else:
        session['sluzba1'] = ""
        session['metre1'] = 0
        session['cena1'] = 0


#Robim druhy riadok
    if session['yn2'] == "on":
        if len(session['sluzba2']) == 0:
            session['sluzba2'] = 'Vyčistenie pozemku'
        if len(session['metre2']) == 0:
            session['metre2'] = 100
        if len(session['cena2']) == 0:
            session['cena2'] = 3.50
        else:
            session['cena2'] = "{:.2f}".format(float(session['cena2']))

    else:
        session['sluzba2'] = ""
        session['metre2'] = 0
        session['cena2'] = 0


#Robim treti riadok
    if session['yn3'] == "on":
        if len(session['sluzba3']) == 0:
            session['sluzba3'] = 'Zemné úpravy'
        if len(session['metre3']) == 0:
            session['metre3'] = 100
        if len(session['cena3']) == 0:
            session['cena3'] = 5.00
        else:
            session['cena3'] = "{:.2f}".format(float(session['cena3']))

    else:
        session['sluzba3'] = ""
        session['metre3'] = 0
        session['cena3'] = 0


#Robim stvrty riadok
    if session['yn4'] == "on":
        if len(session['sluzba4']) == 0:
            session['sluzba4'] = 'Búracie práce'
        if len(session['metre4']) == 0:
            session['metre4'] = 100
        if len(session['cena4']) == 0:
            session['cena4'] = 7.00
        else:
            session['cena4'] = "{:.2f}".format(float(session['cena4']))

    else:
        session['sluzba4'] = ""
        session['metre4'] = 0
        session['cena4'] = 0


#Robim piaty riadok
    if session['yn5'] == "on":
        if len(session['sluzba5']) == 0:
            session['sluzba5'] = 'Vyčistenie cesty'
        if len(session['metre5']) == 0:
            session['metre5'] = 100
        if len(session['cena5']) == 0:
            session['cena5'] = 3.00
        else:
            session['cena5'] = "{:.2f}".format(float(session['cena5']))

    else:
        session['sluzba5'] = ""
        session['metre5'] = 0
        session['cena5'] = 0

#vypocty
    session["cenacelkom1"] = float("{:.2f}".format(float(session['metre1'])*float(session['cena1'])))
    session["cenacelkom2"] = float(session['metre2'])*float(session['cena2'])
    session["cenacelkom3"] = float(session['metre3'])*float(session['cena3'])
    session["cenacelkom4"] = float(session['metre4'])*float(session['cena4'])
    session["cenacelkom5"] = float(session['metre5'])*float(session['cena5'])
    session["dohromady"] = session['cenacelkom1']+session['cenacelkom2']+session['cenacelkom3']+session['cenacelkom4']+session['cenacelkom5']
    return render_template("ponuka.html")



if __name__ == "__main__":
    app.run(debug=True)
