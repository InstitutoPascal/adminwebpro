# -*- coding: utf-8 -*-

def index():
    return dict(message="pagina predeterminada")

@auth.requires_membership(role="Gerente")
def abm_categoria():
    grid = SQLFORM.grid(db.categoria)
    return {"grilla": grid}

def abm_ejemplo():
    return dict(message="ABM EJEMPLO")

def reporte_ejemplo():
    # presentar formulario para criterios de busqueda
    return dict(message="REPORTE ejemplo")

def registrar_comprobante():
    return dict(message="REGISTRAR COMPROBANTE")

def reporte():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando desde fecha %s hasta fecha %s" % (fecha_desde, fecha_hasta))

def borrar():
    # eliminar algo
    # request.vars tiene un diccionario con todos los parametros de la URL (luego del ?)
    id_a_borrar = request.vars["id"]
    nombre_a_borrar = request.vars["nombre"]
    return dict(mensaje="borrado registro con id = %s y nombre = %s!" % (id_a_borrar, nombre_a_borrar))
