def CreateFactura(cursor, folio, cliente_id, descripcion, fecha_emision, monto_neto):
    cursor.execute("""INSERT INTO facturas VALUES (%s, %s, %s, %s, %s);""", (folio, cliente_id, descripcion, fecha_emision, monto_neto))

def getFacturas(cursor, hoja):
    limite = (hoja * 10)
    cursor.execute("""SELECT * FROM facturas LIMIT 10 OFFSET %s;""", (limite,))
    return cursor.fetchall()

def getCotizaciones(cursor, hoja):
    limite = (hoja * 10)
    cursor.execute("""SELECT * FROM cotizaciones LIMIT 10 OFFSET %s;""", (limite,))
    return cursor.fetchall()

def getFacturasByFolio(cursor, folio):
    cursor.execute("""SELECT * FROM facturas WHERE  folio = %s;""", (folio,))
    return cursor.fetchall()

def getCotizacionesById(cursor, id):
    cursor.execute("""SELECT * FROM cotizaciones WHERE  id_cotizacion = %s;""", ( id,))
    return cursor.fetchall()

def getFacturasByClienteId(cursor, clienteId):
    cursor.execute("""SELECT * FROM facturas WHERE  cliente_id = %s;""", ( clienteId,))
    return cursor.fetchall()

def getCotizacionesByClienteId(cursor, clienteId):
    cursor.execute("""SELECT * FROM cotizaciones WHERE  cliente_id = %s;""", ( clienteId,))
    return cursor.fetchall()

def getFacturasByFecha(cursor, fecha1, fecha2):
    cursor.execute("""SELECT * FROM facturas WHERE fecha_emision >= %s AND fecha_emision <= %s;""", ( fecha1, fecha2,))
    return cursor.fetchall()

def getCotizacionesByFecha(cursor, fecha1, fecha2):
    cursor.execute("""SELECT * FROM cotizaciones WHERE fecha >= %s AND fecha <= %s;""", ( fecha1, fecha2,))
    return cursor.fetchall()

def deleteCotizacion(cursor, id):
    cursor.execute("""DELETE FROM cotizaciones WHERE id_cotizacion = %s;""", ( id,))

