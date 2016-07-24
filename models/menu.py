# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('web', SPAN(2), 'py'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="http://www.web2py.com/",
                  _id="web2py-logo")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
#Agregando mi menu
response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Prueba'), False, URL('prueba', 'index'), [
        (T('ABM ejemplo'), False, URL('prueba', 'abm_ejemplo'), []),
        (T('Reporte'), False, URL('prueba', 'reporte_ejemplo'), []),
        (T('Registrar'), False, URL('prueba', 'registrar_comprobante'), []),
        ]),
    (T('Pagos'), False, URL('pagos', 'index'), [
        (T('Autorizar Pago'), False, URL('pagos', 'autorizar_pagos'), []),
        (T('Cheques'), False, URL('pagos', 'abm_cheques'), []),
        (T('Generar Orden de Pago'), False, URL('pagos', 'generar_orden_pagos'), []),
        (T('Reporte Pagos'), False, URL('pagos', 'reporte_pagos'), []),
        ]),
    (T('Cobranzas'), False, '#', [
        (T('Autorizar Cobro'), False, URL('ordencobro', 'autorizar_cobro'), []),
        (T('Cheques'), False, URL('ordencobro', 'abm_cheques'), []),
        (T('Generar Orden de Cobros'), False, URL('ordencobro', 'generar_orden_cobro'), []),
        (T('Reporte Cobros'), False, URL('ordencobro', 'reporte_cobros'), []),
        ]),	
    (T('Ventas'), False, URL('ventas', 'index'), [
        (T('A.B.M. Cliente'), False, URL('ventas', 'abm_clientes'), []),
        (T('Facturar'), False, URL('ventas', 'abm_ventas'), []),
        (T('Consulta de Factura'), False, URL('ventas', 'comprobantes'), []),
        (T('Clientes'), False, URL('ventas', 'abm_clientes'), []),
        (T('Ventas'), False, URL('ventas', 'abm_ventas'), []),
        (T('Comprovantes'), False, URL('ventas', 'comprobantes'), []),
        ]),
     (T('Stock'), False, URL('stock', 'index'), [
        (T('Productos'), False, URL('stock', 'abm_producto'), []),
        (T('Inventario'), False, URL('stock', 'stock'), []),
        (T('Depositos'), False, URL('stock', 'abm_deposito'), []),
        (T('Remito salida'), False, URL('stock', 'remito_salida'), []),
        (T('Remito entrada'), False, URL('stock', 'remito_entrada'), []),
        ]),
    (T('Compra'), False, URL('compra', 'index'), [
        (T('Proveedor'), False, URL('compra', 'index'), [
            ]),
            (T('Alta Proveedor'), False, URL('compra', 'alta_proveedor'), []),
            (T('Baja  Proveedor'), False, URL('compra', 'baja_proveedor'), []),
            (T('Modificación Proveedor'), False, URL('compra', 'modificacion_proveedor'), []),
            ]),      
     (T('Sueldos'), False, URL('sueldos', 'index'), [
         (T('ABM Empleados'), False, URL('sueldos', 'abm_empleados'), []),
         (T('ABM Familiares'), False, URL('sueldos', 'abm_familiares'), []),
         (T('ABM Horas'), False, URL('sueldos', 'abm_horas'), []),
         (T('Reportes'), False, URL('sueldos', 'reportes'), []),
         ]),
]

DEVELOPMENT_MENU = False


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('My Sites'), False, URL('admin', 'default', 'site')),
        (T('This App'), False, '#', [
            (T('Design'), False, URL('admin', 'default', 'design/%s' % app)),
            LI(_class="divider"),
            (T('Controller'), False,
             URL(
                 'admin', 'default', 'edit/%s/controllers/%s.py' % (app, ctr))),
            (T('View'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/%s' % (app, response.view))),
            (T('DB Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/db.py' % app)),
            (T('Menu Model'), False,
             URL(
                 'admin', 'default', 'edit/%s/models/menu.py' % app)),
            (T('Config.ini'), False,
             URL(
                 'admin', 'default', 'edit/%s/private/appconfig.ini' % app)),
            (T('Layout'), False,
             URL(
                 'admin', 'default', 'edit/%s/views/layout.html' % app)),
            (T('Stylesheet'), False,
             URL(
                 'admin', 'default', 'edit/%s/static/css/web2py-bootstrap3.css' % app)),
            (T('Database'), False, URL(app, 'appadmin', 'index')),
            (T('Errors'), False, URL(
                'admin', 'default', 'errors/' + app)),
            (T('About'), False, URL(
                'admin', 'default', 'about/' + app)),
        ]),
        ('web2py.com', False, '#', [
            (T('Download'), False,
             'http://www.web2py.com/examples/default/download'),
            (T('Support'), False,
             'http://www.web2py.com/examples/default/support'),
            (T('Demo'), False, 'http://web2py.com/demo_admin'),
            (T('Quick Examples'), False,
             'http://web2py.com/examples/default/examples'),
            (T('FAQ'), False, 'http://web2py.com/AlterEgo'),
            (T('Videos'), False,
             'http://www.web2py.com/examples/default/videos/'),
            (T('Free Applications'),
             False, 'http://web2py.com/appliances'),
            (T('Plugins'), False, 'http://web2py.com/plugins'),
            (T('Recipes'), False, 'http://web2pyslices.com/'),
        ]),
        (T('Documentation'), False, '#', [
            (T('Online book'), False, 'http://www.web2py.com/book'),
            LI(_class="divider"),
            (T('Preface'), False,
             'http://www.web2py.com/book/default/chapter/00'),
            (T('Introduction'), False,
             'http://www.web2py.com/book/default/chapter/01'),
            (T('Python'), False,
             'http://www.web2py.com/book/default/chapter/02'),
            (T('Overview'), False,
             'http://www.web2py.com/book/default/chapter/03'),
            (T('The Core'), False,
             'http://www.web2py.com/book/default/chapter/04'),
            (T('The Views'), False,
             'http://www.web2py.com/book/default/chapter/05'),
            (T('Database'), False,
             'http://www.web2py.com/book/default/chapter/06'),
            (T('Forms and Validators'), False,
             'http://www.web2py.com/book/default/chapter/07'),
            (T('Email and SMS'), False,
             'http://www.web2py.com/book/default/chapter/08'),
            (T('Access Control'), False,
             'http://www.web2py.com/book/default/chapter/09'),
            (T('Services'), False,
             'http://www.web2py.com/book/default/chapter/10'),
            (T('Ajax Recipes'), False,
             'http://www.web2py.com/book/default/chapter/11'),
            (T('Components and Plugins'), False,
             'http://www.web2py.com/book/default/chapter/12'),
            (T('Deployment Recipes'), False,
             'http://www.web2py.com/book/default/chapter/13'),
            (T('Other Recipes'), False,
             'http://www.web2py.com/book/default/chapter/14'),
            (T('Helping web2py'), False,
             'http://www.web2py.com/book/default/chapter/15'),
            (T("Buy web2py's book"), False,
             'http://stores.lulu.com/web2py'),
        ]),
        (T('Community'), False, None, [
            (T('Groups'), False,
             'http://www.web2py.com/examples/default/usergroups'),
            (T('Twitter'), False, 'http://twitter.com/web2py'),
            (T('Live Chat'), False,
             'http://webchat.freenode.net/?channels=web2py'),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
