# -*- coding: utf-8 -*-
# try something like
def index(): 
    return dict(message="hello from ordenpagos.py")

@auth.requires_login()
def abm_bancos():
    grid = SQLFORM.grid(db.banco)
    return {"grilla": grid}

@auth.requires_login()
def abm_cuenta_bancaria():
    grid = SQLFORM.grid(db.cuenta_bancaria)
    return {"grilla": grid}

@auth.requires_login()
def abm_cheques():
    grid = SQLFORM.grid(db.cheque)
    return {"grilla": grid}

@auth.requires_login()
def generar_orden_pagos():
    grid = SQLFORM.grid(db.pago)
    return {"grilla": grid}

def reporte_pagos():
    return dict(message="hello from ordenpagos.py")
