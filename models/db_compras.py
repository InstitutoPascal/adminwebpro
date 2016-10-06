# -*- coding: utf-8 -*-
db.define_table("compra",
      Field("id_compra"),
      Field("numero_factura", 'integer'),
      Field("tipo_factura", 'string'),
      Field("fecha_factura", 'date'),
      Field("tipo_iva", 'float'),
          )
db.compra.tipo_factura.requires=IS_IN_SET(["Factua A","Factura B"])
db.compra.tipo_iva.requires=IS_IN_SET({27:"Servicios 27%", 21:"Tasa General 21%", 10.5:"Tasa Reducida 10,5%"})
db.compra.numero_factura.requires=IS_NOT_EMPTY()
db.compra.fecha_factura.requires=IS_NOT_EMPTY()

db.define_table("detalle_compra",
      Field("id_producto"),
      Field("id_compra"),
      Field("id_proveedor"),
      Field("precio", 'float'),
      Field("cantidad", 'integer'),
                )

db.detalle_compra.id_producto.requires=IS_NOT_EMPTY()
db.detalle_compra.id_compra.requires=IS_NOT_EMPTY()
db.detalle_compra.id_proveedor.requires=IS_NOT_EMPTY()
db.detalle_compra.precio.requires=IS_NOT_EMPTY()
db.detalle_compra.cantidad.requires=IS_NOT_EMPTY()
