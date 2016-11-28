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
    Field("condicion_frente_al_iva",label="Condición frente al IVA"),
    Field("nombre_de_fantasia",label="Nombre de Fantasía"),
    Field("razon_social",label="Razón Social"),
    Field("cuit",label="C.U.I.T"),
    Field("dni",label="D.N.I."),
    Field("tipo_factura",label="Tipo de Factura"),
    Field("direccion",label="Dirección"),
    Field("numero",label="Número"),
    Field("localidad","string"),
    Field("telefono",label="Teléfono"),
    Field("email",label="E-Mail"),
    format='%(nombre_de_fantasia)s %(razon_social)s ( %(id_cliente)s )',
)
#################Validaciones de Cliente##################

db.cliente.condicion_frente_al_iva.requires=IS_IN_SET(["Responsable Inscripto","Consumidor Final"],error_message='Seleccione una opción' )
db.cliente.tipo_factura.requires=IS_IN_SET(["A","B"],error_message='Seleccione una opción' )
db.cliente.cuit.requires=[IS_NOT_EMPTY(error_message='Complete el campo'),
			IS_NOT_IN_DB(db,"cliente.cuit",error_message='CUIT ya existe')]
db.cliente.dni.requires=[IS_NOT_EMPTY(error_message='Complete el campo'),
			IS_NOT_IN_DB(db,"cliente.dni",error_message='DNI ya existe')]
db.cliente.telefono.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.cliente.direccion.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.cliente.numero.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.cliente.localidad.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.cliente.razon_social.requires=IS_NOT_EMPTY(error_message='Complete el campo')


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
db.proveedor.condicion_iva.requires=IS_IN_SET(["Responsable Inscripto","Monotributista"],error_message='Seleccione una opción' )
db.proveedor.cuit.requires=[IS_NOT_EMPTY(error_message='Complete el campo'),
			IS_NOT_IN_DB(db,"proveedor.cuit",error_message='CUIT ya existe')]
db.proveedor.ingreso_bruto.requires=[IS_NOT_EMPTY(error_message='Complete el campo'),
						IS_NOT_IN_DB(db,"proveedor.ingreso_bruto",error_message='Ingresos Brutos ya existe')]
db.proveedor.razon_social.requires=[IS_NOT_EMPTY(error_message='Complete el campo'),
				    IS_NOT_IN_DB(db,"proveedor.razon_social",error_message='Razón Social ya existe')]
db.proveedor.domicilio.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.localidad.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.codigo_postal.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.provincia.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.pais.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.telefono.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.celular.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.email_proveedor.requires=IS_NOT_EMPTY(error_message='Complete el campo')
db.proveedor.pagina_web.requires=IS_NOT_EMPTY(error_message='Complete el campo')


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
db.producto.precio_venta.requires=IS_NOT_COMA(error_message="No ingresar con coma")
db.producto.precio_compra.requires=IS_NOT_COMA(error_message="No ingresar con coma")
