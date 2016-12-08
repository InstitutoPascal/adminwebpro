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
def buscar_proveedor():
    buscar = "Buscar proveedor"
    if request.vars["buscar_proveedor"]:
        nombre = request.vars["nombre_proveedor"]
        proveedor = db.proveedor((db.proveedor.razon_social == nombre))
        redirect(URL('pagos', 'ver_factura_proveedor', vars=dict(proveedor=proveedor)))
    return {'buscar':buscar}

@auth.requires_login()
def generar_orden_pagos():
    form = SQLFORM(db.pago, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        redirect(URL('pagos', 'alta_cheques'))
    else :
        return {"grilla":"Generar Orden de Pagos", 'form':form}

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
