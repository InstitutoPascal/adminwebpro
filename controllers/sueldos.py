# -*- coding: utf-8 -*-
import time
def index():
    return dict(message="Index en sueldos.py")

@auth.requires_login()
def mostrar_formulario():
    registro = db.legajos(request.args(0))
    form = SQLFORM(db.legajos, registro, deletable=True,
                  upload=URL('download'))
    if form.process().accepted:
        response.flash = 'formulario aceptado'
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    return dict(form=form)

def mostrar_imagen():
    registro = db.legajos(request.args(0))
    form = SQLFORM(db.horas, registro, deletable=True,
                  upload=URL('download'))
    if form.process().accepted:
        response.flash = 'formulario aceptado'
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    return dict(form=form)



def download():
    return response.download(request, db)


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
    # definir los campos a obtener desde la base de datos:
    import os
    form = SQLFORM.factory(
        Field('nro_legajo','primary key',requires=[IS_NOT_EMPTY(error_message='Ingrese el número de legajo'),
                                                  IS_NOT_IN_DB(db,db.legajos.num_legajo,error_message='el legajo no puede repetirse')]),
         Field('fecha_egreso','date'),
         Field('cuil','integer',requires=[IS_NOT_EMPTY(error_message= 'Ingrese el cuil'),
                                         IS_NOT_IN_DB(db, db.legajos.cuil,error_message='el cuil no puede repetirse')]),
         Field('dni','integer',requires=[IS_NOT_EMPTY(error_message='Ingrese el dni'),
                                        IS_NOT_IN_DB(db,db.legajos.dni,error_message='el dni no puede repetirse')]),
         Field('corresponde_hs_extra',requires=IS_IN_SET({1:'si',2:'no'},error_message='Ingrese una opción',zero='Seleccionar...')),
         Field('nombres',requires=IS_NOT_EMPTY(error_message='Ingrese el nombre')),
         Field('apellido',requires=IS_NOT_EMPTY(error_message='Ingrese el apellido')),
         Field('fecha_nacimiento','date'),
         Field('lugar_nacimiento','string'),
         Field('estado_civil', requires=IS_IN_SET(['Soltero','Casado','Viudo'],zero='Seleccione...',error_message='el campo no puede estar vacio')),
         Field('categoria','string'),
         Field('domicilio_calle','string',requires=IS_NOT_EMPTY(error_message= 'Ingrese el domicilio')),
         Field('numero_calle','integer',requires=IS_NOT_EMPTY(error_message= 'Ingrese la altura ')),
         Field('piso','string'),
         Field('depto','string'),
         submit_button="siguiente"
        )
    if form.process().accepted:
        
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
        session["categoria"] = request.vars['categoria']
        session["domicilio"] = request.vars['domicilio_calle']
        session["num_domicilio"] = request.vars['numero_calle']
        session["piso"] = request.vars['piso']
        session["depto"] = request.vars['depto']
        redirect(URL(c='sueldos',f='legajos2'))
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'

    grid = SQLFORM.grid(db.legajos)
    return locals()

