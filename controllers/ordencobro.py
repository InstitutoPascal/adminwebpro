# -*- coding: utf-8 -*-
def reporte_cobros():
    repor = db((db.ventas.buscar_cliente == db.Clientes.ClienteId)&(db.cobros.venta_id == db.ventas.id) & (db.cobros.formas_pago==db.formas_pago.id)).select()
    return dict(repor=repor)
def index():
	pass
def generar_orden_cobro():
	form = SQLFORM(db.cobros)
    	if form.accepts(request,session):
        	response.flash = 'Nuevo cobro'
    	elif form.errors:
        	response.flash = 'Hsy errores en el formulario'
	return dict(form=form)
def forma_pago():
	form = SQLFORM.grid(db.formas_pago)
	return dict(form=form)
