

from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import json


app = Flask(__name__)       #Initialze flask constructor
app.secret_key = "super secret key2"

#Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": "","estadoCompra":""}

#Login
@app.route("/")
def login():
    return render_template("login.html")

#Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html", error = error)

@app.route("/facturas")
def facturas():
    return render_template("facturas.html", error = error)



@app.route("/signupError")
def signupError():
    error = request.args.get('error')
    flash(error)
    return render_template("signup.html", error = error)



#Welcome page
@app.route("/welcome")
def welcome():
    if True:

       
        return render_template("welcome.html", name="s", email = "ha", qrCode=123123)
        #return render_template("camara.html", name=person["name"], email = person["email"])


#If someone clicks on login, they are redirected to /result
@app.route("/result", methods = ["POST", "GET"])
def result():
    if request.method == "POST":        #Only if data has been posted
   
        if True:  
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('login'))



#If someone clicks on register, they are redirected to /register
@app.route("/register", methods = ["POST", "GET"])
def register():
    return redirect(url_for('welcome'))

      


if __name__ == "__main__":
    
    app.run(host='0.0.0.0')
    #app.run(ssl_context=('cert.pem', 'key.pem'))
