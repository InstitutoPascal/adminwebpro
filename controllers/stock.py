@auth.requires_login()
def abm_producto():
    grid = SQLFORM.grid(db.producto)
    return {"grilla": grid}

def abm_deposito():
    grid = SQLFORM.grid(db.deposito)
    return {"grilla": grid}

def remito_entrada():
    grid = SQLFORM.grid(db.remito_entrada)
    return {"grilla": grid}

def remito_salida():
    grid = SQLFORM.grid(db.remito_salida)
    return {"grilla": grid}

def stock():
    return dict(message="stock")




def alta_producto():
    return dict()

def modificacion_producto():
    return dict()


def alta_deposito():
    return dict()

def listado_deposito():
    return dict()

def modificacion_deposito():
    return dict()


def reporte_stock():
    return dict()

def emision_remito():
    return dict()

def emision_remito2():
    return dict()

def resepcion_remito():
    return dict()



def borrar():
    # eliminar algo
    # request.vars tiene un diccionario con todos los parametros de la URL (luego del ?)
    id_a_borrar = request.vars["id"]
    nombre_a_borrar = request.vars["nombre"]
    return dict(mensaje="borrado producto con id = %s y nombre = %s!" % (id_a_borrar, nombre_a_borrar))
