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

def legajos2():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

def legajos3():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}


def horas():
    grid = SQLFORM.grid(db.horas)
    return {"grilla": grid}

def familiar():
    grid = SQLFORM.grid(db.familiares)
    return {"grilla": grid}

def familiar2():
    grid = SQLFORM.grid(db.familiares)
    return {"grilla": grid}

def reportes_empleados():
    return dict()

def reportes_empleados2():
    return dict()

def reportes_horas():
    return dict()

def reportes_horas2():
    return dict()

def reportes_familiares():
    return dict()

def reportes_familiares2():
    return dict()
