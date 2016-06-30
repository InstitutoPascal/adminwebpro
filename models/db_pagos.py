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
    Field("tipo","string"),
    Field("moneda","string"),
    Field("cbu","string"),
)

db.define_table("cheque",
    Field("id_cheques","id"),
    Field("num_cheque","integer"),
    Field("emision","date"),
    Field("vencimiento","date"),
    Field("importe","integer"),
)
db.pagos.num_orden_pago.requires=IS_NOT_IN_DB(db, "pagos.num_orden_pago")
db.pagos.fecha.requires=IS_DATE('%Y-%m-%d')
db.cheques.num_cheques.requires=IS_NOT_IN_DB(db, "cheques.num_cheques")
db.cheques.emision.requires=IS_DATE('%Y-%m-%d')
db.cheques.vencimiento.requires=IS_DATE('%Y-%m-%d')
