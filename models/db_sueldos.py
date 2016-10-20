# -*- coding: utf-8 -*-
db.define_table("legajos",
    Field("num_legajo","integer"),
    Field("cuil","string",unique=True,requires=[IS_EMPTY_OR (IS_CUIT()),IS_EMPTY_OR (IS_NOT_IN_DB(db,"legajos.cuil",error_message="El CUIL del empleado ya existe")),IS_NOT_EMPTY(error_message="Ingrese el CUIL del empleado")],label="CUIL"),
    Field("dni","string",),
    Field("nombre", "string"),
    Field("apellido", "string"),
    Field("fe_nac","date"),
    Field("lu_nac","string"),
    Field("est_civ","string"),
    Field("edad","integer"),
    Field("dom_calle", "string"),
    Field("dom_numero", "integer"),
    Field("piso", "integer"),
    Field("depto","string"),
    Field("codigo_postal","integer"),
    Field("localidad","string"),
    Field("email","string"),
    Field("fecha_ingreso","date"),
    Field("celular","string"),
    Field("telefono","string"),
    Field("estudia","string"),
    Field("horas_extras","integer"),
    Field("obra_social","string"),
    Field("categoria","string"),
    Field("fecha_egreso","date"),
)

db.legajos.num_legajo.requires = [IS_NOT_IN_DB(db,"legajos.num_legajo"),
                                 IS_NOT_EMPTY(error_message= "campo obligatorio")]
db.legajos.est_civ.requires= IS_IN_SET(["Soltero","Casado","Divorciado","Viudo"])
db.legajos.estudia.requires= IS_IN_SET(["si","no"])
db.legajos.cuil.requires=[IS_NOT_IN_DB(db, "legajos.cuil"),
                          IS_NOT_EMPTY(error_message= "campo obligatorio")]
db.legajos.horas_extras.requires= IS_IN_SET(["Si","No"])
db.legajos.telefono.requires=IS_NOT_EMPTY(error_message= "campo obligatorio")
db.legajos.fecha_ingreso.requires=IS_NOT_EMPTY(error_message= "campo obligatorio")
db.legajos.dni.requires=[IS_INT_IN_RANGE(5000000,100000000),
                         IS_NOT_EMPTY(error_message= "campo obligatorio"),
                         IS_NOT_IN_DB(db, "legajos.dni")]
db.legajos.nombre.lenght=20
db.legajos.apellido.lenght=25
db.legajos.fecha_ingreso.requires = IS_DATE(format=T('%Y-%m-%d'),
                   error_message='Debe cumplir con el siguiente formato YYYY-MM-DD!')
#db.legajos.fecha_ingreso.requires=IS_DATE('%Y-%M-%D')
db.legajos.fe_nac.requires = IS_DATE(format=T('%Y-%m-%d'),
                  error_message='Debe cumplir con el siguiente formato YYYY-MM-DD!')

#db.legajos.fe_nac.requires=IS_DATE('%Y-%M-%D')

db.define_table("familiares",
    Field("num_legajo","integer"),
    Field("cuil","string"),
    Field("dni", "integer",),
    Field("nombre", "string"),
    Field("apellido", "string"),
    Field("fe_nac","date"),
    Field("lu_nac","string"),
    Field("est_civ","string"),
    Field("edad","integer"),
    Field("domicilio_calle","string"),
    Field("domicilio_numero","integer"),
    Field("domicilio_piso","integer"),
    Field("domicilio_depto","string"),
    Field("codigo_postal","integer"),
    Field("localidad","string"),
    Field("email","string"),
    Field("telefono","integer"),
    Field("celular","integer"),
    Field("estudia","string"),
    Field("parentezco","string"),
    )

db.familiares.estudia.requires= IS_IN_SET(["Si","No"])
db.familiares.parentezco.requires= IS_IN_SET(["Conyuge","Hijo","Familiar"])
db.familiares.est_civ.requires= IS_IN_SET(["Soltero","Casado","Divorciado","Viudo"])
db.familiares.estudia.requires= IS_IN_SET(["Si","No"])
db.familiares.cuil.requires=[IS_NOT_IN_DB(db,"legajos.cuil"),
                          IS_NOT_EMPTY(error_message= "campo obligatorio")]
db.familiares.dni.requires=[IS_INT_IN_RANGE(5000000,100000000),
                         IS_NOT_EMPTY(error_message= "campo obligatorio"),
                         IS_NOT_IN_DB(db, "legajos.dni")]
db.familiares.nombre.lenght=20
db.familiares.apellido.lenght=25
db.legajos.fe_nac.requires = IS_DATE(format=T('%Y-%m-%d'),
                  error_message='Debe cumplir con el siguiente formato YYYY-MM-DD!')
db.familiares.num_legajo.requires= IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s")

db.define_table("horas",
    Field("num_legajo","integer"),
    Field("mes_trabajado","string"),
    Field("semana","integer"),
    Field("hs_trab","float"),
    Field("hs_ext","float"),
               )
db.horas.num_legajo.requires= IS_IN_DB(db,db.legajos.num_legajo,"%(num_legajo)s")
db.horas.mes_trabajado.requires = IS_IN_SET(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])
db.horas.semana.requires = IS_IN_SET(["1","2","3","4","5"])
