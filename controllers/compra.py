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
    from datetime import datetime
    fecha=datetime.now()
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
        
    return locals()


def detalle_compras():
    # datos predeterminados para completar el formulario
    item = {"id_producto": -1, "cantidad": 1}
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if "modificar" in request.post_vars:
        pro = request.post_vars.getlist("item[]")
        cnt = request.post_vars.getlist("cantidad[]")
        contador = 0
        for p in pro:
            for i in session["items_compra"]:
                if str(p) in str(i["id_producto"]):
                    session["items_compra"][contador]["cantidad"]=int(cnt[contador])
            contador += 1
    if request.vars["boton_enviar"]:
        # obtengo los valores completados en el formulario
        id_proveedor = request.vars["id_proveedor"]
        fecha_factura = request.vars["fecha_factura"]
        numero_factura = request.vars["numero_factura"]
        # guardo los datos elegidos en la sesión
        session["id_proveedor"] = id_proveedor
        session["fecha_factura"] = fecha_factura
        session["numero_factura"] = numero_factura
        session["items_compra"] = []
        #session["tipo_iva"]= tipo_iva
        #session["tipo_factura"] = tipo_factura
        #session["forma_pago"] = forma_pago
        #ssession["tipo_compra"] = tipo_compra
    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_producto = request.vars["id_producto"]
        
        if existe==0:
            cantidad = request.vars["cantidad"]
            item = {"id_producto": id_producto, "cantidad": int(cantidad)}
            # busco en la base de datos el registro del producto seleccionado
            reg_producto = db(db.producto.id_producto==id_producto).select().first()
            item["detalle_producto"] = reg_producto.detalle_producto
            item["precio_producto"] = reg_producto.precio_producto
            # guardo el item en la sesión
            session["items_compra"].append(item)
    print request.vars["accion"]
    if request.vars["accion"] == "eliminar_item":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
    
        session["items_compra"].pop(i)
        #al precionar el boton eliminar la accion queda en f5 y volvia a llamar a eliminar cuando actualizabamos seguia eliminando
        redirect (URL(c="compra",f="detalle_compras"))
        
    if request.vars["accion"] == "modificar":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])
        print session["items_compra"][i]
        #item = session["items_compra"].pop(i)
    # busco en la base de datos al cliente para mostrar su info
    registros = db(db.proveedor.id_proveedor==session["id_proveedor"]).select()
    registro_proveedor = registros.first()
    #aca llamo a los productos

    producto_temporal = SQLFORM.factory(Field ("id_producto", label="Producto", requires=IS_NOT_EMPTY(error_message="Elija un Producto"), widget = SQLFORM.widgets.autocomplete(
     request, db.producto.detalle_producto, id_field=db.producto.id_producto)), Field("cantidad", "integer", default=(1)))
    if producto_temporal.process().accepted:
        id_producto = request.vars["id_producto"]
        exist = False
        for i in session["items_compra"]:
            #if id_producto in session["items_compra"][i]["id_producto"]:
            #    print "hola"
            if str(id_producto) in str(i["id_producto"]):
                exist=True
        if exist == False:
            
            cantidad = request.vars["cantidad"]
            print cantidad
            item = {"id_producto": id_producto, "cantidad": int(cantidad)}
            # busco en la base de datos el registro del producto seleccionado
            reg_producto = db(db.producto.id_producto==id_producto).select().first()
            item["detalle_producto"] = reg_producto.detalle_producto
            item["precio_producto"] = reg_producto.precio_producto
            # guardo el item en la sesión
            session["items_compra"].append(item)
        
    elif producto_temporal.errors:
        response.flash = 'el formulario tiene errores'
    
    #lista_productos = db(db.producto.id_producto>0).select()
    # le pasamos las variables a la vista para armar el html
    #igualamos a 0 las variables
    total_neto = 0
    iva = 0
    total_bruto = 0
    for item in session["items_compra"]:
        total_neto += item["precio_producto"] * item["cantidad"]
        iva += item["precio_producto"] * item["cantidad"] * 0.105
        total_bruto += item["precio_producto"] * item["cantidad"] * 1.105
    return dict(id_proveedor=session["id_proveedor"], fecha_factura=session["fecha_factura"], 
                numero_factura=session["numero_factura"], 
                registro_proveedor=registro_proveedor, 
                items_compra=session["items_compra"], item_modificar=item,
                total_neto=total_neto, iva=iva, total_bruto=total_bruto, producto_temporal=producto_temporal )


def compra_guardada():
           # presentar formulario para criterios de busqueda
    return dict(message="Compra Guardada")
