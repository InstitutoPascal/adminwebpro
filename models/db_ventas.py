# -*- coding: utf-8 -*-
##############ventas####################
db.define_table("ventas",
    Field("buscar_cliente","string"),
    Field("tipo_de_factura","string"),
    Field("fecha","date"),
    Field("tipo_de_pago","string"),
    Field("tipo_de_producto","string"),
    Field("detalle","string"),
    Field("cantidad","integer"),
    Field("precio_unitario","double"),
    Field("iva","double"),
    Field("descuento","double"),
    )
db.ventas.buscar_cliente.requires = IS_IN_DB(db, "cliente.id_cliente", " %(nombre_de_fantasia)s %(razon_social)s ..")
db.ventas.tipo_de_factura.requires=IS_IN_SET(["Factura A","Factura B"])
db.ventas.tipo_de_pago.requires = IS_IN_SET(["Efectivo","Credito"])
db.ventas.tipo_de_producto.requires = IS_IN_SET(["Hardware","Software"])
db.ventas.detalle.requires=IS_IN_DB(db, "producto.id_producto", " %(detalle_producto)s")
db.ventas.iva.requires = IS_IN_SET(["10.5%","21%","27%"])
db.ventas.descuento.requires = IS_IN_SET(["10%","15%","25%","40%"])
