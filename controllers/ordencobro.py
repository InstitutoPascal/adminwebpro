# -*- coding: utf-8 -*-
@auth.requires_login()
def reporte_cobros():
    repor = db((db.ventas.id_cliente == db.cliente.id_cliente)&(db.cobros.venta_id == db.ventas.id) & (db.cobros.formas_pago==db.formas_pago.id)).select()
    return locals()
def index():
	pass
@auth.requires_login()
def generar_orden_cobro():
	form = SQLFORM(db.cobros)
    	if form.accepts(request,session):
        	response.flash = 'Nuevo cobro'
    	elif form.errors:
        	response.flash = 'Hsy errores en el formulario'
	return dict(form=form)
@auth.requires_login()
def forma_pago():
	form = SQLFORM.grid(db.formas_pago)
	return dict(form=form)
@auth.requires_login()
def pdf():
    
    response.title = "Recibo pago "
    cobro = request.args(0) or redirect(URL('/'))
    
    cobro = db((db.cobros.formas_pago==db.formas_pago.id)&(db.cobros.id==cobro)&(db.cobros.venta_id==db.ventas.id)&(db.ventas.id_cliente==db.cliente.id_cliente)).select()
    print cobro
    cobro = cobro.first().as_dict()
   
    import os
    # create a small table with some data:
    logo = os.path.join(request.env.web2py_path, "applications", "adminwebpro", "static", "images", "logo.png")
    rows = [TR(TD(SPAN(B("ADMINWEBPRO")), _width="35%"), TD(B("Recibo de pago"), _width="30%"),TD('Fecha : %s' %(cobro['cobros']['fecha_creacion'].strftime("%d/%m/%Y %H:%M:%S")),_width='35%'))]
    header = TABLE(*rows, _border="0", _align="center", _width="100%")
    rows = [TR(TD(B("Cliente: "), _width="19%"), TD(cobro['cliente']['nombre_de_fantasia'], _width="30%")),
           TR(TD(B("Forma de pago : "), _width="19%"), TD(cobro['formas_pago']['descripcion'], _width="30%")),
           TR(TD(B("Importe : "), _width="19%"), TD('$'+str(cobro['cobros']['importe']), _width="30%"))]
    content = TABLE(*rows, _border="0", _align="center", _width="100%")
    if request.extension == "html":
        from gluon.contrib.pyfpdf import FPDF, HTMLMixin

        # create a custom class with the required functionality 
        class MyFPDF(FPDF, HTMLMixin):
            def footer(self):
                
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                txt = 'Pagina %s de %s' % (self.page_no(), self.alias_nb_pages())
                self.cell(0, 10, txt, 0, 0, 'C')

        pdf = MyFPDF()
        # create a page and serialize/render HTML objects
        pdf.add_page()
        pdf.write_html(str(XML(header, sanitize=False)))
        pdf.ln(5)
        pdf.write_html(str(XML(content, sanitize=False)))
        #pdf.write_html(str(XML(CENTER('NADA'), sanitize=False)))
        # prepare PDF to download:
        response.headers['Content-Type'] = 'application/pdf'
        return pdf.output(dest='S')
    else:
        # normal html view:
        return dict(chart=chart, table=table)
