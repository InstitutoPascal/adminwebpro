# -*- coding: utf-8 -*-


def index(): return dict(message="hello from proveedor.py")

@auth.requires_login()
def abm_proveedor():
    grid = SQLFORM.grid(db.proveedor)
    return {"grilla": grid}
@auth.requires_login()
def abm_factura():
    grid = SQLFORM.grid(db.factura_compra)
    return {"grilla": grid}

def comprobantes():
    return dict(message="comprobante")
