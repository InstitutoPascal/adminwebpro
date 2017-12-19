# -*- coding: utf-8 -*-
db.define_table("legajos",
    Field("num_legajo",'integer'),
    Field("cuil",'string'),
    Field("dni",'string'),
    Field("nombre", "string"),
    Field("apellido", "string"),
    Field("fe_nac","date",default=request.date),
    Field("lu_nac","string"),
    Field("est_civ","string",requires= IS_IN_SET(["Soltero","Casado","Divorciado","Viudo"],zero='seleccione...',error_message='el campo no puede estar vacio')),
    Field("dom_calle", "string"),
    Field("dom_numero", "integer"),
    Field("piso", "integer"),
    Field("depto","string"),
    Field("codigo_postal","integer"),
    Field("localidad","string"),
    Field("email","string",requires = IS_EMAIL(error_message='¡El mail no es válido!')),
    Field("fecha_ingreso","date",default=request.now.date),
    Field("celular","string"),
    Field("telefono","string"),
    Field("estudia","string",requires= IS_IN_SET(["si","no"],zero='seleccione..',error_message='seleccione una opcion')),
    Field("horas_extras","integer"),
    Field("obra_social","string"),
    Field("categoria","string"),
    Field("fecha_egreso","date"),
    Field("constancia_de_cuil","string"),
    Field("fotocopia_dni","string"),
    Field("alta_temprana","string"),
    Field("libreta_familia","string"),
    Field("partida_nacimiento_hijos","string"),
    Field("fotocopia_dni_hijos","string"),
    Field("fotocopia_dni_conyuge","string"),
    Field("constancia_cuil_hijos","string"),
    Field("constancia_cuil_conyuge","string"),
    Field("constancia_Alumno_Regular_Hijo","string"),
    Field("constancia_Alumno_Regular_empleado","string"), 
    Field("curriculum_empleado","string"),
    Field ("image","upload",requires = IS_UPLOAD_FILENAME(extension='jpg',error_message='ingresar archivo con extension jpg')),
)

db.legajos.num_legajo.requires = IS_NOT_IN_DB(db,db.legajos.num_legajo,error_message='el legajo no puede repetirse'),
db.legajos.num_legajo.requires=IS_NOT_EMPTY(error_message='Ingrese el número de legajo'),
#db.legajos.estudia.requires= IS_IN_SET(["si","no"],zero='seleccione..',error_message='seleccione una opcion'),
db.legajos.cuil.requires=IS_NOT_IN_DB(db,db.legajos.cuil,error_message='el campo no puede estar vacio'),
db.legajos.horas_extras.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='Indique una opcion')
db.legajos.telefono.requires=IS_NOT_EMPTY(error_message= "campo obligatorio")
db.legajos.fecha_ingreso.requires=IS_NOT_EMPTY(error_message= "campo obligatorio")
db.legajos.dni.requires=[IS_INT_IN_RANGE(5000000,100000000,error_message= "ingrese un rango entre 5.000.000 y 100.000.000"),
                         #IS_NOT_EMPTY(error_message= "campo obligatorio"),
                         IS_NOT_IN_DB(db, db.legajos.dni)]
db.legajos.nombre.lenght=20
db.legajos.apellido.lenght=25
db.legajos.fecha_ingreso.requires = IS_DATE(format=T('%d-%m-%Y'),
                   error_message='Debe cumplir con el siguiente formato DIA-MES-AÑO!')
db.legajos.fecha_egreso.requires = IS_DATE(format=T('%d-%m-%Y'),
                   error_message='Debe cumplir con el siguiente formato DIA-MES-AÑO!')
db.legajos.fe_nac.requires= IS_DATE(format=T('%d-%m-%Y'),
                   error_message='Debe cumplir con el siguiente formato DIA-MES-AÑO!')
