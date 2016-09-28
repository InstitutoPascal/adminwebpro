# -*- coding: utf-8 -*-


def index(): return dict(message="hello from ventas.py")

@auth.requires_login()
def abm_clientes():
    grid = SQLFORM.grid(db.cliente)
    return {"grilla": grid}

@auth.requires_login()
def abm_ventas():
    return dict(message="abm_ventas")

@auth.requires_login()
def detalle_ventas():
    cliente = request.vars["id_cliente"]
    fecha = request.vars["fecha"]
    comprobante = request.vars["comprobante"]
    return dict(titulo="Para el Cliente: %s, Fecha: %s, N°Comprobante:%s" % (cliente, fecha, comprobante))
    #grid = SQLFORM.grid(db.detalle_ventas)
    #return {"grilla": grid}
@auth.requires_login()
def reporte_ventas():
    return dict(message="reporte_ventas")

def vista_previa():
    return dict(message="vista_previa")

def borrar_item():
    # eliminar algo
    # request.vars tiene un diccionario con todos los parametros de la URL (luego del ?)
    id_a_borrar = request.vars["id"]
    #producto_a_borrar = request.vars["producto"]
    return dict(mensaje="Borrado registro del Item = %s" % (id_a_borrar))

def lista_ventas():
    # obtenemos los criterios de busqueda y generamos el reporte
    desde = request.vars["fecha_desde"]
    hasta = request.vars["fecha_hasta"]
    return dict(titulo="Listando Desde: %s Hasta: %s" % (desde, hasta))

def guardado():
    return dict (mensaje= "Se guardo con exito el comprobante")

def confirmar():
    return dict (mensaje= "Finalizar venta")
