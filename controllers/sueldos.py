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
    import os
    form = SQLFORM.factory(Field('nro_legajo',requires=IS_NOT_EMPTY(error_message='Ingrese el número de legajo')),
                           Field('fecha_egreso','date',requires=IS_NOT_EMPTY(error_message='Ingrese la fecha')),
                          Field('cuil',requires=IS_NOT_EMPTY(error_message='Ingrese el cuil')),
                           Field('dni',requires=IS_NOT_EMPTY(error_message='Ingrese el dni')),
                           Field('corresponde_hs_extra',requires=IS_IN_SET({1:'si',2:'no'},error_message='Ingrese una opción',zero='Seleccionar...')),
                           Field('nombres',requires=IS_NOT_EMPTY(error_message='Ingrese el nombre')),
                           Field('apellido',requires=IS_NOT_EMPTY(error_message='Ingrese el apellido')),
                           Field('fecha_nacimiento','date'),
                           Field('lugar_nacimiento','string'),
                           Field('estado_civil','string'),
                           Field('edad','string'),
                           Field('categoria','string'),
                           Field('domicilio_calle','string'),
                           Field('numero_calle','string'),
                           Field('piso','string'),
                           Field('depto','string'),
                           Field('imagen','upload',uploadfolder=os.path.join(request.folder,'uploads')),
                           submit_button='Siguiente'
                          )

    if form.process().accepted:
        try:
            image = db.legajos.image.store(request.vars["imagen"].file, request.vars["imagen"].filename)
            session["imagen"] = image
        except:
            session['imagen'] = None
        session["nro_legajo"] = request.vars['nro_legajo']
        session["fecha_egreso"] = request.vars['fecha_egreso']
        session["cuil"] = request.vars['cuil']
        session["dni"] = request.vars['dni']
        session["horas_extras"] = request.vars['corresponde_hs_extra']
        session["nombre"] = request.vars['nombres']
        session["apellido"] = request.vars['apellido']
        session["fecha_nacimiento"] = request.vars['fecha_nacimiento']
        session["lugar_nacimiento"] = request.vars['lugar_nacimiento']
        session["estado_civil"] = request.vars['estado_civil']
        session["edad"] = request.vars['edad']
        session["categoria"] = request.vars['categoria']
        session["domicilio"] = request.vars['domicilio_calle']
        session["num_domicilio"] = request.vars['numero_calle']
        session["piso"] = request.vars['piso']
        session["depto"] = request.vars['depto']
        redirect(URL(c='sueldos',f='legajos2'))
    
    grid = SQLFORM.grid(db.legajos)
    return locals()

def legajos2():
    form = SQLFORM.factory(Field('obra_social'),
                           Field('codigo_postal'),
                           Field('localidad'),
                           Field('email'),
                           Field('fecha_ingreso','date'),
                           Field('telefono',label='Teléfono'),
                           Field('telefono_celular',label='Teléfono Celular'),
                           Field('estudia',label='Estudia?',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('cons_cuil',label='Constancia de cuil',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('alt_tem',label='Alta temprana',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('foto_dni',label='Fotocopia de DNI',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('libreta',requires=IS_IN_SET(['corresponde','no corresponde'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('lib_pre','boolean'),
                           Field('partida',requires=IS_IN_SET(['corresponde','no corresponde'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('part_pre','boolean'),
                          )
    if form.process().accepted:
        print session['depto']
        id = db.legajos.insert(
            image = session["imagen"],
            num_legajo = session["nro_legajo"],
            fecha_egreso = session["fecha_egreso"],
            cuil = session["cuil"],
            dni = session["dni"],
            horas_extras = session["horas_extras"],
            nombre = session["nombre"],
            apellido = session["apellido"],
            fe_nac = session["fecha_nacimiento"] ,
            lu_nac = session["lugar_nacimiento"],
            est_civ = session["estado_civil"],
            edad = session["edad"],
            categoria = session["categoria"],
            dom_calle = session["domicilio"],
            dom_numero= session["num_domicilio"],
            piso = session["piso"],
            depto = session['depto']
        )
        #EN el insert faltan agregar los datos que estan en este form 
        
        redirect(URL(c='sueldos',f='legajos3'))
    
    return locals()

def legajos3():
    print session ["imagen"]
    
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
        criterio &=  db.familiares.domicilio_calle != db.legajos.dom_calle
        criterio |=  db.familiares.domicilio_numero != db.legajos.dom_numero
        subtitulo = "Familiares con distinto domicilio"
    registros = db(criterio).select(*campos)
    return dict(lista_familiares=registros,titulo="Listando %s" % subtitulo)


def reportes_familiares2():
    return dict()
