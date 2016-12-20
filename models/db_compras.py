# -*- coding: utf-8 -*-
db.define_table("compra",
      Field("id_compra","id"),
      Field("id_proveedor", db.proveedor),
      Field("numero_factura", 'integer',label="Número de Factura"),
      Field("tipo_factura", 'string',label="Tipo de Factura"),
      Field("fecha_factura", 'date',label="Fecha de Factura"),
      Field("forma_pago", 'string',label="Forma de Pago"),
          )
db.compra.tipo_factura.requires=IS_IN_SET(["Factua A","Factura B"])
db.compra.numero_factura.requires=IS_NOT_EMPTY(),IS_NOT_IN_DB(db,"compra.numero_factura",error_message='El número de facrura ya existe')
db.compra.fecha_factura.requires=IS_NOT_EMPTY()

db.define_table("detalle_compra",
      Field("id_producto", db.producto),
      Field("id_compra", db.compra),
      Field("id_proveedor"),
      Field("precio", 'float',label="Precio"),
      Field("cantidad", 'integer',label="Cantidad"),
                )

db.detalle_compra.id_producto.requires=IS_NOT_EMPTY()
db.detalle_compra.id_compra.requires=IS_NOT_EMPTY()
db.detalle_compra.precio.requires=IS_NOT_EMPTY()
db.detalle_compra.cantidad.requires=IS_NOT_EMPTY()
