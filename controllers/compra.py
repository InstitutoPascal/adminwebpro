# -*- coding: utf-8 -*-


def index(): return dict(message="hello from proveedor.py")

@auth.requires_login()
def abm_proveedor():
    grid = SQLFORM.grid(db.proveedor)
    return {"grilla": grid}

def informe_subdiarioa():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiarioa")

def informe_subdiariob():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiariob")

def listado_proveedor():
       # presentar formulario para criterios de busqueda
    # definir los campos a obtener desde la base de datos:
    campos = db.proveedor.id_proveedor, db.proveedor.cuit, db.proveedor.razon_social, db.proveedor.ingreso_bruto, db.proveedor.condicion_iva, db.proveedor.domicilio, db.proveedor.localidad, db.proveedor.codigo_postal, db.proveedor.provincia, db.proveedor.pais, db.proveedor.telefono, db.proveedor.celular, db.proveedor.email_proveedor, db.proveedor.pagina_web   
    # definir la condición que deben cumplir los registros:
    criterio = db.proveedor.id_proveedor>0
    ##criterio &= db.cliente.condicion_frente_al_iva=="Responsable Inscripto"
    # ejecutar la consulta:
    lista_proveedor = db(criterio).select(*campos)
     # revisar si la consulta devolvio registros:
    if not lista_proveedor:
        mensaje = "No ha cargado proveedor"
    else:
        mensaje = "Seleccione un proveedor"
        ##primer_cliente = lista_clientes[0]
    return dict(message=mensaje, lista_proveedor=lista_proveedor)

    
def formulario_compras():
     
# definir los campos a obtener desde la base de datos:
    campos = db.proveedor.id_proveedor, db.proveedor.razon_social
    # definir la condición que deben cumplir los registros:
    criterio = db.proveedor.id_proveedor>0
    ##criterio &= db.cliente.condicion_frente_al_iva=="Responsable Inscripto"
    # ejecutar la consulta:
    lista_proveedores = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_proveedores:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
        ##primer_cliente = lista_clientes[0]
    return dict(message=mensaje, lista_proveedores=lista_proveedores)


def detalle_compras():
    grid = SQLFORM.grid(db.detalle_compra)
    return {"grilla": grid}

def lista_detalles():
           # presentar formulario para criterios de busqueda
    return dict(message="Lista de Detalles")
