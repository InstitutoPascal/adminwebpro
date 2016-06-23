# -*- coding: utf-8 -*-

db.define_table("categoria",
    #Field("id"),
    Field("nombre",'string'),
    )

# validación para que no se repita el nombre de categoria:
db.categoria.nombre.requires = IS_NOT_IN_DB(db, "categoria.nombre")

db.define_table("imagen",
    Field("categoria_id", db.categoria),
    Field("titulo", "string"),
    Field("descripcion", "text"),
    Field("archivo", "upload"),
    Field("subido_por", db.auth_user),
    )

# valido que el id de categoría exista, 
# y muestro una lista desplegable con el nombre de categoria:
db.imagen.categoria_id.requires = IS_IN_DB(db, "categoria.id", "-- %(nombre)s ..")
# agrego validador para que el campo titulo no se pueda ingresar vacio:
db.imagen.titulo.requires = IS_NOT_EMPTY()

db.imagen.subido_por.default = auth.user_id if auth.user else 0
db.imagen.subido_por.writable = False
db.imagen.subido_por.readable = False

db.define_table("comentario",
    Field("imagen_id", db.imagen),
    Field("mensaje", "text"),
    Field("subido_por", db.auth_user),
    Field("subido_el", "datetime"),
    )

db.comentario.subido_el.default = request.now
