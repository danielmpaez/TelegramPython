from telegram.ext  import Updater, CommandHandler
import os
import pymongo
 
class users:
    def __init__(self, name, edad, telefono):
        self.name = name
        self.edad = edad
        self.telefono = telefono

    def insertar(users):
        base_de_datos = obtener_bd()
        users = base_de_datos.users
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

#Funcion de saludo 
def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))
#Funcion despedida        
def adios(update, context):
    update.message.reply_text(
        'Adios {}'.format(update.message.from_user.first_name))


#Funcion Signup
#Funcion despedida        
def signup (update, context):
    update.message.reply_text(
        'Ingresa tu mail para el registro ')

updater = Updater('1061491150:AAHd2hlo9dPkxLajLWpsBzhCNc6XD_jg79w', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.dispatcher.add_handler(CommandHandler('chau', adios))
inst= users({},{},{})


updater.dispatcher.add_handler(CommandHandler('signup', users.actualizar()))



updater.start_polling()
updater.idle()



# conexión
con = MongoClient('localhost',27017)
db = con.users
 
# colección
users = db.users
 
resultado = users.find_one()
 
print (resultado)


        