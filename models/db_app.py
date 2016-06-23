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

db.define_table("proveedor",
      Field("id"),
      Field("razon_social", 'string'),
      Field("cuit", 'integer'),
    )

db.define_table("producto",
    )