db.legajos.constancia_de_cuil.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.fotocopia_dni.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.alta_temprana.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.libreta_familia.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.partida_nacimiento_hijos.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.fotocopia_dni_conyuge.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.fotocopia_dni_hijos.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.libreta_familia.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.constancia_cuil_hijos.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.constancia_cuil_conyuge.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.constancia_Alumno_Regular_Hijo.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.constancia_Alumno_Regular_empleado.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')
db.legajos.curriculum_empleado.requires= IS_IN_SET(["corresponde","no corresponde"],zero='seleccione...',error_message='seleccione una opcion')



db.define_table("familiares",
    Field("num_legajo","integer"),
    Field("cuil","string"),
    Field("dni", "integer",),
    Field("nombre", "string"),
    Field("apellido", "string"),
    Field("fe_nac","date"),
    Field("lu_nac","string"),
    Field("est_civ","string"),
    Field("domicilio_calle","string",requires=IS_NOT_EMPTY(error_message= 'el campo no puede estar vacio')),
    Field("domicilio_numero","integer",requires=IS_NOT_EMPTY(error_message= 'el campo no puede estar vacio')),
    Field("domicilio_piso","integer"),
    Field("domicilio_depto","string"),
    Field("codigo_postal","integer"),
    Field("localidad","string"),
    Field("email","string",requires = IS_EMAIL(error_message='¡El mail no es válido!')),
    Field("telefono","string",requires=IS_NOT_EMPTY(error_message= 'ingrese un telefono de contacto')),
    Field("celular","string"),
    Field("estudia","string"),
    Field("parentezco","string"),
    )

db.familiares.estudia.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='seleccione una opcion')
db.familiares.parentezco.requires= IS_IN_SET(["Conyuge","Hijo","Familiar"],zero='seleccione...',error_message='seleccione una opcion')
db.familiares.est_civ.requires= IS_IN_SET(["Soltero","Casado","Divorciado","Viudo"],zero='seleccione...',error_message='seleccione una opcion')
db.familiares.estudia.requires= IS_IN_SET(["Si","No"],zero='seleccione...',error_message='seleccione una opcion')
db.familiares.cuil.requires=[IS_NOT_EMPTY(error_message= "campo obligatorio"),
                             IS_NOT_IN_DB(db, db.familiares.cuil,error_message='el cuil no puede repetirse ')]
                          
IS_NOT_IN_DB(db, db.familiares.cuil,error_message='el cuil no puede repetirse ')
db.familiares.dni.requires=[IS_INT_IN_RANGE(5000000,100000000,error_message= "ingrese un rango entre 5.000.000 y 100.000.000"),
                         IS_NOT_EMPTY(error_message= "campo obligatorio"),
                         IS_NOT_IN_DB(db, db.familiares.dni,error_message='el dni no puede repetirse')]
db.familiares.nombre.lenght=20
db.familiares.apellido.lenght=25
db.familiares.fe_nac.requires = IS_DATE(format=T('%d-%m-%Y'),
                  error_message='Debe cumplir el siguiente formato Y-M-D!')
db.familiares.num_legajo.requires=IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s",zero='seleccione...',error_message='seleccione una opcion')

db.define_table("horas",
      Field("num_legajo","string"),
    Field("mes_trabajado",requires=IS_IN_SET(['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'],zero='seleccione...',error_message='seleccione una opcion')),
    Field("semana","integer"),
    Field("hs_trab","float"),
    Field("hs_ext","float"),
               )
db.horas.num_legajo.requires= IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s",zero='seleccione...',error_message='seleccione una opcion')
#db.horas.mes_trabajado.
db.horas.semana.requires = IS_IN_SET(["1","2","3","4","5"],zero='seleccione...',error_message='seleccione una opcion')
db.horas.hs_trab.requires= IS_NOT_EMPTY(error_message='el campo no puede estar vacio')
db.horas.hs_ext.requires= IS_NOT_EMPTY(error_message='el campo no puede estar vacio')
