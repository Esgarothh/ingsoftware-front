import os
import urllib.parse as up
import psycopg2
from funciones import *
from flask import (
    Flask,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    abort,
    url_for,
)
import json


up.uses_netloc.append("postgres")
url = up.urlparse(
    "postgres://rfrjpzhs:i-TLh1ySmYazV81s7l4Bguw9UBoiGKlp@kesavan.db.elephantsql.com/rfrjpzhs"
)
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port,
)
conn.autocommit = True
cursor = conn.cursor()

app = Flask(__name__)  # Initialze flask constructor
app.secret_key = "super secret key2"

# Initialze person as dictionary
person = {"is_logged_in": False, "name": "", "email": "", "uid": "", "estadoCompra": ""}

# Login
@app.route("/")
def login():
    return render_template("login.html")


# Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/facturas")
def facturas():
    return render_template("facturas.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/signupError")
def signupError():
    error = request.args.get("error")
    flash(error)
    return render_template("signup.html", error=error)


def getFactura(id):
    cursor.execute("SELECT * FROM facturas WHERE id = %s", (id,))


# Welcome page
@app.route("/welcome")
def welcome():
    if True:
        piece = " <table> <thead><tr><th>Name</th><th>Description</th></tr></thead> <tbody> <tr><td>Name1</td><td>Description1</td></tr> <tr><td>Name2</td><td>Description2</td></tr> <tr><td>Name3</td><td>Description3</td></tr> </tbody> </table>"

        my_list = [
            {
                "folio": "2",
                "cliente": "yyy",
                "fechaemision": "zzz",
                "monto": "4990",
                "descripcion": "descripcion",
            },
            {
                "folio": "3",
                "cliente": "591293",
                "fechaemision": "zzz",
                "monto": "5990",
                "descripcion": "descripcion",
            },
            {
                "folio": "4",
                "cliente": "aguasandinas",
                "fechaemision": "zzz",
                "monto": "4990",
                "descripcion": "descripcion",
            },
        ]
        # cursor.execute("""SELECT nombre_empresa, mail FROM usuarios WHERE rut_empresa = 123456789""")
        # user_pass = cursor.fetchall()
        return render_template(
            "welcome.html",
            # name=user_pass[0][0],
            # email=user_pass[0][1],
            qrCode=123123,
            texto="FUNCIONA",
            piece=piece,
            my_list=my_list,
        )
        # return render_template("welcome.html", name='b', email = 'a', qrCode=123123)
        # return render_template("camara.html", name=person["name"], email = person["email"])


# If someone clicks on login, they are redirected to /result
@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":  # Only if data has been posted

        if True:
            return redirect(url_for("welcome"))
        else:
            return redirect(url_for("login"))


# If someone clicks on register, they are redirected to /register
@app.route("/verfacturas", methods=["POST", "GET"])
def verfacturas():
    return render_template("verfacturas.html")


# If someone clicks on register, they are redirected to /register
@app.route("/register", methods=["POST", "GET"])
def register():
    return redirect(url_for("welcome"))


if __name__ == "__main__":

    app.run(host="0.0.0.0")
    # app.run(ssl_context=('cert.pem', 'key.pem'))

conn.commit()
conn.close()
