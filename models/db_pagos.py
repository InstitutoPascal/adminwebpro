# -*- coding: utf-8 -*-
db.define_table("banco",
    Field("id_banco","id"),
    Field("sucursal","string"),
    Field("nombre_banco","string"),
    Field("telefono","string"),
)
db.define_table("cuenta_bancaria",
    Field("id_cuenta_bancaria","id"),
    Field("numero_cuenta","string"),
    Field("tipo_de_cuenta", "string"),
    Field("tipo_de_moneda","string"),
    Field("cbu","string"),
    Field("id_banco",db.banco),
)

db.define_table("pago",
    Field("id_pagos","id"),
    Field("num_orden_pago","string"),
    Field("fecha","date"),
    Field("importe","string"),
    Field("id_compras",db.compra, label="Numero Factura de Compra"),
    Field("id_proveedor", db.proveedor, label="Nombre de Proveedor"),
)

db.define_table("cheque",
    Field("id_cheques","id"),
    Field("num_cheque","integer"),
    Field("emision","date"),
    Field("vencimiento","date"),
    Field("importe","integer"),
    Field("id_cuenta_bancaria",db.cuenta_bancaria),
    Field("id_pagos", db.pago)
)

db.define_table("pagado",
    Field("id_pagado", "id"),
    Field("factura_pagada", "boolean"),
    Field("id_pagos", db.pago),
    Field("id_compras", db.compra)
)

db.pago.num_orden_pago.requires=IS_NOT_IN_DB(db, "pago.num_orden_pago")
db.pago.fecha.requires=IS_DATE('%Y-%m-%d')
db.banco.nombre_banco.requires = IS_NOT_EMPTY()
db.banco.nombre_banco.requires = IS_NOT_IN_DB(db, "banco.nombre_banco")
db.cuenta_bancaria.id_banco.requires = IS_IN_DB(db, "banco.id_banco", "-- %(nombre_banco)s ..")
db.pago.id_proveedor.requires = IS_IN_DB(db, "proveedor.id", "-- %(razon_social)s ..")
db.cheque.id_cuenta_bancaria.requires = IS_IN_DB(db, "cuenta_bancaria.id_cuenta_bancaria", "-- %(numero_cuenta)s ..")
db.cheque.num_cheque.requires=IS_NOT_IN_DB(db, "cheque.num_cheque")
db.cheque.emision.requires=IS_DATE('%Y-%m-%d')
db.cheque.vencimiento.requires=IS_DATE('%Y-%m-%d')
db.pago.id_compras.requires = IS_IN_DB(db, "compra.id_compra", "-- %(numero_factura)s ..")
