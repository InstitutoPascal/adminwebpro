# -*- coding: utf-8 -*-

# Archivo para definir las tablas comunes para todos

db.define_table("cliente",
    )

db.define_table("proveedor",
      Field("id"),
      Field("razon_social", 'string'),
      Field("cuit", 'integer'),
    )

db.define_table("producto",
    )
