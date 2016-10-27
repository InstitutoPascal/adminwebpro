# -*- coding: utf-8 -*-

from datetime import date

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

def legajos2():
    if request.vars["boton_siguiente"]:
        # obtengo los valores completados en el formulario
        nro_legajo = request.vars["nro_legajo"]
        fecha_egreso = request.vars["fecha_egreso"]
        cuil = request.vars["cuil"]
        
        # guardo los datos elegidos en la sesión
        session["nro_legajo"] = nro_legajo
        session["fecha_egreso"] = fecha_egreso
        session["nro_comprobante"] = nro_comprobante
        session["cuil"] = cuil
        print session["cuil"]
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}
def legajos():
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
    dt_str = fecha_desde
    dt_obj = datetime.strptime(dt_str, '%Y-%m-%d')
    fecha_desde = dt_obj
    dt_str2 = fecha_hasta
    dt_obj2 = datetime.strptime(dt_str2, '%Y-%m-%d')
    fecha_hasta = dt_obj2
    ordenar = request.vars["ordenar"]
    
    campos = db.legajos.num_legajo, db.legajos.nombre, db.legajos.apellido, db.legajos.fecha_ingreso
    criterio = db.legajos.fecha_ingreso >= fecha_desde
    criterio &= db.legajos.fecha_ingreso <= fecha_hasta
    
    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre, 
    else:
        orden = db.legajos.num_legajo

    registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_empleados=registros,fecha_desde=fecha_desde,fecha_hasta=fecha_hasta,titulo="Listando desde fecha %s hasta fecha %s" % (fecha_desde.date(), fecha_hasta.date()))

# obtenemos los criterios de busqueda y generamos el reporte
# desde = request.vars["fecha_desde"]
# hasta = request.vars["fecha_hasta"]
# return dict(titulo="Listando desde fecha %s hasta fecha %s" % (fecha_desde, fecha_hasta))

def reportes_empleados2():
    return dict()

def reportes_horas():
    Legajo = request.vars["Legajo"]
    Mes = request.vars["Mes"]
    ordenar = request.vars["ordenar"]
    
    campos = db.horas.num_legajo, db.legajos.nombre, db.legajos.apellido, db.horas.hs_trab,
    criterio = db.horas.num_legajo >= Legajo
    criterio &= db.horas.mes_trabajado <= Mes
    
    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre,db.horas.hs_trab, db.horas.mes_trabajado, 
    else:
        orden = db.legajos.num_legajo

    registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_horas=registros)

    return dict()

def reportes_horas2():
    return dict()

def reportes_familiares():
    familia_menor21 = request.vars["familia_menor21"]
    familia_estudian = request.vars["familia_estudian"]
    familiar_distdom = request.vars["familiar_distdom"]
    
    campos = db.familiares.num_legajo, db.familiares.nombre, db.familiares.apellido, db.familiares.estudia,db.familiares.edad,
    criterio = db.familiares.num_legajo == db.legajos.num_legajo
    
    if familia_menor21:
        criterio &=  db.familiares.edad < 21
        subtitulo = "Familiares menores de 21 años"
    if familia_estudian:
        criterio &=  db.familiares.estudia == True
        subtitulo = "Familiares que estudian"
    if familiar_distdom:
        criterio &=  db.familiares.domicilio_calle == db.legajos.dom_calle
        subtitulo = "Familiares con distinto domicilio"
    registros = db(criterio).select(*campos)
    return dict(lista_familiares=registros,titulo="Listando %s" % subtitulo)


def reportes_familiares2():
    return dict()
