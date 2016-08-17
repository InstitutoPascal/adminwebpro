# -*- coding: utf-8 -*-
##############ventas####################

from datetime import datetime 

db.define_table("ventas",
    Field("buscar_cliente",db.cliente),
    Field("tipo_de_factura","string"),
    Field("punto_de_venta","integer"),
    Field("numero_factura","integer"),
    Field("fecha","date"),
    Field("tipo_de_pago","string"),
    #format='%(punto_de_venta)s',
    format='%(numero_factura)s %(tipo_de_factura)s',
)

db.ventas.buscar_cliente.requires = IS_IN_DB(db, "cliente.id_cliente"," %(nombre_de_fantasia)s-%(razon_social)s .")
db.ventas.tipo_de_factura.requires=IS_IN_SET(["Factura A","Factura B"])
db.ventas.punto_de_venta.requires=IS_IN_SET({1:"0001"})
db.ventas.numero_factura.requires=IS_INT_IN_RANGE("0","10000000")
db.ventas.tipo_de_pago.requires = IS_IN_SET(["Efectivo","Credito"])

###########################DETALLE VENTAS#######################

db.define_table("detalle_ventas",
    Field("numero_de_factura","integer"),
    Field("detalle","string"),
    Field("cantidad","integer"),
    Field("precio_unitario","double"),
    Field("iva","double"),
    Field("descuento","double"),
    
    )

#db.detalle_ventas.requieres=IS_IN_DB(db, "ventas.numero_factura"," %(numero_factura)s-%(tipo_de_factura)s")
db.detalle_ventas.detalle.requires=IS_IN_DB(db,"producto.detalle_producto", " %(detalle_producto)s")
db.detalle_ventas.iva.requires = IS_IN_SET({10.5:"10.5%",21:"21%",27:"27%"})
db.detalle_ventas.descuento.requires = IS_IN_SET({0:"0%",10:"10%",15:"15%",25:"25%",40:"40%"})
db.detalle_ventas.precio_unitario.requires =IS_IN_DB(db,"producto.precio_venta","%(precio_venta)s")
db.detalle_ventas.numero_de_factura.requires =IS_IN_DB(db,"ventas.numero_factura","%(numero_factura)s-%(tipo_de_factura)s")

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

