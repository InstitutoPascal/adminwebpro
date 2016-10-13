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
    campos = db.cliente.id_cliente, db.cliente.nombre_de_fantasia
    criterio = db.cliente.id_cliente>0
    ##criterio &= db.cliente.condicion_frente_al_iva=="Responsable Inscripto"
    # ejecutar la consulta:
    lista_clientes = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_clientes:
        mensaje = "No ha cargado clientes"
    else:
        mensaje = "Seleccione un cliente"
        ##primer_cliente = lista_clientes[0]
        
    return dict(message=mensaje, lista_clientes=lista_clientes)
    

def emision_remito2():
     # si el usuario completo el formulario, extraigo los valores de los campos:
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        print id_cliente
        fecha = request.vars["fecha"]
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha"] = fecha
    
    registros = db(db.cliente.id_cliente==session["id_cliente"]).select()
    reg_cliente = registros[0]
    
    return dict(id_cliente=session["id_cliente"], fecha=session["fecha"] , reg_cliente=reg_cliente)
   
def emision_remito3():
    return dict()

def emision_remito4():
    return dict()

def resepcion_remito():
    return dict()

def resepcion_remito2():
    return dict()

def resepcion_remito3():
    return dict()

def resepcion_remito4():
    return dict()

def ficha_stock():
    return dict()


def borrar():
    # eliminar algo
    # request.vars tiene un diccionario con todos los parametros de la URL (luego del ?)
    id_a_borrar = request.vars["id"]
    nombre_a_borrar = request.vars["nombre"]
    return dict(mensaje="borrado producto con id = %s y nombre = %s!" % (id_a_borrar, nombre_a_borrar))
