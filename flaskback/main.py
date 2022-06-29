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
        productos_factura = request.form.get("productos_final").split(",")
        if productos_factura[0] == "":
            return redirect(request.referrer)
        folio = request.form.get("folio")
        fecha_emision = datetime.today().strftime('%Y-%m-%d')
        descripcion = request.form.get("descripcion_factura")
        rut_cliente = request.form.get("rut_cliente")
        nombre_cliente = request.form.get("nombre_cliente")
        giro = request.form.get("giro")
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
        CreateFactura(cursor, rut_cliente, descripcion,
                      fecha_emision, monto_neto)
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
        productos_cotizacion = request.form.get("productos_final").split(",")
        if productos_cotizacion == "":
            return redirect(request.referrer)
        id_cotizacion = request.form.get("id_cotizacion")
        fecha_emision = datetime.today().strftime('%Y-%m-%d')
        descripcion = request.form.get("descripcion_cotizacion")
        rut_cliente = request.form.get("rut_cliente")
        nombre_cliente = request.form.get("nombre_cliente")
        giro = request.form.get("giro")
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
        createCotizacion(cursor, descripcion, rut_cliente,
                         fecha_emision, monto_neto)
        return redirect("/vercotizaciones")

@app.route("/delete_cotizacion", methods=["GET", "POST"])
def delete_cotizacion():
    if request.method == "POST":
        id = request.form.get("delete_id")
        print(id)
        deleteCotizacion(cursor, id)
        return redirect("/verproductos")




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
        id = request.form.get("edit_id")
        nombre = request.form.get("edit_nombre")
        descripcion = request.form.get("edit_descripcion")
        precio = request.form.get("edit_precio")
        updateProducto(cursor, id, nombre, descripcion, precio)
        return redirect("/verproductos")



@app.route("/welcome", methods=["GET"])
@app.route("/testing")
def testing():
    folio = request.args.get('folio')
    print(folio)
    data = getFacturasByFolio(cursor, folio)
    print(data)
    productos = getProductosByFolioFactura(cursor,folio)
    print(productos)
    primer = productos[0]
    idprod = primer[0]
    print(idprod)
    prod = getProductoById(cursor, idprod)[0]

    print(prod)
    data = data[0]
    test = {}
    # folio 0 idcliente 1 descripcion 2 fechaemi 3 montoneto 4
    test["folio"] = data[0]
    test["cliente"] = data[1]       # 0 folio 1 idproducto 2 cantidad 3 monto
    test["producto"] = prod[1]        # id nombre descripcion costo
    test["precio"] = primer[3]
    test["descripcion"] = prod[2]
    test["cantidad"] = 1
    test["n_productos"] = 1
    test = json.dumps(test)
    return render_template("pdf.html", test=test)
      

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

# If someone clicks on login, they are redirected to /result


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":  # Only if data has been posted
        result = request.form  # Get the data
        email = result["email"]
        password = result["pass"]
        try:
            # Try signing in the user with the given information
            if email == "pizarras@gmail.com" and password == "123456":
                # Insert the user data in the global person
                global person
                person["is_logged_in"] = True
            # Redirect to welcome page
                return redirect(url_for('welcome'))
            else:
                return redirect(url_for('login'))

        except Exception as e:
            print(e)
            # If there is any error, redirect back to login

    else:
        if person["is_logged_in"] == True:
            return redirect(url_for('welcome'))
        else:
            return redirect(url_for('login'))


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


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

conn.commit()
conn.close()
