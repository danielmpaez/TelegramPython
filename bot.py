from telegram.ext import Updater, CommandHandler
from mongo import Users


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

updater.dispatcher.add_handler(CommandHandler('signup', Users.Actualizar))




updater.start_polling()
updater.idle()

