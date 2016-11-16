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

def legajos():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

def legajos():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}



def legajos2():
     if request.vars["buton_siguiente"]:
        # obtengo los valores completados en el formulario
        #image = db.legajos.image.store(request.vars["imagen"].file, request.vars["imagen"].filename)
        nro_legajo = request.vars["nro_legajo"]
        fecha_egreso = request.vars["fecha_egreso"]
        cuil = request.vars["cuil"]
        dni = request.vars["dni"]
        horas_extras = request.vars["horas_extras"]
        nombre = request.vars["nombre"]
        apellido = request.vars["apellido"]
        fecha_nacimiento = request.vars["fecha_nacimiento"]
        lugar_nacimiento = request.vars["lugar_nacimiento"]
        estado_civil = request.vars["estado_civil"]
        edad = request.vars["edad"]
        categoria = request.vars["categoria"]
        domicilio = request.vars["domicilio"]
        num_domicilio = request.vars["num_domicilio"]
        piso = request.vars["piso"]
        depto = request.vars["depto"]

        # guardo los datos elegidos en la sesión
        #session["imagen"] = image
        session["nro_legajo"] = nro_legajo
        session["fecha_egreso"] = fecha_egreso
        session["cuil"] = cuil
        session["dni"] = dni
        session["horas_extras"] = horas_extras
        session["nombre"] = nombre
        session["apellido"] = apellido
        session ["fecha_nacimiento"] = fecha_nacimiento
        session ["lugar_nacimiento"] = lugar_nacimiento
        session ["estado_civil"] = estado_civil
        session ["edad"] = edad
        session ["categoria"] = categoria
        session ["domicilio"] = domicilio
        session ["num_domicilio"] = num_domicilio
        session ["piso"] = piso
        session ["depto"] = depto
        grid = SQLFORM.grid(db.legajos)
        return {"grilla": grid}

def legajos2():
    grid = SQLFORM.grid(db.legajos)
    return {"grilla": grid}

def legajos3():
    print session ["imagen"]
    id = db.legajos.insert(
         #   image = session ["imagen"],
            num_legajo = session["nro_legajo"],
            fecha_egreso = session["fecha_egreso"],
            cuil = session["cuil"],
            dni = session["dni"],
            horas_extras = session["horas_extras"],
            nombre = session["nombre"],
            apellido = session["apellido"],
            fe_nac = session ["fecha_nacimiento"] ,
            lu_nac = session ["lugar_nacimiento"],
            est_civ = session ["estado_civil"],
            edad = session ["edad"],
            categoria = session ["categoria"],
            dom_calle = session ["domicilio"],
            dom_numero= session ["num_domicilio"],
            piso = session ["piso"],
            depto = session ["depto"],

    )
    return {"msg": "se agrego id = %s" % id}



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
    mes = request.vars["mes"]
    ordenar = request.vars["ordenar"]

    campos = db.horas.num_legajo, db.legajos.nombre, db.legajos.apellido, db.horas.hs_trab, db.horas.mes_trabajado
    criterio = db.horas.num_legajo >= Legajo
    criterio &= db.horas.mes_trabajado == mes

    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre,db.horas.hs_trab, db.horas.mes_trabajado,
    else:
        orden = db.legajos.num_legajo

    registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_horas=registros, mes=mes, titulo="Listando desde Mes %s" % (mes))

    return dict()

def reportes_horas2():
    return dict()

def reportes_familiares():
    familia_menor21 = request.vars["familia_menor21"]
    familia_estudian = request.vars["familia_estudian"]
    familiar_distdom = request.vars["familiar_distdom"]

    campos = db.familiares.num_legajo, db.familiares.nombre, db.familiares.apellido, db.familiares.estudia, db.familiares.edad, db.familiares.domicilio_calle, db.legajos.dom_calle, db.familiares.domicilio_numero
    criterio = db.familiares.num_legajo == db.legajos.num_legajo

    if familia_menor21:
        criterio &=  db.familiares.edad < 21
        subtitulo = "Familiares menores de 21 años"
    if familia_estudian:
        criterio &=  db.familiares.estudia == "Si"
        subtitulo = "Familiares que estudian"
    if familiar_distdom:
        criterio = db.familiares.num_legajo == db.legajos.num_legajo
        criterio &=  ((db.familiares.domicilio_calle != db.legajos.dom_calle) |  (db.familiares.domicilio_numero != db.legajos.dom_numero))
        subtitulo = "Familiares con distinto domicilio"
    registros = db(criterio).select(*campos)
    return dict(lista_familiares=registros,titulo="Listando %s" % subtitulo)


def reportes_familiares2():
    return dict()
