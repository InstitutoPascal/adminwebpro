# -*- coding: utf-8 -*-

#2.14.6-stable+timestamp.2016.05.10.00.21.47
#(Ejecutando en Rocket 1.2.6, Python 2.7.3)
"""
buscar actualizaciones

Pruebe la interfaz móvil

Nueva aplicación

Nombre de la aplicación:

Crear
Suba e instale una aplicación empaquetada
# Archivo para definir las tablas comunes para todos
"""
db.define_table("cliente",
    Field("id_cliente","id"),
    Field("condicion_frente_al_iva","string"),
    Field("nombre_de_fantasia","string"),
    Field("razon_social","string"),
    Field("cuit","string"),
    Field("dni","string"),
    Field("tipo_factura","string"),
    Field("direccion","string"),
    Field("numero","string"),
    Field("localidad","string"),
    Field("telefono","string"),
    Field("email","string"),
    format='%(nombre_de_fantasia)s %(razon_social)s ( %(id_cliente)s )',
)
#################Validaciones de Cliente##################

db.cliente.condicion_frente_al_iva.requires=IS_IN_SET(["Responsable Inscripto","Consumidor Final"])
db.cliente.cuit.requires=IS_NOT_IN_DB(db, "cliente.cuit")
db.cliente.dni.requires=IS_NOT_IN_DB(db, "cliente.dni")
#db.cliente.condicion_frente_al_iva.requires=IS_NOT_EMPTY(error_message='Selecione un campo')
db.cliente.telefono.requires=IS_NOT_EMPTY(error_message='Ingresar el numero Telefonico')
db.cliente.direccion.requires=IS_NOT_EMPTY(error_message='Ingresar la Direccion')
db.cliente.numero.requires=IS_NOT_EMPTY(error_message='Ingresar el Numero')
db.cliente.localidad.requires=IS_NOT_EMPTY(error_message='Ingresar Lalocalidad')


db.define_table("proveedor",
      Field("id_proveedor", "id"),
      Field("razon_social", 'string'),
      Field("ingreso_bruto", 'string'),
      Field("condicion_iva", 'string'),
      Field("cuit", 'string'),
      Field("domicilio", 'string'),
      Field("localidad", 'string'),
      Field("codigo_postal", 'integer'),
      Field("provincia", 'string'),
      Field("pais", 'string'),
      Field("telefono", 'string'),
      Field("celular", 'string'),
      Field("email_proveedor", 'string'),
      Field("pagina_web", 'string'),
      format='%(razon_social)s %(id_proveedor)s )',
    )
db.proveedor.condicion_iva.requires=IS_IN_SET(["Responsable Inscripto","Monotributista"])
db.proveedor.cuit.requires=IS_NOT_EMPTY(),
db.proveedor.ingreso_bruto.requires=IS_NOT_EMPTY()
db.proveedor.razon_social.requires=IS_NOT_EMPTY()
db.proveedor.domicilio.requires=IS_NOT_EMPTY()
db.proveedor.localidad.requires=IS_NOT_EMPTY()
db.proveedor.codigo_postal.requires=IS_NOT_EMPTY()
db.proveedor.provincia.requires=IS_NOT_EMPTY()


db.define_table("producto",
    Field("id_producto","id"),
    Field("detalle_producto","string"),
    Field("precio_compra","float"),
    Field("precio_venta","float"),
    Field("alicuota_iva","float"),
    Field("marca","string"),
    Field("categoria","string"),
)

db.producto.categoria.requires=IS_IN_SET(["Hardware","Software"])
db.producto.alicuota_iva.requires=IS_IN_SET({10.5: "10.5%",21: "21%"})
db.producto.id_producto.requires=IS_NOT_EMPTY()
db.producto.id_producto.requires=IS_NOT_IN_DB(db,"producto.id_producto")
db.producto.detalle_producto.requires=IS_NOT_EMPTY()
db.producto.precio_venta.requires=IS_NOT_EMPTY()
