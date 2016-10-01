# -*- coding: utf-8 -*-
# try something like
def index(): 
    return dict(message="hello from ordenpagos.py")

@auth.requires_login()
def abm_bancos():
    if request.vars["boton_guardar"]:
        banco = request.vars["banco"]
        telefono = request.vars["telefono"]
        db.banco.insert(nombre_banco=banco, telefono=telefono)
        response.flash = "Datos Guardados"
        return dict({"grilla":"ABM Bancos"})
    else :
        return {"grilla":"ABM Bancos"}

@auth.requires_login()
def abm_cuenta_bancaria():
    if request.vars["boton_guardar"]:
        numero_cuenta = request.vars["cuenta_bancaria"]
        tipo_de_moneda = request.vars["tipo_moneda"]
        cbu = request.vars["cbu"]
        id_banco = request.vars["nombre_banco"]
        db.cuenta_bancaria.insert(numero_cuenta=numero_cuenta, tipo_de_moneda=tipo_de_moneda, cbu=cbu, id_banco=id_banco)
        response.flash = "Datos Guardados"
    q = db(db.banco).select()
    return {"grilla": "ABM Cuenta Bancaria", 'q':q}

@auth.requires_login()
def abm_cheques():
    if request.vars["boton_guardar"]:
        num_cheque = request.vars["num_cheque"]
        emision = request.vars["emision"]
        vencimiento = request.vars["vencimiento"]
        importe = request.vars["importe"]
        id_cuenta_bancaria = request.vars["id_cuenta_bancaria"]
        id_pagos = request.vars["id_pagos"]
        db.cheque.insert(num_cheque=num_cheque, emision=emision, vencimiento=vencimiento, importe=importe, id_cuenta_bancaria=id_cuenta_bancaria, id_pagos=id_pagos)
        response.flash = "Datos Guardados"
    q = db(db.cuenta_bancaria).select()
    qdos = db(db.pago).select()
    return {"grilla": "ABM Cheques", 'q':q, 'qdos':qdos}

@auth.requires_login()
def generar_orden_pagos():
    if request.vars["boton_guardar"]:
        num_orden_pago = request.vars["num_orden_pago"]
        fecha = request.vars["fecha"]
        importe = request.vars["importe"]
        id_compras = request.vars["id_compras"]
        id_proveedor = request.vars["razon_social"]
        db.pago.insert(num_orden_pago=num_orden_pago, fecha=fecha, importe=importe, id_compras=id_compras, id_proveedor=id_proveedor)
        response.flash = "Datos Guardados"
    q = db(db.compra).select()
    qdos = db(db.proveedor).select()
    return {"grilla": "Generar Orden pagos", 'q':q, 'qdos':qdos}

@auth.requires_login()
def generar_reporte():
    return dict(message="Generar reporte de pagos")

@auth.requires_login()
def reporte_pagos():
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    registros = db((db.pago.fecha>=desde)&(db.pago.fecha<=hasta)).select()
    return dict({'titulo':"Listando desde fecha %s hasta fecha %s" % (desde, hasta), 'registros':registros})
