# -*- coding: utf-8 -*-


def index(): return dict(message="hello from ventas.py")

@auth.requires_login()
def abm_clientes():
    grid = SQLFORM.grid(db.cliente)
    return {"grilla": grid}

@auth.requires_login()
def abm_ventas():
    #importamos libreria para el formato de la fecha
    import time
    #genera la fecha actual
    fecha_hoy= time.strftime("%x")
    # definir los campos a obtener desde la base de datos:
    campos = db.cliente.id_cliente, db.cliente.nombre_de_fantasia, db.cliente.razon_social
    # definir la condición que deben cumplir los registros:
    criterio = db.cliente.id_cliente>0
    # ejecutar la consulta:
    lista_clientes = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_clientes:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
    #redirije los valores al HTML
    return dict(message=mensaje, lista_clientes=lista_clientes, hoy=fecha_hoy,)


@auth.requires_login()
def detalle_ventas():
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        fecha = request.vars["fecha"]
        numero_factura = request.vars["numero_factura"]
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha"] = fecha
        session["numero_factura"] = numero_factura
        session["items_venta"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_producto = request.vars["id_producto"]
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.producto.id_producto==id_producto).select().first()
        item["detalle_producto"] = reg_producto.detalle_producto
        item["precio_venta"] = reg_producto.precio_venta
        item["alicuota_iva"] = reg_producto.alicuota_iva
        # guardo el item en la sesión
        session["items_venta"].append(item)
    # busco en la base de datos al cliente para mostrar su info
    registros = db(db.cliente.id_cliente==session["id_cliente"]).select()
    reg_cliente = registros[0]
    lista_productos = db(db.producto.id_producto>0).select()
    # le pasamos las variables a la vista para armar el html
    return dict(id_cliente=session["id_cliente"], fecha=session["fecha"],
                nro_cbte=session["numero_factura"],
                reg_cliente=reg_cliente, lista_productos=lista_productos,
                items_venta=session["items_venta"],
                )

def confirmar():
    reg_cliente = db(db.cliente.id_cliente==session["id_cliente"]).select().first()
    total = 0
    for item in session["items_venta"]:
        total += (item["precio_venta"] * item["cantidad"] + item["precio_venta"] * item["cantidad"] *item["alicuota_iva"]/100.00)
    return dict (mensaje= "Finalizar venta",
                 id_cliente=session["id_cliente"],
                 fecha=session["fecha"],
                 nro_cbte=session["numero_factura"],
                 reg_cliente=reg_cliente, total=total)

def guardado():
    # Agregar los registros a la base de datos:
    # encabezado:
    nuevo_id_venta = db.ventas.insert(
         id_cliente=session["id_cliente"],
         numero_factura=session["numero_factura"],
         fecha=session["fecha"],
         )
     # detalle (productos)
    for item in session["items_venta"]:
         db.detalle_ventas.insert(
            id_venta=nuevo_id_venta,
             id_producto=item["id_producto"],
             cantidad=item["cantidad"]
             )
    return dict (mensaje= "Se guardo con exito el comprobante id=%s" % nuevo_id_venta,
                 id_venta=nuevo_id_venta)
    return dict (mensaje= "Se guardo con exito el comprobante")

def vista_previa():
    #return dict(message="vista_previa")
    id_venta = request.args[0]
    reg_venta = db(db.ventas.id == id_venta).select().first()
    reg_cliente = db(db.cliente.id_cliente == reg_venta.id_cliente).select().first()
    # busco los datos de cada item vendido (id, cantidad, etc.) y del producto
    q = db.detalle_ventas.id_venta == id_venta
    q &= db.producto.id_producto == db.detalle_ventas.id_producto
    reg_detalle_ventas = db(q).select()
    return dict(message="vista_previa", 
                ventas=reg_venta, 
                cliente=reg_cliente, 
                items=reg_detalle_ventas,

                items_venta=session["items_venta"])


@auth.requires_login()
def reporte_ventas():
    return dict(message="reporte_ventas")

def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))

def reporte_por_cliente():
    campos = db.cliente.id_cliente, db.cliente.nombre_de_fantasia, db.cliente.razon_social
    # definir la condición que deben cumplir los registros:
    criterio = db.cliente.id_cliente>0
    # ejecutar la consulta:
    lista_clientes = db(criterio).select(*campos)
    return dict(lista_clientes=lista_clientes)

def lista_ventas_por_cliente():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))
