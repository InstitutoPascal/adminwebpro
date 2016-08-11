# -*- coding: utf-8 -*-
db.define_table("compra",
      Field("id"),
      Field("numero_factura", 'integer'),
      Field("cuit", 'integer'),
      Field("tipo_factura", 'string'),
      Field("fecha_factura", 'date'),
      Field("razon_social", 'string'),
      Field("tipo_iva", 'float'),
      Field("ingresos_brutos", 'integer'),
      Field("domicilio", 'string'),
      Field("localidad", 'string'),
      Field("codigo_postal", 'integer'),
      Field("provincia", 'string'),
      Field("telefono", 'integer'),
    )
db.compra.tipo_factura.requires=IS_IN_SET(["Factua A","Factura B"])
db.compra.tipo_iva.requires=IS_IN_SET({27:"Servicios 27%", 21:"Tasa General 21%", 10.5:"Tasa Reducida 10,5%"})
db.compra.numero_factura.requires=IS_NOT_EMPTY()
db.compra.cuit.requires=IS_NOT_EMPTY()
db.compra.fecha_factura.requires=IS_NOT_EMPTY()
db.compra.razon_social.requires=IS_NOT_EMPTY()
db.compra.ingresos_brutos.requires=IS_NOT_EMPTY()
db.compra.domicilio.requires=IS_NOT_EMPTY()
db.compra.localidad.requires=IS_NOT_EMPTY()
db.compra.codigo_postal.requires=IS_NOT_EMPTY()
db.compra.provincia.requires=IS_NOT_EMPTY()
db.compra.telefono.requires=IS_NOT_EMPTY()

db.define_table("detalle_compra",
      Field("id_producto", db.producto),
      Field("id_compra", db.compra),
      Field("id",db.proveedor),
      Field("precio", 'float'),
      Field("cantidad", 'integer'),
                )
