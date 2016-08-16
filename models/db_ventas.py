# -*- coding: utf-8 -*-
##############ventas####################
from datetime import datetime 
db.define_table("ventas",
    Field("buscar_cliente",db.cliente),
    Field("tipo_de_factura","string"),
    Field("numero_serie","double"),
    Field("numero_factura","double"),
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
db.ventas.numero_serie.requires=IS_IN_SET(["0001","0002","0003","0004"])
db.ventas.numero_factura.requires=IS_INT_IN_RANGE("0","9999")
db.ventas.tipo_de_pago.requires = IS_IN_SET(["Efectivo","Credito"])
db.ventas.tipo_de_producto.requires = IS_IN_SET(["Hardware","Software"])
db.ventas.detalle.requires=IS_IN_DB(db, "producto.id_producto", " %(detalle_producto)s")
db.ventas.iva.requires = IS_IN_SET({10.5:"10.5%",21:"21%",27:"27%"})
db.ventas.descuento.requires = IS_IN_SET(["0%","10%","15%","25%","40%"])
db.ventas.precio_unitario.requires =IS_IN_DB(db,"producto.precio_venta","%(precio_venta)s")

db.define_table("cobros",
                Field("venta_id",db.ventas),
                Field('formas_pago',db.formas_pago),
                Field('fecha_creacion','datetime',default=datetime.now()),
                Field('importe','double',requires=IS_NOT_EMPTY(error_message='El importe no puede estar vacio'))
                )
db.cobros.formas_pago.requires = IS_IN_DB(db, "formas_pago.id", " %(descripcion)s",zero='Seleccionar...')
db.cobros.venta_id.readable = False
db.cobros.venta_id.writable = False
