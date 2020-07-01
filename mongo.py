import pymongo
 
from pymongo import MongoClient
 
# conexión
con = MongoClient('localhost',27017)
db = con.users
 
# colección
users = db.users
 
resultado = users.find_one()
 
print (resultado)

class users:
    def __init__(self, name, edad, telefono):
        self.name = name
        self.edad = edad
        self.telefono = telefono

    def insertar(users):
    base_de_datos = obtener_bd()
    productos = base_de_datos.users
    return users.insert_one({
        "name": users.name,
        "edad": users.edad,
        "telefono": users.telefono,
        }).inserted_id

    def actualizar(id, users):
        base_de_datos = obtener_bd()
        resultado = base_de_datos.users.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "name": users.name,
                "edad": users.edad,
                "telefono": users.telefono,
            }
        })
    return resultado.modified_count

    def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.users.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count