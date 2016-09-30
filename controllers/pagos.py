# -*- coding: utf-8 -*-
# try something like
def index(): 
    return dict(message="hello from ordenpagos.py")

@auth.requires_login()
def abm_bancos():
    return {"grilla": "ABM Bancos"}

@auth.requires_login()
def abm_bancos_guardar():
    n = int(request.vars["telefono"])
    db.banco.insert(nombre_banco=request.vars["banco"], telefono=n)
    return {"banco": "Datos guardados"}

@auth.requires_login()
def abm_cuenta_bancaria():
    q = db(db.banco).select()
    return {"grilla": "ABM Cuenta Bancaria", 'q':q}

@auth.requires_login()
def abm_cuenta_bancaria_guardar():
    id_b = (db.banco.nombre_banco == request.vars["nombre_banco"])
    registro = db.banco(id_b)
    db.cuenta_bancaria.insert(numero_cuenta=request.vars["cuenta_bancaria"], tipo_de_moneda=request.vars["tipo_moneda"], cbu=request.vars["cbu"], id_banco=registro.id_banco)
    return {"grilla": "Datos Guardados"}

@auth.requires_login()
def abm_cheques():
    q = db(db.cuenta_bancaria).select()
    qdos = db(db.pago).select()
    return {"grilla": "ABM Cheques", 'q':q, 'qdos':qdos}

@auth.requires_login()
def abm_cheques_guardar():
    id_b = (db.cuenta_bancaria.numero_cuenta == request.vars["id_cuenta_bancaria"])
    registro = db.cuenta_bancaria(id_b)
    id_bdos = (db.pago.num_orden_pago == request.vars["num_orden_pago"])
    registrodos = db.pago(id_bdos)
    db.cheque.insert(num_cheque=request.vars["num_cheque"], emision=request.vars["emision"], vencimiento=request.vars["vencimiento"], importe=request.vars["importe"], id_cuenta_bancaria=registro.id_cuenta_bancaria, id_pagos=registrodos.id_pagos)
    return {"grilla": "Datos Guardados"}

@auth.requires_login()
def generar_orden_pagos():
    q = db(db.compra).select()
    qdos = db(db.proveedor).select()
    return {"grilla": "Generar Orden pagos", 'q':q, 'qdos':qdos}

@auth.requires_login()
def generar_orden_pagos_guardar():
    db.pago.insert(num_orden_pago=request.vars["num_orden_pago"], fecha=request.vars["fecha"], importe=request.vars["importe"], id_compras=request.vars["id_compras"], id_proveedor=request.vars["razon_social"])
    return {"grilla": "Datos Guardados"}

@auth.requires_login()
def generar_reporte():
    return dict(message="Generar reporte de pagos")

@auth.requires_login()
def reporte_pagos():
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    registros = db((db.pago.fecha>=desde)&(db.pago.fecha<=hasta)).select()
    return dict({'titulo':"Listando desde fecha %s hasta fecha %s" % (desde, hasta), 'registros':registros})
