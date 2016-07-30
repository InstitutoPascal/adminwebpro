# -*- coding: utf-8 -*-

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=myconf.get('db.migrate'),
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.get('smtp.server')
mail.settings.sender = myconf.get('smtp.sender')
mail.settings.login = myconf.get('smtp.login')
mail.settings.tls = myconf.get('smtp.tls') or False
mail.settings.ssl = myconf.get('smtp.ssl') or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)

# Tabla "Clientes"
db.define_table('Clientes', 
                Field('ClienteId',length=25),
                Field('RazonSocial',length=50,default='',label=T('Razon Social')),
                Field('CUIT',length=13,default='9-99999999-99',label=T('CUIT')),
                Field('Direccion',length=25,default='',label=T('Direccion')),
                Field('PosIVAId',label=T('Posicion IVA')),
               )
# Validadores "Clientes"
db.Clientes.ClienteId.requires=IS_NOT_IN_DB(db, 'Clientes.ClienteId')
db.Clientes.CUIT.requires=IS_NOT_IN_DB(db, 'Clientes.CUIT')
db.Clientes.ClienteId.requires=IS_NOT_EMPTY(error_message='Falta ingresar el Cod. de Cliente')
db.Clientes.CUIT.requires=IS_NOT_EMPTY(error_message='Falta ingresar el CUIT')
db.Clientes.RazonSocial.requires=IS_NOT_EMPTY(error_message='Falta ingresar la Razon Social')
db.Clientes.PosIVAId.requires=IS_IN_SET(('Responsable Inscripto','Monotributo','Exento','Consumidor Final','Responsable No Inscripto'))

# Tabla "DocumentosCabecera"
db.define_table('DocumentosCabecera', 
                Field('DocumentosId'),
                Field('Sucursal',length=4,default='0001',label=T('Sucursal')),
                Field('Numero',length=8,default='00000001',label=T('Numero')),
                Field('TipoDocumento',length=3,default='REC',label=T('Tipo de Documento')),
                Field('ClienteId',length=15,default='',label=T('Cliente')),
                Field('SubTotal',default='0.00',label=T('SubTotal')),
                Field('Total',default='0.00', label=T('Nombre')),
                Field('Fecha',default='01/01/2016',label=T('Fecha')),
                Field('PosIVAId',label=T('Posicion IVA')),
               )
# Validadores "DocumentosCabecera"
db.DocumentosCabecera.DocumentosId.requires=IS_NOT_IN_DB(db, 'DocumentosCabecera.DocumentosId')
db.DocumentosCabecera.ClienteId.requires=IS_IN_DB(db, 'Clientes.ClienteId')
db.DocumentosCabecera.ClienteId.requires=IS_NOT_EMPTY(error_message='Falta ingresar el Cod. de Cliente')
db.DocumentosCabecera.TipoDocumento.requires=IS_IN_SET(('FCA','FCB','REC','OPA','PAG')) # FCA=Factura A, FCB=Factura B, REC=Recibo, OPA=Orden de Pago, PAG=Pago Contrafactura
db.DocumentosCabecera.Fecha.requires=IS_NOT_EMPTY(error_message='Falta ingresar la Fecha')
db.DocumentosCabecera.PosIVAId.requires=IS_IN_SET(('Responsable Inscripto','Monotributo','Exento','Consumidor Final','Responsable No Inscripto'))

# Tabla "DocumentosDetalle"
db.define_table('DocumentosDetalle', 
                Field('DocumentosDetalleId'),
                Field('DocumentosId'),
                Field('ProductoId',length=25,label=T('Cod. Producto')),
                Field('Descripcion',label=T('Descripcion')),
                Field('Cantidad',default='1',label=T('Cantidad')),
                Field('Unitario',label=T('Precio Unitario')),
                Field('Descuento',label=T('Descuento')),
                Field('AlicuotaIVA',default='21',label=T('Alicuota IVA')),
               )
# Validadores "DocumentosDetalle"
db.DocumentosDetalle.DocumentosDetalleId.requires=IS_NOT_IN_DB(db, 'DocumentosDetalle.DocumentosDetalleId')
db.DocumentosDetalle.DocumentosId.requires=IS_IN_DB(db, 'DocumentosCabecera.DocumentosId')
db.DocumentosDetalle.ProductoId.requires=IS_NOT_EMPTY(error_message='Falta ingresar el Cod. de Producto')
db.DocumentosDetalle.Descripcion.requires=IS_NOT_EMPTY(error_message='Falta ingresar la Descripcion del Producto')
db.DocumentosDetalle.Cantidad.requires=IS_NOT_EMPTY(error_message='Falta ingresar la Cantidad del Producto')
db.DocumentosDetalle.Unitario.requires=IS_NOT_EMPTY(error_message='Falta ingresar el Precio Unitario')
db.DocumentosDetalle.AlicuotaIVA.requires=IS_NOT_EMPTY(error_message='Falta ingresar la Alicuota IVA')
