import telebot			#Importaciones
from os import environ		

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN']) #Token del bot 

# Variable que se utilizará en el comando /start para enviarlo como el texto del mensaje del bot
bot_text = '''				
Howdy, how are you doing?
Source code on https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

# Inicio lección 1- 19/07/2018

@bot.message_handler(commands=['start', 'help']) # Comando /start o /help . Cuando un usuario escriba cualquiera de las dos, respondera a su mensaje con
def send_welcome(message):			 # el mensaje escrito en la variable más arriba declarada.
	bot.reply_to(message, bot_text)

  
@bot.message_handler(commands=['ayuda'])		# Ejemplo de comando /ayuda que en vez de pasarle una variable, directamente escribimos 
def ayuda(message):					
	bot.reply_to(message, 'ahora mismo te ayudo')	# el bot responde 'ahora mismo te ayudo' al mensaje
  

  
@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
  cid = message.chat.id 				# guardamos en al variale cid el id de el mensaje recibido 
  
  if message.text.lower() == "holi":			#comparamos el texto el mensaje si es igual a 'holi'
   
    id = message.from_user.id				#guardamos en una variable el id del usuario que envió el mensaje			
    
    nombre = message.from_user.first_name		#guardamos en una variable el nombre del usuario que envió el mensaje
    
    bot.send_message(cid, 'holi ' + nombre )		# el bot responde 'holi' y después el nombre del usuario que guardamos en la variable da arriba
   

    if id == 239822769:					#comparamos el id guardado del usuario con un id que le hemos pasado
		
        bot.send_message( cid, 'Hola mi creador 😙')	# si es igual responde el mensaje que hemos introducido al chat indicado
        
    elif id == 270803389 :				# en este caso el id lo comparamos con otra id diferente 
	
      bot.send_message( cid, 'Holi manuel')		# aquí envia al chat que le hemos hablado 'Holi manuel'

      bot.send_message( 115659666, 'Holi manuel')	#aquí probamos a pasarle en vez de cid un id de un usuario y le enviará el mensaje por mensaje 
							#privado

    else:						# si no se da ninguno de los resultados de arriba hará lo siguiente
      
       bot.send_message( cid, 'No estás registrado')	# enviará por el chat el mensaje 'No estás registrado'
  
  if message.text.lower() == "mensaje":			# aquí probamos un if comparandolo con un String(una cadena de carácteres
		
    bot.send_message( cid, 'mensaje')			# si es así contestará 'mensaje'
    
	
#Fin lección 1 - 19/07/218
  
  
  
  
  
  
  
  
  
  
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))
