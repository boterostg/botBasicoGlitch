import telebot
from telebot import *
from os import environ

from random import randrange

import json
import requests

from configBan import *


bot = telebot.TeleBot(environ['TELEGRAM_TOKEN']) #Token del bot 

# Variable que se utilizará en el comando /start para enviarlo como el texto del mensaje del bot
bot_text = '''				
Este bot ha sido creado aquí. https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])



menuKeyboard = types.InlineKeyboardMarkup()
menuKeyboard.add(types.InlineKeyboardButton('Ayuda', callback_data='ayuda'),
           types.InlineKeyboardButton('Creador', callback_data='creador'))

yoNuncaKeyboard = types.InlineKeyboardMarkup()
yoNuncaKeyboard.add(types.InlineKeyboardButton('Me apunto', callback_data='yo'))

propuestaInlineKeyboard = types.InlineKeyboardMarkup()
propuestaInlineKeyboard.add(types.InlineKeyboardButton('Me apunto', callback_data='inlineApuntado'))



  


@bot.message_handler(commands=['menu'])
def menu(m):

  cid = m.chat.id
  bot.send_message(cid, "Menu", reply_markup=menuKeyboard, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ['ayuda', 'creador'])
def callback_handlerMenu(call):
  
  cid = call.message.chat.id
  mid = call.message.message_id
  info = call.data
  
  #bot.send_message(cid, "Has pulsado " + str(info))
  
  if info == "ayuda":
    #bot.send_message(cid, "Entramos en  " + str(info))
    
    bot.edit_message_text("Has pulsado ayuda", cid, mid, reply_markup=menuKeyboard, parse_mode="Markdown")
    
  elif info == "creador":
    
    #bot.send_message(cid, "Entramos en  " + str(info))
    
    bot.edit_message_text("Mi creador es : @batichico" , cid, mid, reply_markup=menuKeyboard , parse_mode="Markdown")
  

@bot.inline_handler(lambda query: query.query.startswith('propuesta') and len(query.query.split()) > 1)
def function_propuesta(q):

  cid = q.from_user.id
  txt = q.query.split(None, 1)[1]

  keyboard = types.InlineKeyboardMarkup()
  keyboard.add(types.InlineKeyboardButton("Me apunto", callback_data="propuesta {}".format(txt)))

  article = types.InlineQueryResultArticle(1, "Enviar propuesta", types.InputTextMessageContent(txt), reply_markup=keyboard)
  bot.answer_inline_query(q.id, [article], cache_time=1)


  
  
@bot.callback_query_handler(func=lambda call: call.data.startswith('propuesta'))
def function_button(call):
  
  mensaje = call.data.split(None, 1)[1]

  

  idUsuario = call.from_user.id
  nombreUsuario = call.from_user.username
  nombreUsuario = "@"+nombreUsuario
  
  todoCall = call
  print(str(todoCall))
  
 
  mid = call.inline_message_id
  
  
  contenido = mensaje + "\n\n"
  
  apuntados = mensaje.split("\n\n")[1:]
  
  #bot.answer_callback_query(call.id , str(mensaje) , show_alert=True)
  
  if nombreUsuario not in mensaje:
  
    mensaje = contenido  + nombreUsuario
     
    bot.answer_callback_query(call.id , "Vamos a apuntarte, apuntados: " + str(apuntados)  , show_alert=True)
    bot.edit_message_text(mensaje,  inline_message_id=call.inline_message_id , reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")
    
    
    apuntados = mensaje.split("\n\n")[1:]
  
  
  else :

    apuntadosS = ""

    apuntados = mensaje.split("\n\n")[1:]

    contenido = mensaje.split("\n\n")[0]

    contenido = contenido + "\n\n"

    apuntados.remove(str(nombreUsuario))
  
    
    bot.answer_callback_query(call.id , str(apuntados) , show_alert=True)
                      
   
     
    
    '''
    
  
  
  mid = call.message.message_id
  mensaje = call.message.text
  
  contenido = mensaje + "\n\n"
  
  apuntados = mensaje.split("\n\n")[1:]
  
  
    else :

      apuntadosS = ""

      apuntados = mensaje.split("\n\n")[1:]

      contenido = mensaje.split("\n\n")[0]

      contenido = contenido + "\n\n"

      apuntados.remove(str(nombreUsuario))

      if len(apuntados) == 0 :

        bot.edit_message_text(contenido, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

      elif len(apuntados) == 1 :
          mensaje = contenido  + apuntados[0]
          bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

      elif len(apuntados) >= 1 : 
        for apuntado in apuntados:
          apuntadosS = apuntadosS + apuntado + "\n\n" 

        mensaje = contenido  + apuntadosS
        bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

    
    
    
    
 
  
  
  
  
  

  else :
    
    apuntadosS = ""
    
    apuntados = mensaje.split("\n\n")[1:]
    
    contenido = mensaje.split("\n\n")[0]
    
    contenido = contenido + "\n\n"
    
    apuntados.remove(str(nombreUsuario))
                      
    if len(apuntados) == 0 :
      
      bot.edit_message_text(contenido, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")
      
    elif len(apuntados) == 1 :
        mensaje = contenido  + apuntados[0]
        bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")
        
    elif len(apuntados) >= 1 : 
      for apuntado in apuntados:
        apuntadosS = apuntadosS + apuntado + "\n\n" 

      mensaje = contenido  + apuntadosS
      bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")
     
  '''
  
@bot.callback_query_handler(func=lambda call: call.data in ['yosi'])
def callback_handlerYoNunca(call):
  
  cid = call.message.chat.id
  idUsuario = call.from_user.id
  nombreUsuario = call.from_user.first_name	
  
  mid = call.message.message_id
  mensaje = call.message.text
  
  arrayApuntados = arrayUsuarios
  
  nombreUsuarioClick = call.message.from_user.first_name	
  
  if idUsuario not in arrayApuntados or len(arrayApuntados) == 0 :

    añadirUser = {mid:{idUsuario:nombreUsuario}}

    arrayApuntados.append(añadirUser)
    
    nombreNuevoUser = arrayApuntados[-1][mid][idUsuario]

    mensaje = mensaje + "\n\n" + nombreNuevoUser
    bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

    bot.send_message(cid, str(arrayApuntados))

  elif idUsuario in arrayApuntados :
    arrayApuntados.pop(idUsuario)
    
 

@bot.callback_query_handler(func=lambda call: call.data in ['inlineApuntado'])
def callback_handlerPropuesta(call):
  
  print("Entramos en handler")
  
  print("CALL: " + str(call))
  
  print(str(call.id))
  
  #cid = call.message.chat.id
  idUsuario = call.from_user.id
  nombreUsuario = call.from_user.username
  nombreUsuario = "@"+nombreUsuario
  
  print(str(nombreUsuario))
    
  mid = call.inline_message_id
  
  print(str(mid))
  
  #mensaje = call.message.text
  
  #mensaje = call.data.split(None, 1)[1]
  
  mensaje = call.data
  
  
  contenido = mensaje + "Contenido\n\n"
  
  #contenido = mensaje + "\n\n"
  
  apuntados = mensaje.split("\n\n")[1:]
  
  print("Apuntados: " + str(apuntados))
  
  
  #bot.answer_callback_query(mid , str(apuntados) , show_alert=True)
  
  if nombreUsuario not in mensaje:
    
    print ("entramos en if" + nombreUsuario + "\n" + mensaje)
    
    mensaje = contenido  + nombreUsuario
    
    apuntados = mensaje.split("\n\n")[1:]

    print("Mensaje metido: " + mensaje)
    
    print("Apuntados: " + str(apuntados))
    
    #bot.answer_callback_query(call.id , "Vamos a apuntarte, apuntados: " + str(apuntados)  , show_alert=True)
    bot.edit_message_text(mensaje,  inline_message_id=call.inline_message_id , reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")
    
    print("Mensaje despues metido: " + mensaje)
    
    #bot.edit_message_text(mensaje,  inline_message_id=mid, reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")

    #bot.edit_message_text(mensaje, cid, mid, reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")

    
    
  else :
  
    #print ("entramos en else")
    
    apuntadosS = ""

    apuntados = mensaje.split("\n\n")[1:]
    
    #print (apuntados)

    contenido = mensaje.split("\n\n")[0]

    contenido = contenido + "\n\n"

    apuntados.remove(str(nombreUsuario))

    if len(apuntados) == 0 :

      bot.edit_message_text(contenido, cid, mid, reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")

    elif len(apuntados) == 1 :
        mensaje = contenido  + apuntados[0]
        bot.edit_message_text(mensaje, cid, mid, reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")

    elif len(apuntados) >= 1 : 
      for apuntado in apuntados:
        apuntadosS = apuntadosS + apuntado + "\n\n" 

      mensaje = contenido  + apuntadosS
      bot.edit_message_text(mensaje, cid, mid, reply_markup=propuestaInlineKeyboard, parse_mode="Markdown")







@bot.callback_query_handler(func=lambda call: call.data in ['yo'])
def callback_handlerYoNunca(call):
  
  cid = call.message.chat.id
  idUsuario = call.from_user.id
  
  if (call.from_user.username is None):
    bot.answer_callback_query(call.id, "Tienes que tener nickname, @ lo que sea", show_alert=True)
  else:
    nombreUsuario = call.from_user.username
    nombreUsuario = "@"+nombreUsuario

    mid = call.message.message_id
    mensaje = call.message.text

    contenido = mensaje + "\n\n"

    apuntados = mensaje.split("\n\n")[1:]


    if nombreUsuario == "@elraro":

      #print(str(call.id) + " " + nombreUsuario)
      bot.answer_callback_query(call.id, "HDP", show_alert=True)

    else:

      if nombreUsuario not in mensaje:

        mensaje = contenido  + nombreUsuario
        bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        apuntados = mensaje.split("\n\n")[1:]
      else :

        apuntadosS = ""

        apuntados = mensaje.split("\n\n")[1:]

        contenido = mensaje.split("\n\n")[0]

        contenido = contenido + "\n\n"

        apuntados.remove(str(nombreUsuario))

        if len(apuntados) == 0 :

          bot.edit_message_text(contenido, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        elif len(apuntados) == 1 :
            mensaje = contenido  + apuntados[0]
            bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

        elif len(apuntados) >= 1 : 
          for apuntado in apuntados:
            apuntadosS = apuntadosS + apuntado + "\n\n" 

          mensaje = contenido  + apuntadosS
          bot.edit_message_text(mensaje, cid, mid, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

# Inicio charla 1- 19/07/2018


  

@bot.message_handler(commands=['start', 'help']) 	# Comando /start o /help . Cuando un usuario escriba cualquiera de los comandos 							
def send_welcome(message):			 	
	bot.reply_to(message, bot_text)			# El bot responde con el contenido de la variable bot_text al mensaje.

  
@bot.message_handler(commands=['ayuda'])		# Ejemplo de comando /ayuda que en vez de pasarle una variable, directamente escribimos 
def ayuda(message):					
	bot.reply_to(message, 'ahora mismo te ayudo')   # El bot responde 'ahora mismo te ayudo' al mensaje
  
#Inicio charla 2 - 31/07/2018


@bot.message_handler(commands=['ruleta'])
def ruleta(message):

  cid = message.chat.id
  nombreUsuario = message.from_user.username
  idUsuario = message.from_user.id
  rnd = randrange(0, int(5))

  if rnd == 4:
    bot.send_message(cid, "Pummmm tas muelto @" + nombreUsuario )
    bot.kick_chat_member(cid,idUsuario)
    bot.unban_chat_member(cid, idUsuario)

  else:

    bot.send_message(cid, "Te has salvado amijo @" + nombreUsuario)
  
#Fin charla 2 - 31/07/2018
  
@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  idUsu = message.from_user.id
  
  if message.text.lower() ==  "bot vete" :
    
    if idUsu== 239822769:
      bot.send_message(cid, 'vale :C, adios mi gente!')	
      bot.leave_chat(cid)
    
  
  if "ban" in message.text.lower().split() :	
    
    bot.send_message(cid, 'estas ban')	
  
  if message.text.lower() == "holi":			# Comparamos el texto el mensaje si es igual a 'holi'
   
    id = message.from_user.id				# Guardamos en una variable el id del usuario que envió el mensaje			
    
    nombre = message.from_user.first_name		# Guardamos en una variable el nombre del usuario que envió el mensaje
    
    bot.send_message(cid, 'holi ' + nombre )		# El bot responde 'holi' y después el nombre del usuario que guardamos en la variable da arriba
   

    if id == 239822769:					# Comparamos el id guardado del usuario con un id que le hemos pasado
		
        bot.send_message( cid, 'Hola mi creador 😙')	# Si es igual responde el mensaje que hemos introducido al chat indicado
        
    elif id == 270803389 :				# En este caso el id lo comparamos con otra id diferente 
	
      bot.send_message( cid, 'Holi manuel')		# Aquí envia al chat que le hemos hablado 'Holi manuel'

      bot.send_message( 115659666, 'Holi manuel')	# Aquí probamos a pasarle en vez de cid, un id de un usuario y le enviará el mensaje por mensaje 
							#privado

    else:						# Si no se da ninguno de los resultados de arriba hará lo siguiente:
      
       bot.send_message( cid, 'No estás registrado')	# Enviará por el chat el mensaje 'No estás registrado'
  
  if message.text.lower() == "mensaje":			# Aquí probamos un if comparandolo con un String(una cadena de carácteres)
		
    bot.send_message( cid, 'mensaje')			# Si es así contestará 'mensaje'
    
  
    
	
#Fin charla 1 - 19/07/218
  if message.text.lower().startswith('/'):
    idMensaje = message.message_id
    idUsuario = call.from_user.id
    
    bot.delete_message(cid,idMensaje)
    
    dt = datetime.datetime(2018, 8, 21, 16, 00)
    unixTime = time.mktime(dt.timetuple())
    
    bot.restrict_chat_member(self, cid, idUsuario, until_date=None, can_send_messages=False,
                             can_send_media_messages=False, can_send_other_messages=False,
                             can_add_web_page_previews=False)
    
  #Inicio charla 3 - 08/08/2018
  if message.text.lower().startswith('participo con el numero'):

      cid = message.chat.id
      mensaje=message.text
      rnd = randrange(0, int(9))
      respuesta = ' '.join(mensaje.split(" ")[4:])

      #bot.send_message(cid, "la respuesta es: " + respuesta)
      #bot.send_message(cid, str(rnd))

      if int(respuesta) == rnd:
        bot.send_message(cid, "Has acertado")

      else:
        bot.send_message(cid, "Has fallado, el número era " + str(rnd))

  #Fin charla 3 - 08/08/2018
  
  if message.text.lower().startswith("propuesta") and len(message.text)>1:
      cid = message.chat.id
      nombre = message.from_user.first_name
      mensaje = message.text
      
      respuesta = ' '.join(mensaje.split(" ")[1:])

      bot.send_message(cid, respuesta, reply_markup=yoNuncaKeyboard, parse_mode="Markdown")

  #Inicio charla 2 - 31/07/2018

  if "boti di" in message.text.lower():               # Comparamos el texto el mensaje si es igual a "boti di"

      cid = message.chat.id                              #Id del chat
      mensaje=message.text                               #Mensaje completo
      respuesta = ' '.join(mensaje.split(" ")[2:])       #Respuesta
      bot.send_message(cid, respuesta)                   #El bot envía la respuesta


#Respuesta a la entrada de un usuario al grupo 
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                    #Id del chat
    cname = m.chat.title                               #Nombre del grupo
    bienvenida = ""                                    #Variable dónde guardaremos el mensaje de bienvenida

    infoMesaje = str(m)
    
    nuevoUsuarioId = m.new_chat_member.id
    nuevoUsuarioName = m.new_chat_member.username
    añadidoPorId = m.from_user.id
    añadidoPor = m.from_user.username
    
    #bot.send_message(cid, infoMesaje) 
    if nuevoUsuarioName == "Botinutilbot":
     
      if cid != -1001318959349:
        
        bot.send_message(cid, añadidoPor + " , para que hostias me metes, este no es mi grupo joderrr!")
        bot.leave_chat(cid)
      
      
    if añadidoPorId == nuevoUsuarioId:
      bot.send_message(cid, 'Entrado por enlace de invitación') 
      
      
      #bot.send_message(cid, infoMesaje) 
    else:
      bot.send_message(cid, 'añadido por: ' + añadidoPor) 
      bot.send_message(cid, str(cid)) 
      
    if (m.new_chat_member.username is None):           #Si el usuario no tiene nickname
        nun = m.new_chat_member.first_name             #Guardamos el primer nombre del usuario
        
        if (m.new_chat_member.last_name is not None):  #Si el usuario tiene apellido
            nun += " "                        
            nun += m.new_chat_member.last_name         #Se guarda el apellido
            
        else:                                          #Si no tiene apellido
            bienvenida = "Bienvenido al grupo"         #Se guarda "Bienvenido al grupo"
            bienvenida += str(cname)                   #Se le añade el nombre del chat detras de "Bienvenido al grupo"
            bienvenida += " "
    else:                                              #Si el usuario tiene nickname
        nun = m.new_chat_member.username               #Se guarda en nun el nickname del usuario
        bienvenida = "Bienvenido al grupo "            #Se guarda "Bienvenido al grupo"
        bienvenida += str(cname)                       #Se le añade el nombre del chat detras de "Bienvenido al grupo"
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun))  #Se envía el mensaje de bienvenida concatenando el nombre/nickname del usuario

    
#Respuesta a la salida de un usuario del grupo 
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def command_bye(m):
    cid = m.chat.id                                    #Id del grupo
    despedida = ""                                     #Variable dónde guardaremos el mensaje de despedida
    
    if (m.left_chat_member.username is None):          #Si el usuario no tiene nickname
        nun = m.left_chat_member.first_name            #Guardamos el primer nombre del usuario
        
        if (m.left_chat_member.last_name is not None): #Si el usuario tiene apellido
            nun += " "
            nun += m.left_chat_member.last_name        #Se guarda el apellido
            
    else:                                              #Si el usuario tiene nickname
        nun = m.left_chat_member.username              #Se guarda en nun el nickname del usuario
        despedida = "Hasta luego "                     #Se guarda "Hasta luego"
        despedida += " @"

    bot.send_message(cid, str(despedida) + str(nun))   #Se envía el mensaje de despedida concatenando el nombre/nickname del usuario

  
#Fin charla 2 - 31/07/2018

'''

APUNTESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSs

import random
from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # Taken from itertools recipes:
    # https://docs.python.org/2/library/itertools.html#recipes
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

apuntados = ["peter","alice","andy","patxi","richard","ana"]
parejas = ""

print(str(apuntados))

random.shuffle(apuntados)
print(len(apuntados))
if len(apuntados) >1:
    for primero, segundo in grouper(apuntados, 2):
        parejas = parejas + str(primero) +  " y " + str(segundo) +"\n"
else:
      bot.send_message(cid,"solo hay uno")
print(parejas)

'''
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
