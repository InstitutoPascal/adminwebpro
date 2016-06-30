# -*- coding: utf-8 -*-

def index():
    return dict(message="pagina predeterminada")

@auth.requires_login()
def abm_categoria():
    grid = SQLFORM.grid(db.categoria)
    return {"grilla": grid}

def abm_ejemplo():
    return dict(message="ABM EJEMPLO")

def reporte_ejemplo():
    return dict(message="REPORTE ejemplo")

def registrar_comprobante():
    return dict(message="REGISTRAR COMPROBANTE")
