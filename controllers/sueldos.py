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
    fecha_desde = request.vars["fecha_desde"]
    fecha_hasta = request.vars["fecha_hasta"]
    ordenar = request.vars["ordenar"]
    
    campos = db.legajos.num_legajo, db.legajos.nombre, db.legajos.apellido,
    criterio = db.legajos.fecha_ingreso >= fecha_desde
    criterio &= db.legajos.fecha_ingreso <= fecha_hasta
    
    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre, 
    else:
        orden = db.legajos.num_legajo

    registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_empleados=registros)

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
