# -*- coding: utf-8 -*-


def index(): return dict(message="hello from proveedor.py")

@auth.requires_login()
def abm_proveedor():
    grid = SQLFORM.grid(db.proveedor)
    return {"grilla": grid}
@auth.requires_login()
def abm_factura():
    grid = SQLFORM.grid(db.compra)
    return {"grilla": grid}

def informe_subdiarioa():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiarioa")

def informe_subdiariob():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiariob")

def listado_proveedor():
       # presentar formulario para criterios de busqueda
    return dict(message="Listado Proveedor")


def formulario_compras():
       # presentar formulario para criterios de busqueda
    return dict(message="Formulario Compras")


def formulario_proveedores():
           # presentar formulario para criterios de busqueda
    return dict(message="Formulario Proveedores")
