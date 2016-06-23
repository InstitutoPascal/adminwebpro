# -*- coding: utf-8 -*-

# Archivo para definir las tablas comunes para todos

db.define_table("cliente",
    Field("id_cliente","id"),
    Field("nombre_de_fantasia","string"),
    Field("razon_social","string"),
    Field("cuit","integer"),
    Field("dni","integer"),
    Field("condicion_frente_al_iva","string"),
    Field("direccion","string"),
    Field("numero","integer"),
    Field("localidad","string"),
    Field("telefono","integer"),
    Field("email","string"),
)
db.cliente.condicion_frente_al_iva.requires=IS_IN_SET(["Responsable Inscripto","Monotributista","Consumidor Final"])
db.cliente.cuit.requires=IS_NOT_IN_DB(db, "cliente.cuit")
db.cliente.dni.requires=IS_NOT_IN_DB(db, "cliente.dni")
db.cliente.telefono.requires=IS_NOT_EMPTY()
db.cliente.direccion.requires=IS_NOT_EMPTY()
db.cliente.numero.requires=IS_NOT_EMPTY()
db.cliente.localidad.requires=IS_NOT_EMPTY()


db.define_table("proveedor",
      Field("id"),
      Field("razon_social", 'string'),
      Field("cuit", 'integer'),
    )

db.define_table("producto",
    )
