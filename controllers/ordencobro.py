# -*- coding: utf-8 -*-
def reporte_cobros():
    repor = db((db.ventas.buscar_cliente == db.cliente.id_cliente)&(db.cobros.venta_id == db.ventas.id) & (db.cobros.formas_pago==db.formas_pago.id)).select()
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
def pdf():
    response.title = "Recibo de venta %s " %(request.args(0)) 
    import os
    # create a small table with some data:
    rows = [THEAD(TR(TH("Key", _width="70%"), TH("Value", _width="30%"))),
            TBODY(TR(TD("Hello"), TD("60")), 
                  TR(TD("World"), TD("40")))]
    table = TABLE(*rows, _border="0", _align="center", _width="50%")

    if request.extension == "html":
        from gluon.contrib.pyfpdf import FPDF, HTMLMixin

        # create a custom class with the required functionality 
        class MyFPDF(FPDF, HTMLMixin):
            def header(self): 
                logo = os.path.join(request.env.web2py_path, "applications", "adminwebpro", "static", "images", "images.jpeg")
                self.image(logo, 10, 8, 33)
                self.set_font('Arial', 'B', 15)
                self.cell(65) # padding
                self.cell(60, 10, response.title, 1, 0, 'C')
                self.ln(20)

            def footer(self):
                "hook to draw custom page footer (printing page numbers)"
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                txt = 'Page %s of %s' % (self.page_no(), self.alias_nb_pages())
                self.cell(0, 10, txt, 0, 0, 'C')

        pdf = MyFPDF()
        # create a page and serialize/render HTML objects
        pdf.add_page()
        pdf.write_html(str(XML(table, sanitize=False)))
        pdf.write_html(str(XML(CENTER('NADA'), sanitize=False)))
        # prepare PDF to download:
        response.headers['Content-Type'] = 'application/pdf'
        return pdf.output(dest='S')
    else:
        # normal html view:
        return dict(chart=chart, table=table)
