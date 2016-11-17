# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(B('Adminwebpro'), XML('&trade;&nbsp;'),
                  _class="navbar-brand", _href="/adminwebpro/default/index",
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
    
    (T('Compras'), False, URL('compra', 'index'), [
        (T('ABM Proveedor'), False, URL('compra','abm_proveedor'),[]),        
        (T('Reporte Subdiario'), False, URL('compra','informe_subdiarioa'),[]),
        (T('Lista de Proveedor'), False, URL('compra','listado_proveedor'),[]),
        (T('Formulario de Compras'), False, URL('compra','formulario_compras'),[]),
        ]),
    (T('Stock'), False, URL('stock', 'index'), [
        (T('Reporte'), False, URL('stock', 'reporte_stock'), []),
        (T('ABM Producto'), False, URL('stock', 'abm_producto'), []),
        (T('Deposito nuevo'), False, URL('stock', 'alta_deposito'), []),
        (T('Emision de remito'), False, URL('stock', 'emision_remito'), []),
        (T('Recepcion de remito'), False, URL('stock', 'resepcion_remito'), []),
        ]),
    (T('Pagos'), False, URL('pagos', 'index'), [
        (T('ABM Bancos'), False, URL('pagos', 'alta_bancos'), []),
        (T('ABM Cuentabancaria'), False, URL('pagos', 'alta_cuenta_bancaria'), []),
        (T('Generar Orden de Pago'), False, URL('pagos', 'generar_orden_pagos'), []),
        (T('Generar Reporte'), False, URL('pagos', 'generar_reporte'), []),
        ]),
    (T('Ventas'), False, URL('ventas', 'index'), [
        (T('Clientes'), False, URL('ventas', 'abm_clientes'), []),
        (T('Factura'), False, URL('ventas', 'abm_ventas'), []),
        (T('Reporte de ventas'), False, URL('ventas', 'reporte_ventas'), []),
        (T('Reporte de ventas por Cliente'), False, URL('ventas', 'reporte_por_cliente'), []),
        ]),
    (T('Cobranzas'), False, '#', [
        #(T('Autorizar Cobro'), False, URL('ordencobro', 'autorizar_cobro'), []),
        #(T('Cheques'), False, URL('ordencobro', 'abm_cheques'), []),
        (T('Cobrar'), False, URL('ordencobro', 'generar_orden_cobro'), []),
        (T('Reporte Cobros'), False, URL('ordencobro', 'reporte_cobros'), []),
        (T('Formas de pago'), False, URL('ordencobro', 'forma_pago'), []),
        ]),	
    (T('Sueldos'), False, URL('sueldos', 'index'), [
         (T('ABM Empleados'), False, URL('sueldos', 'abm_empleados'), []),
         (T('ABM Familiares'), False, URL('sueldos', 'abm_familiares'), []),
         (T('ABM Horas'), False, URL('sueldos', 'abm_horas'), []),
         (T('Reporte Legajos'), False, URL('sueldos', 'reportes_empleados2'), []),
          (T('Reporte Horas'), False, URL('sueldos', 'reportes_horas2'), []),
          (T('Reporte Familiares'), False, URL('sueldos', 'reportes_familiares2'), []),
         (T('Formulario Legajos'), False, URL('sueldos', 'legajos'), []),
         (T('Formulario Familiares'), False, URL('sueldos', 'familiar'), []),
         # (T('Reporte Horas'), False, URL('sueldos', 'reportes_horas'), []),
           (T('Formulario Horas'), False, URL('sueldos', 'horas'), []), 
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
