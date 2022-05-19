from datetime import datetime
import os
from pydoc import describe
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
    productos = getAllProductos(cursor)
    maximo = len(productos)
    folio = getLastFolio(cursor)
    fecha = datetime.today().strftime('%Y-%m-%d')
    return render_template("facturas.html",productos=productos, folio=folio[0][0] + 1, fecha=fecha, maximo=maximo)


@app.route("/cotizaciones")
def cotizaciones():
    productos = getAllProductos(cursor)
    maximo = len(productos)
    return render_template("cotizaciones.html",productos=productos,maximo=maximo)


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
        fecha_emision = datetime.today().strftime('%Y-%m-%d')
        monto_neto = request.form.get("product_price")
        CreateFactura(cursor, cliente, descripcion, fecha_emision, monto_neto)
        return redirect("/verfacturas")

@app.route("/editar_producto", methods=["GET", "POST"])
def editar_producto():
    if request.method == "POST":
        id = request.form.get("edit_id")
        nombre = request.form.get("edit_nombre")
        descripcion = request.form.get("edit_descripcion")
        precio = request.form.get("edit_precio")
        updateProducto(cursor, id, nombre, descripcion, precio)
        return redirect("/verproductos")

@app.route("/delete_producto", methods=["GET", "POST"])
def delete_producto():
    if request.method == "POST":
        id = request.form.get("delete_id")
        print(id)
        deleteProducto(cursor, id)
        return redirect("/verproductos")



@app.route("/crear_cotizacion", methods=["GET", "POST"])
def crear_cotizacion():
    if request.method == "POST":
        #precio = request.form.get("product_price")
        #cliente = request.form.get("rut_cliente")
        #descripcion = request.form.get("product_description")
        #fecha_emision = datetime.today().strftime('%Y-%m-%d')
        #monto_neto = request.form.get("product_price")
        #print(precio)
        #CreateFactura(cursor, cliente, descripcion, fecha_emision, monto_neto)
        return redirect("/verfacturas")

@app.route("/crear_producto", methods=["GET", "POST"])
def crear_producto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        createProducto(cursor, nombre, descripcion, precio)
        return redirect("/verproductos")

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
    facturas = getFacturas(cursor, 0)
    maximo = len(facturas)
    return render_template("verfacturas.html",lista_facturas=facturas,maximo=maximo)


@app.route("/vercotizaciones", methods=["POST", "GET"])
def vercotizaciones():
    cotizaciones = getCotizaciones(cursor, 0)
    maximo = len(cotizaciones)
    return render_template("vercotizaciones.html",lista_cotizaciones=cotizaciones,maximo=maximo)


@app.route("/verproductos", methods=["POST", "GET"])
def verproductos():
    productos = getProductos(cursor, 0)
    maximo = len(productos)
    return render_template("verproductos.html",productos = productos, maximo=maximo)


# If someone clicks on register, they are redirected to /register
@app.route("/register", methods=["POST", "GET"])
def register():
    return redirect(url_for("welcome"))


if __name__ == "__main__":

    app.run(host="0.0.0.0")
    # app.run(ssl_context=('cert.pem', 'key.pem'))

conn.commit()
conn.close()
