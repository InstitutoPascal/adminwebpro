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
        return {"grilla":"ABM Bancos", 'form':form}

@auth.requires_login()
def alta_cuenta_bancaria():
    form = SQLFORM(db.cuenta_bancaria, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Cuenta Bancaria", 'form':form})
    else :
        return {"grilla":"ABM Cuenta Bancaria", 'form':form}

@auth.requires_login()
def alta_cheques():
    form = SQLFORM(db.cheque, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Cheques", 'form':form})
    else :
        return {"grilla":"ABM Cheques", 'form':form}

@auth.requires_login()
def generar_orden_pagos():
    form = SQLFORM(db.pago, submit_button="Guardar")
    if form.accepts(request.vars, session):
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Pagos", 'form':form})
    else :
        return {"grilla":"ABM Pagos", 'form':form}

@auth.requires_login()
def generar_reporte():
    return dict(message="Generar reporte de pagos")

@auth.requires_login()
def reporte_pagos():
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    registros = db((db.pago.fecha>=desde)&(db.pago.fecha<=hasta)).select()
    return dict({'titulo':"Listando desde fecha %s hasta fecha %s" % (desde, hasta), 'registros':registros})
