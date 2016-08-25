# -*- coding: utf-8 -*-

def index():
    return dict(message="Index en sueldos.py")


@auth.requires_login()

def abm_empleados():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

@auth.requires_login()

def abm_familiares():
    grid = SQLFORM.grid(db.familiares)
    return {"grilla": grid}


@auth.requires_login()
def abm_horas():
    grid = SQLFORM.grid(db.horas)
    return {"grilla": grid}

def legajos():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

def reportes_empleados():
    return dict()
