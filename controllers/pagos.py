# -*- coding: utf-8 -*-
# try something like
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
    form = SQLFORM(db.cheque, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return {"grilla":"Alta Cheques", 'form':form}
    else :
        return {"grilla":"Alta Cheques", 'form':form}

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
    compra_id = request.vars["id"]
    factura_compra = db.compra((db.compra.id_compra == compra_id))
    detalle_compra = db.detalle_compra((db.detalle_compra.id_compra == compra_id))
    pagos = db((db.pago.id_pagos)).select().last()
    if pagos == None:
        num_orden_pago = 1
    else :
        num_orden_pago = int(pagos.num_orden_pago) + 1
    return {'num_orden_pago':num_orden_pago, "factura_compra":factura_compra, "detalle_compra":detalle_compra}

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
