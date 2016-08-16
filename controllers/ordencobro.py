# -*- coding: utf-8 -*-
def index():
	pass
def generar_orden_cobro():
	
	form = SQLFORM(db.cobros)
	return dict(form=form)
def forma_pago():
	form = SQLFORM(db.formas_pago)
	if form.accepts(request,session):
		response.flash = 'Nueva forma de pago'
	elif form.errors:
		response.flash = 'El formulario contiene errores'	
	return dict(form=form)