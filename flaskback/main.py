import os
from pickle import TRUE
import json
from datetime import datetime

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
person = {"is_logged_in": False, "name": "",
          "email": "", "uid": "", "estadoCompra": ""}

# Login


@app.route("/")
def login():
    return render_template("login.html")


# Sign up/ Register
@app.route("/signup")
def signup():
    return render_template("signup.html")

#RUTAS DE FACTURAS

@app.route("/facturas")
def facturas():
    productos = getAllProductos(cursor)
    maximo = len(productos)
    folio = getLastFolio(cursor)
    fecha = datetime.today().strftime('%Y-%m-%d')
    return render_template("facturas.html",productos=productos, folio=folio[0][0]+1, fecha=fecha, maximo=maximo)


@app.route("/crear_factura", methods=["GET", "POST"])
def crear_factura():
    if request.method == "POST":
        folio = request.form.get("folio")
        fecha_emision = datetime.today().strftime('%Y-%m-%d')
        descripcion = request.form.get("descripcion_factura")
        rut_cliente = request.form.get("rut_cliente")
        nombre_cliente = request.form.get("nombre_cliente")
        giro = request.form.get("giro")
        productos_factura = request.form.get("productos_final").split(",")
        monto_neto = 0
        for i in range(int(len(productos_factura)/3)):
            producto_nuevo = []
            for j in range(3):
                productos_factura[i*3+j] = int(productos_factura[i*3+j])
                producto_nuevo.append(productos_factura[i*3+j])
                if j+1 % 3 == 3:
                    print(int(productos_factura[i*3+j]))
                    monto_neto += int(productos_factura[i*3+j])
            agregarProductoFactura(cursor, producto_nuevo[0], folio, producto_nuevo[1], producto_nuevo[2])
        print(fecha_emision, descripcion, monto_neto, rut_cliente, nombre_cliente, giro, productos_factura)
        createCliente(cursor, rut_cliente, nombre_cliente, giro)
        CreateFactura(cursor, rut_cliente, descripcion, fecha_emision, monto_neto)
        return redirect("/verfacturas")

#RUTAS DE COTIZACIONES

@app.route("/cotizaciones")
def cotizaciones():
    productos = getAllProductos(cursor)
    maximo = len(productos)
    fecha = datetime.today().strftime('%Y-%m-%d')
    id_cotizacion = getLastIdCotizacion(cursor)
    return render_template("cotizaciones.html",productos=productos,maximo=maximo,id_cotizacion=id_cotizacion[0][0]+1,fecha=fecha)


@app.route("/crear_cotizacion", methods=["GET", "POST"])
def crear_cotizacion():
    if request.method == "POST":
        id_cotizacion = request.form.get("id_cotizacion")
        fecha_emision = datetime.today().strftime('%Y-%m-%d')
        descripcion = request.form.get("descripcion_cotizacion")
        rut_cliente = request.form.get("rut_cliente")
        nombre_cliente = request.form.get("nombre_cliente")
        giro = request.form.get("giro")
        productos_cotizacion = request.form.get("productos_final").split(",")
        monto_neto = 0
        for i in range(int(len(productos_cotizacion)/3)):
            producto_nuevo = []
            for j in range(3):
                productos_cotizacion[i*3+j] = int(productos_cotizacion[i*3+j])
                producto_nuevo.append(productos_cotizacion[i*3+j])
                if j+1 % 3 == 3:
                    print(int(productos_cotizacion[i*3+j]))
                    monto_neto += int(productos_cotizacion[i*3+j])
            agregarProductoCotizacion(cursor, producto_nuevo[0], id_cotizacion, producto_nuevo[1], producto_nuevo[2])
        print(fecha_emision, descripcion, monto_neto, rut_cliente, nombre_cliente, giro, productos_cotizacion)
        createCliente(cursor, rut_cliente, nombre_cliente, giro)
        createCotizacion(cursor, descripcion, rut_cliente, fecha_emision, monto_neto)
        return redirect("/vercotizaciones")


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


@app.route("/editar_producto", methods=["GET", "POST"])
def editar_producto():
    if request.method == "POST":
<<<<<<< HEAD
        precio = request.form.get("product_price")
        cliente = request.form.get("rut_cliente")
        descripcion = request.form.get("product_description")
        fecha_emision = "2020-01-01"
        monto_neto = request.form.get("product_price")
        producto = request.form.get("product_name")
        test = []
        test.append(precio)
        test.append(cliente)
        test.append(descripcion)
        test.append(fecha_emision)
        test.append(monto_neto)
        print(precio)
        CreateFactura(cursor, cliente+"1", cliente,
                      descripcion, fecha_emision, monto_neto)
        return render_template("pdf.html", test=json.dumps(test))


@app.route("/testing")
def testing():
    test = {}
    test["folio"] = "12345"
    test["cliente"] = "12345678-k"
    test["producto"] = "lavadora"
    test["precio"] = 100
    test["descripcion"] = "descripcion de prueba de producto lavadora"
    test["cantidad"] = 1
    test["n_productos"] = 1
    test = json.dumps(test)
    return render_template("pdf.html", test=test)
=======
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


@app.route("/crear_producto", methods=["GET", "POST"])
def crear_producto():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        descripcion = request.form.get("descripcion")
        precio = request.form.get("precio")
        createProducto(cursor, nombre, descripcion, precio)
        return redirect("/verproductos")
>>>>>>> aa00d483fa232371c5a5bb7dd6c10c48eba995fb

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
    nombres = []
    for x in facturas:
        lista = list(x)
        cliente = getClienteByID(cursor, lista[1])
        nombres.append(cliente[0][0])
    return render_template("verfacturas.html",lista_facturas=facturas,maximo=maximo,clientes=nombres)


@app.route("/vercotizaciones", methods=["POST", "GET"])
def vercotizaciones():
    cotizaciones = getCotizaciones(cursor, 0)
    maximo = len(cotizaciones)
    nombres = []
    for x in cotizaciones:
        lista = list(x)
        cliente = getClienteByID(cursor, lista[2])
        nombres.append(cliente[0][0])
    cotizaciones = getCotizaciones(cursor, 0)
    maximo = len(cotizaciones)
    return render_template("vercotizaciones.html",lista_cotizaciones=cotizaciones,maximo=maximo,clientes=nombres)


@app.route("/verproductos", methods=["POST", "GET"])
def verproductos():
    productos = getProductos(cursor, 0)
    maximo = len(productos)
    return render_template("verproductos.html",productos = productos, maximo=maximo)


# If someone clicks on register, they are redirected to /register
@app.route("/register", methods=["POST", "GET"])
def register():
    return redirect(url_for("welcome"))


<<<<<<< HEAD
if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
    # app.run(ssl_context=('cert.pem', 'key.pem'))
=======
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
>>>>>>> aa00d483fa232371c5a5bb7dd6c10c48eba995fb

conn.commit()
conn.close()
