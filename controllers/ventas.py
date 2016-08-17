# -*- coding: utf-8 -*-


def index(): return dict(message="hello from ventas.py")

@auth.requires_login()
def abm_clientes():
    grid = SQLFORM.grid(db.cliente)
    return {"grilla": grid}

@auth.requires_login()
def abm_ventas():
    grid = SQLFORM.grid(db.ventas)
    return {"grilla": grid}

@auth.requires_login()
def detalle_ventas():
    grid = SQLFORM.grid(db.detalle_ventas)
    return {"grilla": grid}

def comprobantes():
    return dict(message="comprobante")
