# -*- coding: utf-8 -*-
##############ventas####################
db.define_table("ventas",
    Field("buscar_cliente","string"),
    Field("tipo_de_factura","string"),
    Field("fecha","date"),
    Field("tipo_de_pago","string"),
    Field("producto_o_servicio","string"),
    Field("cantidad","integer"),
    Field("precio_unitario","double"),
    Field("iva","double"),
    Field("descuento","double"),
    )
db.ventas.buscar_cliente.requires = IS_IN_DB(db, "cliente.id_cliente", "-- %(nombre_de_fantasia)s %(razon_social)s ..")
