# -*- coding: utf-8 -*-

def index():
    return dict(message="Index en sueldos.py")
def reporte_legajos():
    return dict(message="Reportes de legajos en sueldos.py")

@auth.requires_login()

def abm_empleados():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

def abm_familiares():
    return dict(message="Familiares en sueldos.py")

def abm_horas():
    return dict(message="Horas en sueldos.py")