def legajos2():
    form = SQLFORM.factory(Field('obra_social',"string"),
                           Field('codigo_postal',"integer"),
                           Field('localidad',"string"),
                           Field('email',"string",requires = IS_EMAIL(error_message='¡El mail no es válido!')),
                           Field('fecha_ingreso','date',requires=IS_NOT_EMPTY(error_message='ingrese fecha de ingreso')),
                                                       
                           Field('telefono',"string",requires=IS_NOT_EMPTY(error_message='Ingrese el telefono de contacto')),
                           Field('telefono_celular',"string"),
                           Field('estudia',label='Estudia?',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('cons_cuil',label='Constancia de cuil',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('alt_tem',label='Alta temprana',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('foto_dni',label='Fotocopia de DNI',requires=IS_IN_SET(['si','no'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('libreta',requires=IS_IN_SET(['corresponde','no corresponde'],zero='Seleccionar...',error_message='Indique una opción')),
                           Field('lib_pre','boolean'),
                           Field('partida',requires=IS_IN_SET(['corresponde','no corresponde'],zero='Seleccionar...',error_message='Indique una opción')),
                          )
    if form.process().accepted:
        #la sesion no hace falta que se llame como el vars
        session["obrasocial"] = request.vars["obra_social"]
        session["codigopostal"] = request.vars["codigo_postal"]
        session["localidad"] = request.vars["localidad"]
        session["email"] = request.vars["email"]
        session["fechaingreso"] = request.vars["fecha_ingreso"]
        session["telefono"] = request.vars["telefono"]
        session["celular"] = request.vars["telefono_celular"]
        session["estudia"] = request.vars["estudia"]
        session["constancia_cuil"] = request.vars["cons_cuil"]
        session["alta_temprana"] = request.vars["alt_tem"]
        session["fotodni"] = request.vars["foto_dni"]
        session["libreta"] = request.vars["libreta"]
        session["lib_pre"] = request.vars["lib_pre"]
        session["partida"] = request.vars["partida"]
        session["part"] = request.vars["part_pre"]
        redirect(URL(c='sueldos',f='legajos3'))
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    return locals()

def legajos3():
    form = SQLFORM.factory(Field("fotocopia_dni_hijos","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("fotocopia_dni_conyuge","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("constancia_cuil_hijos","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("constancia_cuil_conyuge","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("constancia_Alumno_Regular_Hijo","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("constancia_Alumno_Regular_empleado","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                          
                           Field("curriculum_empleado","string",requires=IS_IN_SET(["corresponde","no corresponde"],zero='Seleccionar...',error_message='Indique una opción')),
                           Field("image","upload",requires=IS_UPLOAD_FILENAME(extension='jpg',error_message='ingrese formato de imagen jpg')),table_name='legajos',
                           submit_button='Guardar'
                          )
        
    if form.process().accepted:
        
        imagen_upload = None
        
        try:
            imagen_upload = form.vars.image 
        except Exception as e:
            print e,"error"
            #si tengo razon web2py tiene un bug
        
        legajo_id = db.legajos.insert(
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
            categoria = session["categoria"],
            dom_calle = session["domicilio"],
            dom_numero= session["num_domicilio"],
            piso = session["piso"],
            depto = session['depto'],
            obra_social = session["obrasocial"],
            codigo_postal = session["codigopostal"] ,
            localidad = session["localidad"] ,
            email = session["email"] ,
            fecha_ingreso = session["fechaingreso"],
            telefono = session["telefono"] ,
            celular = session["celular"] ,
            estudia = session["estudia"] ,
            constancia_de_cuil = session["constancia_cuil"],
            alta_temprana = session["alta_temprana"],
            fotocopia_dni = session["fotodni"] ,
            libreta_familia = session["libreta"] ,
            image = imagen_upload,
            partida_nacimiento_hijos = session["partida"] ,
            fotocopia_dni_hijos= request.vars["fotocopia_dni_hijos"],
            fotocopia_dni_conyuge= request.vars["fotocopia_dni_conyuge"],
            constancia_cuil_hijos = request.vars["constancia_cuil_hijos"],
            constancia_cuil_conyuge = request.vars["constancia_cuil_conyuge"],
            constancia_Alumno_Regular_Hijo = request.vars["constancia_Alumno_Regular_Hijo"],
            constancia_Alumno_Regular_empleado = request.vars["constancia_Alumno_Regular_empleado"],
            curriculum_empleado = request.vars["curriculum_empleado"],
        )
        redirect(URL(c='sueldos',f='vista_previa',args =legajo_id))
        #EN el insert faltan agregar los datos que estan en este for
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    return locals()

def vista_previa():
    legajo_id = request.args(0)
    edad_num = None
    fecha_parse = None
    recordset = db(db.legajos.id == legajo_id ).select().first()
    
    if recordset:
        if recordset.fe_nac is not None:
            edad_num = edad(recordset.fe_nac)
            fecha_parse = recordset.fe_nac.strftime("%d/%m/%Y")
    return locals()

def vista_previa_horas():
    hora_id = request.args(0)
    recordset = db(db.horas.id == hora_id ).select().first()
    return locals()

def vista_previa_familiar():
    familiar_id = request.args(0)
    edad_num = None
    fecha_parse = None
    recordset = db(db.familiares.id == familiar_id ).select().first()
    if recordset:
        if recordset.fe_nac is not None:
            edad_num = edad(recordset.fe_nac)
            fecha_parse = recordset.fe_nac.strftime("%d/%m/%Y")
    return locals()
def edad(fecha_nacimiento):
        from datetime import datetime
        return int((datetime.now().date() - fecha_nacimiento).days / 365.25)


def horas():
    import os
    form = SQLFORM.factory(Field('nro_legajo',requires= IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s",zero='seleccionar...',error_message='seleccione numero de legajo')), 
                               Field('mes_trab',requires=IS_IN_SET(['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],zero='seleccionar...',error_message='seleccione una opcion')),
                           Field('semana',requires=IS_IN_SET({1:'1',2:'2',3:'3',4:'4',5:'5'},error_message='Ingrese una opción',zero='Seleccionar...')),
                           Field('horas_trab','integer',requires=IS_NOT_EMPTY(error_message= 'ingrese cantidad de horas')),
                           Field('horas_extras','integer',requires=IS_NOT_EMPTY(error_message= 'ingrese cantidad de horas extras')),
                           
     )
    
    if form.process().accepted:
        hora_id = db.horas.insert(
            num_legajo = request.vars["nro_legajo"],
            mes_trabajado = request.vars["mes_trab"],
            semana = request.vars["semana"],
            hs_trab = request.vars["horas_trab"],
            hs_ext = request.vars["horas_extras"]
            )
        redirect(URL(c='sueldos',f='vista_previa_horas',args =hora_id))
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    return locals()


def familiar():
    import os
    form = SQLFORM.factory(Field("num_legajo",requires= IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s",error_message='el campo no puede estar vacio')),
                                                        
                                 
    Field("cuil","integer",requires= [IS_NOT_EMPTY(error_message='el campo no puede estar vacio'),
                                      IS_NOT_IN_DB(db, db.familiares.cuil,error_message='el cuil ya existe en la base de datos')]),
    Field("dni","integer", requires = [IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio"),
                                       IS_NOT_IN_DB(db, db.familiares.dni,error_message='el dni ya esta en la base de datos')]),
    Field("nombre",requires = IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio"),),
    Field("apellido", requires = IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio")),
    Field("fe_nac","date"),
    Field("lu_nac","string"),
    Field("est_civ",requires=IS_IN_SET(['soltero','casado','viudo','otro'],zero='Seleccione...',error_message='Indique una opción')),
    Field("domicilio_calle",requires = IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio")),
    Field("domicilio_numero","integer",requires = IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio")),
    submit_button='Siguiente'
        )
    if form.process().accepted:
        #la sesion no hace falta que se llame como el vars
        session["num_legajo"] = request.vars["num_legajo"]
        session["cuil"] = request.vars["cuil"]
        session["dni"] = request.vars["dni"]
        session["nombre"] = request.vars["nombre"]
        session["apellido"] = request.vars["apellido"]
        session["fe_nac"] = request.vars["fe_nac"]
        session["lu_nac"] = request.vars["lu_nac"]
        session["est_civ"] = request.vars["est_civ"]
        session["domicilio_calle"] = request.vars["domicilio_calle"]
        session["domicilio_numero"] = request.vars["domicilio_numero"]
        redirect(URL(c='sueldos',f='familiar2'))
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    return locals()
    
    
def familiar2():
    form = SQLFORM.factory(
    Field("domicilio_piso","string"),
    Field("domicilio_depto","string"),
    Field("codigo_postal",requires = IS_NOT_EMPTY(error_message= "campo obligatorio no puede estar vacio")),
    Field("localidad","string"),
    Field("email","string",requires = IS_EMAIL(error_message='¡El mail no es válido!')),
        Field("telefono","integer",requires=IS_NOT_EMPTY(error_message='ingrese telefono de contacto')),
    Field("celular","integer"),
    Field("estudia",requires=IS_IN_SET(['si','no'],zero='Seleccione...',error_message='Indique una opción')),
    Field("parentezco","string",requires=IS_IN_SET(['Conyuge','Hijo','Familiar'],zero='Seleccione...',error_message='Indique una opción')),
        )
    if form.process().accepted:
        familiar_id = db.familiares.insert(
            num_legajo = session["num_legajo"],
            cuil = session["cuil"],
            dni = session["dni"],
            nombre = session["nombre"],
            apellido = session["apellido"],
            fe_nac = session["fe_nac"],
            lu_nac = session["lu_nac"],
            est_civ = session["est_civ"],
            domicilio_calle = session["domicilio_calle"],
            domicilio_numero = session["domicilio_numero"],
            domicilio_piso = request.vars["domicilio_piso"],
            parentezco =  request.vars["parentezco"],
            domicilio_depto = request.vars["domicilio_depto"],
            codigo_postal = request.vars["codigo_postal"],
            localidad = request.vars["localidad"],
            email = request.vars["email"],
            telefono = request.vars["telefono"],
            celular = request.vars["celular"],
            estudia  = request.vars["estudia"],
            

            )
        redirect(URL(c='sueldos',f='vista_previa_familiar',args =familiar_id))
    elif form.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    return locals()



def reportes_empleados():
    fecha_desde = request.vars["fecha_desde"]
    fecha_hasta = request.vars["fecha_hasta"]
    dt_str = fecha_desde
    dt_obj = datetime.strptime(dt_str, '%Y-%m-%d')
    fecha_desde = dt_obj
    dt_str2 = fecha_hasta
    dt_obj2 = datetime.strptime(dt_str2, '%Y-%m-%d')
    fecha_hasta = dt_obj2
    fecha_actual = datetime.now()
    #dt_objactual3 = datetime.strptime(fecha_actual, '%Y-%m-%d')
    #fecha_actual = dt_objactual3
    ordenar = request.vars["ordenar"]
    campos = db.legajos.num_legajo, db.legajos.nombre, db.legajos.apellido, db.legajos.fecha_ingreso, db.legajos.fe_nac
    criterio = db.legajos.fecha_ingreso >= fecha_desde
    criterio &= db.legajos.fecha_ingreso <= fecha_hasta
    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre,
    else:
        orden = db.legajos.num_legajo
        orden = db.legajos.fe_nac
    registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_empleados=registros,fecha_desde=fecha_desde,fecha_hasta=fecha_hasta,fecha_actual=fecha_actual,titulo="Listando desde fecha %s hasta fecha %s. La fecha actual es:  %s" % (fecha_desde.date(), fecha_hasta.date(), fecha_actual.date()))

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
    campos = db.horas.num_legajo,db.legajos.nombre, db.legajos.num_legajo, db.legajos.apellido, db.horas.hs_trab, db.horas.mes_trabajado
    criterio = ((db.horas.num_legajo == Legajo) & (db.horas.num_legajo == db.legajos.num_legajo) & (db.horas.mes_trabajado == mes)
               )
    #criterio = db.horas.num_legajo == Legajo
    #criterio & = db.horas.num_legajo == db.legajos.num_legajo
    #criterio &= db.horas.mes_trabajado == mes
    if ordenar:
        orden = db.legajos.apellido, db.legajos.nombre,db.horas.hs_trab, db.horas.mes_trabajado
    else:
        orden = db.legajos.num_legajo
        registros = db(criterio).select(*campos, orderby=orden)
    return dict(lista_horas=registros, mes=mes,Legajo=Legajo, titulo="Listando desde Mes %s , para el Legajo %s" % (mes, Legajo))

def reportes_horas2():
    return dict()

def reportes_familiares():
    familia_menor21 = request.vars["familia_menor21"]
    familia_estudian = request.vars["familia_estudian"]
    familiar_distdom = request.vars["familiar_distdom"]
    
    where = ""
    if familia_menor21:
        subtitulo = "Familiares menores de 21 años"
        where += " and  EXTRACT(YEAR FROM age(current_date,familiares.fe_nac)) < 21"
    if familia_estudian:
        subtitulo = "Familiares que estudian"
        where += " and familiares.estudia = 'Si' "
    if familiar_distdom:
        subtitulo = "Familiares con distinto domicilio"
        where += " and familiares.domicilio_calle <> legajos.dom_calle "
    #registros = db(criterio).select(*campos)
    registros = db.executesql("SELECT cast (EXTRACT(YEAR FROM age(current_date,familiares.fe_nac)) as integer) as edad, familiares.id as familiar_id ,familiares.num_legajo, familiares.nombre,familiares.apellido, familiares.estudia,familiares.domicilio_calle,familiares.domicilio_numero, legajos.dom_calle,legajos.dom_numero from familiares join legajos on familiares.num_legajo = legajos.num_legajo where 1=1  "+where,as_dict=True )

    return dict(lista_familiares=registros,titulo="Listando %s" % (subtitulo))

    
    
def reportes_familiares2():
    return dict()
    #return dict(lista_familiares=registros,titulo="Listando %s" % (subtitulo))

def reportes_familiares2():
    return dict()
