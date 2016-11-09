# -*- coding: utf-8 -*-

db.define_table("deposito",
    Field("numero_deposito",'integer'),
    Field("ubicacion" ,"string"),
    Field("disponibilidad","string"),
    Field("tipo" , "string"),
    )
db.deposito.numero_deposito.requires = IS_NOT_IN_DB(db, "deposito.numero_deposito")

db.define_table("remito_entrada",
    Field("numero_remito_e","integer"),
    Field("fecha","date"),
    Field("id_proveedor",db.proveedor ),
    Field("id_producto",db.producto ),
    Field("cantidad","integer" ),
    )
db.remito_entrada.numero_remito_e.requires = IS_NOT_IN_DB(db, "remito_entrada.numero_remito_e")
db.remito_entrada.id_proveedor.requires = IS_IN_DB(db, "proveedor.razon_social","%(razon_social)s")
db.remito_entrada.id_producto.requires = IS_IN_DB(db, "producto.id_producto","%(detalle_producto)s")

db.define_table("remito_salida",
    Field("numero_remito_s","integer"),
    Field("fecha","date"),
    Field("cliente",db.cliente ),
    Field("producto",db.producto ),
    Field("cantidad","integer" ),
    )
db.remito_salida.numero_remito_s.requires = IS_NOT_IN_DB(db, "remito_entrada.numero_remito_s")
db.remito_salida.cliente.requires = IS_IN_DB(db, "cliente.nombre_de_fantasia","%(nombre_de_fantasia)s")
db.remito_salida.producto.requires = IS_IN_DB(db, "producto.id_producto","%(detalle_producto)s")

db.define_table("stock",
                Field("id_producto",db.producto,requires=IS_NOT_EMPTY("No hay producto")),
                Field("cantidad", "integer")
               )
