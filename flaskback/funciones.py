# FUNCIONES FACTURAS

def CreateFactura(cursor, cliente_id, descripcion, fecha_emision, monto_neto):
    cursor.execute("""SELECT folio FROM facturas ORDER BY folio DESC LIMIT 1;""")
    folio = cursor.fetchall()
    folio = folio[0][0] + 1
    cursor.execute("""INSERT INTO facturas(folio, cliente_id, descripcion, fecha_emision, monto_neto) VALUES (%s, %s, %s, %s, %s);""", (folio, cliente_id, descripcion, fecha_emision, monto_neto))

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

def createCotizacion(cursor, estado, cliente_id, fecha, total):
    cursor.execute("""INSERT INTO facturas(estado, cliente_id, fecha, total) VALUES (%s, %s, %s, %s);""", (estado, cliente_id, fecha, total))

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

def updateEstadoCotizacion(cursor, id, estado):
    cursor.execute("""UPDATE cotizaciones SET estado = %s WHERE id_cotizacion = %s;""", (id, estado,))

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

def getProductoById(cursor, id):
    cursor.execute("""SELECT * FROM productos WHERE productos id_producto = %s;""", (id,))
    return cursor.fetchall()

def getProductoByNombre(cursor, nombre):
    cursor.execute("""SELECT * FROM productos WHERE productos nombre = %s;""", (nombre,))
    return cursor.fetchall()

def updateNombreProducto(cursor, id, nombre):
    cursor.execute("""UPDATE productos SET nombre = %s WHERE id_producto = %s;""", (nombre, id,))

def updateCostoProducto(cursor, id, costo_neto):
    cursor.execute("""UPDATE productos SET costo_neto = %s WHERE id_producto = %s;""", (costo_neto, id,))

def updateDescripcionProducto(cursor, id, descripcion):
    cursor.execute("""UPDATE productos SET descripcion = %s WHERE id_producto = %s;""", (descripcion, id,))

def deleteProducto(cursor, id):
    cursor.execute("""DELETE FROM productos WHERE id_producto = %s;""", (id,))
