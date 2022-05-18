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
    list_products = [
        {
            "codigo": "1",
            "nombre": "Pizarra",
            "desc": "Producto 1",
            "cant": "1",
            "precio": "100",
            "total": "100",
        },
        {
            "codigo": "2",
            "nombre": "Borrador",
            "desc": "Producto 2",
            "cant": "4",
            "precio": "300",
            "total": "1200",
        },
        {
            "codigo": "3",
            "nombre": "Lapiz",
            "desc": "Producto 3",
            "cant": "7",
            "precio": "500",
            "total": "3500",
        },
    ]
    return render_template("facturas.html",list_products=list_products)


@app.route("/cotizaciones")
def cotizaciones():
    list_products = [
        {
            "codigo": "1",
            "nombre": "Pizarra",
            "desc": "Producto 1",
            "cant": "1",
            "precio": "100",
            "total": "100",
        },
        {
            "codigo": "2",
            "nombre": "Borrador",
            "desc": "Producto 2",
            "cant": "4",
            "precio": "300",
            "total": "1200",
        },
        {
            "codigo": "3",
            "nombre": "Lapiz",
            "desc": "Producto 3",
            "cant": "7",
            "precio": "500",
            "total": "3500",
        },
    ]
    return render_template("cotizaciones.html",list_products=list_products)


@app.route("/productos")
def productos():
    return render_template("productos.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/signupError")
def signupError():
    error = request.args.get("error")
    flash(error)
    return render_template("signup.html", error=error)


# Welcome page
@app.route("/welcome", methods=["GET", "POST"])
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

        filas = getFacturas(cursor, 0)
        maximo = len(filas)

        # cursor.execute("""SELECT nombre_empresa, mail FROM usuarios WHERE rut_empresa = 123456789""")
        # user_pass = cursor.fetchall()
        return render_template(
            "welcome.html",
            # name=user_pass[0][0],
            # email=user_pass[0][1],
            qrCode=123123,
            texto="FUNCIONA",
            piece=piece,
            my_list=filas,
            maximo=maximo,
        )
        # return render_template("welcome.html", name='b', email = 'a', qrCode=123123)
        # return render_template("camara.html", name=person["name"], email = person["email"])


@app.route("/crear_factura", methods=["GET", "POST"])
def crear_factura():
    if request.method == "POST":
        precio = request.form.get("product_price")
        cliente = request.form.get("rut_cliente")
        descripcion = request.form.get("product_description")
        fecha_emision = "2020-01-01"
        monto_neto = request.form.get("product_price")
        print(precio)
        CreateFactura(cursor, 999, cliente, descripcion, fecha_emision, monto_neto)
        return redirect("/verfacturas")


# If someone clicks on login, they are redirected to /result
@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":  # Only if data has been posted

        if True:
            return redirect("/welcome")
        else:
            return redirect(url_for("login"))


# If someone clicks on register, they are redirected to /register
@app.route("/verfacturas", methods=["POST", "GET"])
def verfacturas():
    return render_template("verfacturas.html")


@app.route("/vercotizaciones", methods=["POST", "GET"])
def vercotizaciones():
    return render_template("vercotizaciones.html")


@app.route("/verproductos", methods=["POST", "GET"])
def verproductos():
    list_products = [
        {
            "id": "1",
            "nombre": "Producto 1",
            "precio": "100",
            "cantidad": "1",
            "descripcion": "descripcion",
        },
        {
            "id": "2",
            "nombre": "Producto 2",
            "precio": "300",
            "cantidad": "4",
            "descripcion": "descripcion",
        },
        {
            "id": "3",
            "nombre": "Producto 3",
            "precio": "500",
            "cantidad": "7",
            "descripcion": "descripcion",
        },
    ]
    return render_template("verproductos.html",list_products=list_products)


# If someone clicks on register, they are redirected to /register
@app.route("/register", methods=["POST", "GET"])
def register():
    return redirect(url_for("welcome"))


if __name__ == "__main__":

    app.run(host="0.0.0.0")
    # app.run(ssl_context=('cert.pem', 'key.pem'))

conn.commit()
conn.close()
