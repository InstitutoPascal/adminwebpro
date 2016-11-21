@auth.requires_login()
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
     # datos predeterminados para completar el formulario
    item = {"id_producto": -1, "cantidad": 1}
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_cliente = request.vars["id_cliente"]
        print id_cliente
        fecha = request.vars["fecha"]
        # guardo los datos elegidos en la sesión
        session["id_cliente"] = id_cliente
        session["fecha"] = fecha
        session["items_agregados"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_producto = request.vars["id_producto"]
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        session["item"] = item
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.producto.id_producto==id_producto).select().first()
        item["detalle_producto"] = reg_producto.detalle_producto
        item["precio_producto"] = reg_producto.precio_compra
        # guardo el item en la sesión
        session["items_agregados"].append(item)
    if request.vars["accion"] == "eliminar":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
        session["items_agregados"].pop(i)
    if request.vars["accion"] == "modificar":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
        item = session["items_agregados"].pop(i)
    # busco en la base de datos al cliente para mostrar su info
    registros = db(db.cliente.id_cliente==session["id_cliente"]).select()
    reg_cliente = registros[0]
    lista_productos = db(db.producto.id_producto>0).select()
    # le pasamos las variables a la vista para armar el html
    
    total_bruto = 0
    return dict(id_cliente=session["id_cliente"], fecha=session["fecha"] , reg_cliente=reg_cliente , lista_productos=lista_productos,
                items_agregados=session["items_agregados"] , item_modificar=item )
   
def emision_remito3():
    registros = db(db.cliente.id_cliente==session["id_cliente"]).select()
    reg_cliente = registros[0]
    return dict(id_cliente=session["id_cliente"], reg_cliente=reg_cliente , items_agregados=session["items_agregados"]  )


def emision_remito4():
    """if request.vars["boton_enviar"]:
        id_cliente = request.vars["id_cliente"]
        session["fecha"] = fecha
        session["id_cliente"] = id_cliente
    registros = db(db.cliente.id_cliente==session["id_cliente"]).select()
    reg_cliente = registros[0]
    """
    #return dict(fecha=session["fecha"] , id_cliente=session["id_cliente"] , reg_cliente=reg_cliente , items_agregados=session["items_agregados"])
    return locals()

def resepcion_remito():
    campos = db.proveedor.id_proveedor, db.proveedor.razon_social
    criterio = db.proveedor.id_proveedor>0
    # ejecutar la consulta:
    lista_proveedores = db(criterio).select(*campos)
    # revisar si la consulta devolvio registros:
    if not lista_proveedores:
        mensaje = "No ha cargado proveedor"
    else:
        mensaje = "Seleccione un proveedor"
    return dict(message=mensaje, lista_proveedores=lista_proveedores)


def resepcion_remito2():
    # datos predeterminados para completar el formulario
    item = {"id_producto": -1, "cantidad": 1}
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_proveedor = request.vars["id_proveedor"]
        fecha = request.vars["fecha"]
        # guardo los datos elegidos en la sesión
        session["id_proveedor"] = id_proveedor
        session["fecha"] = fecha
        session["items_agregados"] = []
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_producto = request.vars["id_producto"]
        cantidad = request.vars["cantidad"]
        item = {"id_producto": id_producto, "cantidad": int(cantidad)}
        session["item"] = item
        # busco en la base de datos el registro del producto seleccionado
        reg_producto = db(db.producto.id_producto==id_producto).select().first()
        item["detalle_producto"] = reg_producto.detalle_producto
        item["precio_producto"] = reg_producto.precio_compra
        # guardo el item en la sesión
        session["items_agregados"].append(item)
    if request.vars["accion"] == "eliminar":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
        session["items_agregados"].pop(i)
    if request.vars["accion"] == "modificar":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
        item = session["items_agregados"].pop(i)
    # busco en la base de datos al cliente para mostrar su info
    registros = db(db.proveedor.id_proveedor==session["id_proveedor"]).select()
    reg_proveedor = registros[0]
    lista_productos = db(db.producto.id_producto>0).select()
    # le pasamos las variables a la vista para armar el html
    
    total_bruto = 0
    return dict(id_proveedor=session["id_proveedor"], fecha=session["fecha"] , reg_proveedor=reg_proveedor , lista_productos=lista_productos,
                items_agregados=session["items_agregados"] , item_modificar=item )
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
def ingreso_mercaderia():
    id_compra=request.args(0) or redirect(URL(c='default',f='index'))
    detalle=db(db.detalle_compra.id_compra==id_compra).select()
    id_remito_entrada=db.remito_entrada.insert(id_compra=id_compra)
    for d in detalle:
        for q in range(d.cantidad):
            db.stock.insert(remito_entrada=id_remito_entrada,id_producto=d.id_producto)
    
    #redirect(URL(c='stock', f='emision_remito4',args=id_remito_entrada))
    return locals()
