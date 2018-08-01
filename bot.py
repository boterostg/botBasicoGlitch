import telebot			#Importaciones
from os import environ		

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN']) #Token del bot 

# Variable que se utilizará en el comando /start para enviarlo como el texto del mensaje del bot
bot_text = '''				
Howdy, how are you doing?
Source code on https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

# Inicio lección 1- 19/07/2018

@bot.message_handler(commands=['start', 'help']) 	# Comando /start o /help . Cuando un usuario escriba cualquiera de los comandos 							
def send_welcome(message):			 	
	bot.reply_to(message, bot_text)			# El bot responde con el contenido de la variable bot_text al mensaje.

  
@bot.message_handler(commands=['ayuda'])		# Ejemplo de comando /ayuda que en vez de pasarle una variable, directamente escribimos 
def ayuda(message):					
	bot.reply_to(message, 'ahora mismo te ayudo')   # El bot responde 'ahora mismo te ayudo' al mensaje
  
#Inicio charla 2 - 31/07/2018
  
#Comando para simular una ruleta rusa en grupos de Telegram
@bot.message_handler(commands=['ruleta'])
def ruleta(message):

  cid = message.chat.id					#Id del chat
  nombreUsuario = message.from_user.username		#Nicknmae del usuario
  idUsuario = message.from_user.id			#Id del usuario
  rnd = randrange(0, int(5))				#Generación de número aleatorio entre 0 y 5

  if rnd == 4:						#Si el número aleatorio es igual a 4
	
    bot.send_message(cid, "Pummmm estas muerto @" + nombreUsuario )	#El bot envía mensaje de que has muerto y añade el nickname del usuario en el mensaje
    bot.kick_chat_member(cid,idUsuario)					#El bot expulsa al usuario del grupo restringiendolo del grupo
    bot.unban_chat_member(cid, idUsuario)				#El bot quita la restrinción al usuario para que así pueda volver al grupo

  else:									#Si el número aleatorio es diferente de 4

    bot.send_message(cid, "Te has salvado amigo @" + nombreUsuario)	#El bot envía un mensaje diciendo que se ha salvado añadiendo el nickname del usuario
  
#Fin charla 2 - 31/07/2018
  
@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# Guardamos en la variale cid el id de el mensaje recibido 
  
  if message.text.lower() == "holi":			# Comparamos el texto el mensaje si es igual a 'holi'
   
    id = message.from_user.id				# Guardamos en una variable el id del usuario que envió el mensaje			
    
    nombre = message.from_user.first_name		# Guardamos en una variable el nombre del usuario que envió el mensaje
    
    bot.send_message(cid, 'holi ' + nombre )		# El bot responde 'holi' y después el nombre del usuario que guardamos en la variable da arriba
   

    if id == 239822769:					# Comparamos el id guardado del usuario con un id que le hemos pasado
		
        bot.send_message( cid, 'Hola mi creador 😙')    # Si es igual responde el mensaje que hemos introducido al chat indicado
        
    elif id == 270803389 :				# En este caso el id lo comparamos con otra id diferente 
	
      bot.send_message( cid, 'Holi manuel')		# Aquí envia al chat que le hemos hablado 'Holi manuel'

      bot.send_message( 115659666, 'Holi manuel')	# Aquí probamos a pasarle en vez de cid, un id de un usuario y le enviará el mensaje por mensaje 
							#privado

    else:						# Si no se da ninguno de los resultados de arriba hará lo siguiente:
      
       bot.send_message( cid, 'No estás registrado')	# Enviará por el chat el mensaje 'No estás registrado'
  
  if message.text.lower() == "mensaje":			# Aquí probamos un if comparandolo con un String(una cadena de carácteres)
		
    bot.send_message( cid, 'mensaje')			# Si es así contestará 'mensaje'
    
	
#Fin lección 1 - 19/07/218

#Inicio charla 2 - 31/07/2018


  if message.text.lower().startswith('bot di'):        # Comprobamos si el texto el empieza por "bot di"
    
    cid = message.chat.id                              #Id del chat
    mensaje=message.text                               #Mensaje completo

    respuesta = ' '.join(mensaje.split(" ")[2:])       #Respuesta = el texto que venga detrás de bot di.
						       #Ejemplo bot di hola. Con este código se guardará el "hola" porque se guardará
						       # todo lo que se escriba a partir del tercer espacio.
			
    bot.send_message(cid, respuesta)                   #El bot envía la respuesta



#Respuesta a la entrada de un usuario al grupo 
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                    #Id del chat
    cname = m.chat.title                               #Nombre del grupo
    bienvenida = ""                                    #Variable dónde guardaremos el mensaje de bienvenida
    
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
 
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
