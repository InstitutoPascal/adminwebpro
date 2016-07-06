# -*- coding: utf-8 -*-
db.define_table("pago",
    Field("id_pagos","id"),
    Field("num_orden_pago","integer"),
    Field("fecha","date"),
    Field("importe","integer"),
)
db.define_table("banco",
    Field("id_banco","id"),
    Field("nombre_banco","string"),
    Field("telefono","integer"),
)

db.define_table("cheque",
    Field("id_cheques","id"),
    Field("num_cheque","integer"),
    Field("emision","date"),
    Field("vencimiento","date"),
    Field("importe","integer"),
    Field("id_banco",db.banco)
)
db.pago.num_orden_pago.requires=IS_NOT_IN_DB(db, "pago.num_orden_pago")
db.pago.fecha.requires=IS_DATE('%Y-%m-%d')
db.banco.nombre_banco.requires = IS_NOT_EMPTY()
db.cheque.id_banco.requires = IS_IN_DB(db, "banco.id_banco", "-- %(nombre_banco)s ..")
db.cheque.num_cheque.requires=IS_NOT_IN_DB(db, "cheque.num_cheque")
db.cheque.emision.requires=IS_DATE('%Y-%m-%d')
db.cheque.vencimiento.requires=IS_DATE('%Y-%m-%d')
