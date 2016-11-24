# -*- coding: utf-8 -*-
from datetime import date
def index():
    #args es una abrebiacion de elementos nos trae
    a=db(db.compra.id_compra == request.args(0)).select()
    print a
    return dict(message="hello from proveedor.py")

@auth.requires_login()
def abm_proveedor():
    grid = SQLFORM.grid(db.proveedor)
    return {"grilla": grid}

def formulario_orden_compras():
    return dict (message="Formulario Orden de Compras")

def detalle_orden_compras():
    return dict(message="Detalle Formulario Orden de Compra")

def orden_compras():
    return dict(message="Orden de Compra")


def informe_subdiarioa():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiarioa")

def informe_subdiariob():
       # presentar formulario para criterios de busqueda
    return dict(message="Informe Subdiariob")

def listado_proveedor():
    razon_social = request.post_vars["razon_social"]
    condicion_iva = request.post_vars["condicion_iva"]
    criterio = (db.proveedor.id_proveedor>0)
    where = ""
    if razon_social != "" and razon_social is not None:
        #where += " and upper (razon_social) like upper ('%"+razon_social+"%')"
	where += " and razon_social='%s' " %(razon_social)
    if condicion_iva != "" and condicion_iva is not None:
        where += " and condicion_iva='%s' " %(condicion_iva)
    proveedores = db.executesql("""SELECT * from proveedor where 1=1 %s""" %(where),as_dict=True)
    print """SELECT * from proveedor where 1=1 %s""" %(where)
    lista_proveedor = db(criterio).select()
    if not lista_proveedor:
        mensaje = "No ha cargado proveedor"
    else:
        mensaje = "Seleccione un proveedor"
    return locals()

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
    # cuando presionamos el boton confirmar
    if "confirmar" in request.post_vars:
        pro = request.post_vars.getlist("item[]")
        if len (pro)>0:
            id_compra = db.compra.insert(id_proveedor=session["id_proveedor"], fecha_factura=session["fecha_factura"],
                                         numero_factura=session["numero_factura"], tipo_factura=session["tipo_factura"], forma_pago=session["forma_pago"])

            pro = request.post_vars.getlist("item[]")
            cnt = request.post_vars.getlist("cantidad[]")
            pre = request.post_vars.getlist("precio_producto[]")
            contador = 0
            for p in pro:
                for i in session["items_compra"]:
                    if str(p) in str(i["id_producto"]):
                        db.detalle_compra.insert(id_compra=id_compra, id_producto=int(pro[contador]), precio=float(pre[contador]), cantidad=int(cnt[contador]))
                contador += 1
            redirect(URL(c="compra", f="compra_guardada", args=id_compra))
    # si el usuario completo el formulario, extraigo los valores de los campos:
    if "modificar" in request.post_vars:
        pro = request.post_vars.getlist("item[]")
        cnt = request.post_vars.getlist("cantidad[]")
        pre = request.post_vars.getlist("precio_producto[]")
        contador = 0
        for p in pro:
            for i in session["items_compra"]:
                if str(p) in str(i["id_producto"]):
                    session["items_compra"][contador]["cantidad"]=int(cnt[contador])
                    session["items_compra"][contador]["precio_producto"]=float(pre[contador])
            contador += 1
    if request.vars["boton_enviar"]:
        # guardo los datos elegidos en la sesión
        session["id_proveedor"] = request.vars["id_proveedor"]
        session["fecha_factura"] = request.vars["fecha_factura"]
        session["numero_factura"] = request.vars["numero_factura"]
        session["items_compra"] = []
        session["tipo_factura"] = request.vars["tipo_factura"]
        session["forma_pago"] = request.vars["forma_pago"]

    if request.vars["agregar_item"]:
        # obtengo los valores del formulario
        id_producto = request.vars["id_producto"]

        if existe==0:
            cantidad = request.vars["cantidad"]
            item = {"id_producto": id_producto, "cantidad": int(cantidad)}
            # busco en la base de datos el registro del producto seleccionado
            reg_producto = db(db.producto.id_producto==id_producto).select().first()
            item["detalle_producto"] = reg_producto.detalle_producto
            item["precio_compra"] = reg_producto.precio_compra
            # guardo el item en la sesiónF
            session["items_compra"].append(item)

    if request.vars["accion"] == "eliminar_item":
        # elimino el elemento de la lista
        i = int(request.vars["indice"])

        session["items_compra"].pop(i)
        #al presionar el boton eliminar la accion queda en f5 y volvia a llamar a eliminar cuando actualizabamos seguia eliminando
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
     request, db.producto.detalle_producto, id_field=db.producto.id_producto)), Field("cantidad", "integer", default=(1)), submit_button="Agregar Producto")
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

            item = {"id_producto": id_producto, "cantidad": int(cantidad)}
            # busco en la base de datos el registro del producto seleccionado
            reg_producto = db(db.producto.id_producto==id_producto).select().first()
            item["detalle_producto"] = reg_producto.detalle_producto
            item["precio_producto"] = reg_producto.precio_compra
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
    id_compra = request.args[0]
    reg_producto = db(db.compra.id == id_compra).select().first()
    reg_proveedor = db(db.proveedor.id_proveedor == reg_producto.id_proveedor).select().first()
    # busco los datos de cada item vendido (id, cantidad, etc.) y del producto
    q = db.detalle_compra.id_compra == id_compra
    q &= db.producto.id_producto == db.detalle_compra.id_producto
    reg_detalle_compra = db(q).select()
    return dict(message="vista_previa", 
                compra=reg_producto, 
                proveedor=reg_proveedor, 
                items=reg_detalle_compra)
