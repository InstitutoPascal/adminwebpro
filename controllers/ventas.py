# -*- coding: utf-8 -*-


def index(): return dict(message="hello from ventas.py")

@auth.requires_login()
def abm_clientes():
    grid = SQLFORM.grid(db.cliente)
    return {"grilla": grid}

def abm_ventas():
    return dict(message="abm ventas")


def comprobantes():
    return dict(message="comprobante")
