# -*- coding: utf-8 -*-
# try something like
import datetime
def index(): 
    return dict(message="hello from ordenpagos.py")

@auth.requires_login()
def alta_bancos():
    form = SQLFORM(db.banco, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Bancos", 'form':form})
    else :
        return {"grilla":"Alta Bancos", 'form':form}

@auth.requires_login()
def alta_cuenta_bancaria():
    form = SQLFORM(db.cuenta_bancaria, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Cuenta Bancaria", 'form':form})
    else :
        return {"grilla":"Alta Cuenta Bancaria", 'form':form}

@auth.requires_login()
def alta_cheques():
    if request.vars["siguiente"]:
        session["alta_cheque"][0]["vencimiento"] = request.vars["vencimiento"]
        session["alta_cheque"][0]["cuenta_bancaria"] = request.vars["cuenta_bancaria"]
        redirect(URL('pagos', 'confirmar_orden_pago'))
    cheque = db((db.cheque.id_cheques)).select().last()
    cta_bancaria = db((db.cuenta_bancaria)).select()
    if cheque == None:
        num_cheque = 1
    else :
        num_cheque = int(cheque.num_cheque) + 1
    importe = session["orden_de_pago"][0]["importe"]
    x = datetime.datetime.now()
    session["alta_cheque"] = []
    datos_cheque = {}
    datos_cheque["num_cheque"] = num_cheque
    datos_cheque["emision"] = "%s/%s/%s" % (x.day, x.month, x.year)
    datos_cheque["importe"] = importe
    session["alta_cheque"].append(datos_cheque)
    return {'alta_cheques':session["alta_cheque"], "cta_bancaria":cta_bancaria}

@auth.requires_login()
def factura_proveedor():
    proveedor_id = request.vars["id"]
    facturas = db((db.compra.id_proveedor == proveedor_id)).select()
    return {"facturas":facturas}


@auth.requires_login()
def buscar_proveedor():
    buscar = "Buscar proveedor"
    proveedor = None
    if request.vars["buscar_proveedor"]:
        nombre = request.vars["nombre_proveedor"]
        proveedor = db.proveedor((db.proveedor.razon_social == nombre))
    return {'buscar':buscar, 'proveedor':proveedor}

@auth.requires_login()
def generar_orden_pagos():
    if request.vars["ingresar_cheque"]:
        redirect(URL('pagos', 'alta_cheques'))
    compra_id = request.vars["id"]
    factura_compra = db.compra((db.compra.id_compra == compra_id))
    detalle_compra = db.detalle_compra((db.detalle_compra.id_compra == compra_id))
    pagos = db((db.pago.id_pagos)).select().last()
    if pagos == None:
        num_orden_pago = 1
    else :
        num_orden_pago = int(pagos.num_orden_pago) + 1
    x = datetime.datetime.now()
    session["orden_de_pago"] = []
    datos_orden_pago = {}
    datos_orden_pago["num_orden_pago"] = num_orden_pago
    datos_orden_pago["fecha"] = "%s/%s/%s" % (x.day, x.month, x.year)
    datos_orden_pago["importe"] = int(detalle_compra.precio) * int(detalle_compra.cantidad)
    datos_orden_pago["numero_de_factura"] = factura_compra.numero_factura
    datos_orden_pago["id_compra"] = factura_compra.id_compra
    datos_orden_pago["proveedor"] = factura_compra.id_proveedor.razon_social
    datos_orden_pago["proveedor_id"] = factura_compra.id_proveedor
    session["orden_de_pago"].append(datos_orden_pago)
    return {"orden_de_pago":session["orden_de_pago"]}

@auth.requires_login()
def confirmar_orden_pago():
    for datos in session["orden_de_pago"]:
        datos_pagos = datos
    for datos in session["alta_cheque"]:
        datos_cheque = datos
    #datos de la orden de pago
    num_orden_pago = datos_pagos["num_orden_pago"]
    fecha = datos_pagos["fecha"]
    importe = datos_pagos["importe"]
    numero_de_factura = datos_pagos["numero_de_factura"]
    id_compra = datos_pagos["id_compra"]
    proveedor_id = datos_pagos["proveedor_id"]
    #datos del cheque
    num_cheque = datos_cheque["num_cheque"]
    emision = datos_cheque["emision"]
    importe = datos_cheque["importe"]
    vencimiento = datos_cheque["vencimiento"]
    cuenta_bancaria = datos_cheque["cuenta_bancaria"]
    #insertar datos cheques
    db.cheque.insert(num_cheque=num_cheque, emision=emision, vencimiento=vencimiento, importe=importe, id_cuenta_bancaria=cuenta_bancaria)
    #insertar datos de orden de pago
    cheque_pago=db.cheque((db.cheque.num_cheque==num_cheque))
    db.pago.insert(num_orden_pago=num_orden_pago, fecha=fecha, importe=importe, id_compras=id_compra, id_proveedor=proveedor_id, id_cheque=cheque_pago.id_cheques)
    return {"confirmacion":"Datos guardados"}

@auth.requires_login()
def generar_reporte():
    return dict(message="Generar reporte de pagos")

@auth.requires_login()
def reporte_pagos():
    if request.vars["reporte_fecha"]:
        desde = request.vars["fecha_desde"]
        hasta = request.vars["fecha_hasta"]
        registros = db((db.pago.fecha>=desde)&(db.pago.fecha<=hasta)).select()
        titulo="Listando desde fecha %s hasta fecha %s" % (desde, hasta)
    if request.vars["reporte_nombre"]:
        nombre = request.vars["nombre_proveedor"]
        proveedor = db.proveedor((db.proveedor.razon_social == nombre))
        registros = db((db.pago.id_proveedor == proveedor)).select()
        titulo="Listado por nombre"
    return dict({'titulo':titulo, 'registros':registros})

def ver_orden_pago():
    num_orden_pago = request.vars["id"]
    orden_pago = db.pago((db.pago.id_pagos == num_orden_pago))
    cheque = db.cheque((db.cheque.id_pagos == num_orden_pago))
    print orden_pago
    return dict({'orden_pago':orden_pago, 'cheque':cheque})
