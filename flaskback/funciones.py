# FUNCIONES FACTURAS

def CreateFactura(cursor, cliente_id, descripcion, fecha_emision, monto_neto):
    cursor.execute("""INSERT INTO facturas(cliente_id, descripcion, fecha_emision, monto_neto) VALUES (%s, %s, %s, %s);""", (cliente_id, descripcion, fecha_emision, monto_neto))

def getLastFolio(cursor):
    cursor.execute("""SELECT folio FROM facturas ORDER BY folio DESC LIMIT 1;""")
    return cursor.fetchall()

def getFacturas(cursor, hoja):
    limite = (hoja * 10)
    cursor.execute("""SELECT * FROM facturas LIMIT 10 OFFSET %s;""", (limite,))
    return cursor.fetchall()

def getFacturasByFolio(cursor, folio):
    cursor.execute("""SELECT * FROM facturas WHERE  folio = %s;""", (folio,))
    return cursor.fetchall()

def getFacturasByClienteId(cursor, clienteId):
    cursor.execute("""SELECT * FROM facturas WHERE  cliente_id = %s;""", (clienteId,))
    return cursor.fetchall()

def getFacturasByFecha(cursor, fecha1, fecha2):
    cursor.execute("""SELECT * FROM facturas WHERE fecha_emision >= %s AND fecha_emision <= %s;""", (fecha1, fecha2,))
    return cursor.fetchall()

# FUNCIONES COTIZACIONES

def createCotizacion(cursor, descripcion, cliente_id, fecha, total):
    cursor.execute("""INSERT INTO facturas(descripcion, cliente_id, fecha, total) VALUES (%s, %s, %s, %s);""", (descripcion, cliente_id, fecha, total))

def getCotizaciones(cursor, hoja):
    limite = (hoja * 10)
    cursor.execute("""SELECT * FROM cotizaciones LIMIT 10 OFFSET %s;""", (limite,))
    return cursor.fetchall()

def getCotizacionesById(cursor, id):
    cursor.execute("""SELECT * FROM cotizaciones WHERE  id_cotizacion = %s;""", (id,))
    return cursor.fetchall()

def getCotizacionesByClienteId(cursor, clienteId):
    cursor.execute("""SELECT * FROM cotizaciones WHERE  cliente_id = %s;""", (clienteId,))
    return cursor.fetchall()

def getCotizacionesByFecha(cursor, fecha1, fecha2):
    cursor.execute("""SELECT * FROM cotizaciones WHERE fecha >= %s AND fecha <= %s;""", (fecha1, fecha2,))
    return cursor.fetchall()

def updateClienteCotizacion(cursor, id, cliente_id):
    cursor.execute("""UPDATE cotizaciones SET cliente_id = %s WHERE id_cotizacion = %s;""", (cliente_id, id,))

def updateDescripcionCotizacion(cursor, id, descripcion):
    cursor.execute("""UPDATE cotizaciones SET descripcion = %s WHERE id_cotizacion = %s;""", (id, descripcion,))

def updateTotalCotizacion(cursor, id, total):
    cursor.execute("""UPDATE cotizaciones SET total = %s WHERE id_cotizacion = %s;""", (total, id,))
    
def updateFechaCotizacion(cursor, id, fecha):
    cursor.execute("""UPDATE cotizaciones SET fecha = %s WHERE id_cotizacion = %s;""", (fecha, id,))

def deleteCotizacion(cursor, id):
    cursor.execute("""DELETE FROM cotizaciones WHERE id_cotizacion = %s;""", (id,))

# FUNCIONES PROUDCTOS

def createProducto(cursor, nombre, descripcion, costo_neto):
    cursor.execute("""INSERT INTO productos(nombre, descripcion, costo_neto) VALUES (%s, %s, %s);""", (nombre, descripcion, costo_neto))

def getProductos(cursor, hoja):
    limite = (hoja * 10)
    cursor.execute("""SELECT * FROM productos LIMIT 10 OFFSET %s;""", (limite,))
    return cursor.fetchall()

def getAllProductos(cursor):
    cursor.execute("""SELECT * FROM productos;""")
    return cursor.fetchall()

def getProductoById(cursor, id):
    cursor.execute("""SELECT * FROM productos WHERE productos id_producto = %s;""", (id,))
    return cursor.fetchall()

def getProductoByNombre(cursor, nombre):
    cursor.execute("""SELECT * FROM productos WHERE productos nombre = %s;""", (nombre,))
    return cursor.fetchall()

def updateProducto(cursor, id, nombre, descripcion, costo_neto):
    cursor.execute("""UPDATE productos SET nombre = %s, descripcion = %s, costo_neto = %s WHERE id_producto = %s;""", (nombre, descripcion, costo_neto, id,))

def updateNombreProducto(cursor, id, nombre):
    cursor.execute("""UPDATE productos SET nombre = %s WHERE id_producto = %s;""", (nombre, id,))

def updateCostoProducto(cursor, id, costo_neto):
    cursor.execute("""UPDATE productos SET costo_neto = %s WHERE id_producto = %s;""", (costo_neto, id,))

def updateDescripcionProducto(cursor, id, descripcion):
    cursor.execute("""UPDATE productos SET descripcion = %s WHERE id_producto = %s;""", (descripcion, id,))

def deleteProducto(cursor, id):
    cursor.execute("""DELETE FROM productos WHERE id_producto = %s;""", (id,))
 
#FUNCIONES CLIENTES

def createCliente(cursor, rut_cliente, nombre_cliente, giro):
    cursor.execute("""INSERT INTO clientes(rut_cliente, nombre_cliente, giro) VALUES (%s, %s, %s);""", (rut_cliente, nombre_cliente, giro))

def getClienteByID(cursor, id):
    cursor.execute("""SELECT nombre_cliente FROM clientes WHERE rut_cliente = %s;""", (id,))
    return cursor.fetchall()
# FUNCIONES DE LISTAS

def agregarProductoFactura(cursor, id_producto, id_factura, cantidad, monto):
    cursor.execute("""INSERT INTO productosxfactura(id_producto, folio, cantidad, monto) VALUES (%s, %s, %s, %s);""", (id_producto, id_factura, cantidad, monto,))
