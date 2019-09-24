# BOT BÁSICO PARA TELEGRAM 
# [GRUPO DE TELEGRAM](http://t.me/boterostg)
# [COMUNIDAD DE GITHUB](https://github.com/boterostg)
# [CLASES](https://repl.it/community/classrooms/114961)

## Este bot esta creado con Python3 con el fin de mostrar ejemplos de funciones de bots de Telegram. A continuación sigue las indicaciones:

## 1.- Primero de todo leed el tutorial que está explicado aquí -> http://telegra.ph/Creando-Bots-en-Telegram-06-09

## 2.- Si habéis leído la explicación y habéis seguido todos los pasos ya podéis mirar el glitch del bot, entrad en este enlace https://glitch.com/~botbasico y luego pinchad en View Source para ver el proyecto del bot. Podéis mirar funciones que hay de ejemplo y adaptarlas a vuestro bot :D

## 3.- Documentación: TELEGRAM BOT API (aquí está toda la información que se necesita para añadir funcionalidades a un bot): https://core.telegram.org/bots/api y aquí: https://github.com/eternnoir/pyTelegramBotAPI teneís el wrapper que se utilizará para programar este bot.

## 4.- Las funcionalidades del bot están en bot.py  -> https://github.com/boterostg/botBasicoGlitch/blob/master/bot.py y en https://glitch.com/~botbasico

## *Este proyecto surge del grupo de Telegram http://t.me/boterostg . Dado que hay mucha gente con ganas de aprender, hemos decidido crear un bot desde cero con https://glitch.com/ y Python3. Se utilizará el bot como ejemplo mientras se dan clases/charlas y poco a poco irá aumentando el código de dicho bot. Cualquier duda sobre el código o gente interesada en colaborar solo tiene que entrar al grupo http://t.me/boterostg :)

## *Esto es posible gracias a https://github.com/sanguchi que creó toda la estructura del proyecto y el siguiente tutorial de como utilizarlo: http://telegra.ph/Creando-Bots-en-Telegram-06-09

## [1] Primera clase 19/07/2018 Explicación de como utilizar glitch, comando de un bot y bot send message:

### Cómo crear tu bot y empezar con glitch:

http://telegra.ph/Creando-Bots-en-Telegram-06-09

### Ejemplo creación de un comando
```python
@bot.message_handler(commands=['start'])
def nombreComando(message):
  bot.reply_to(message, 'Has iniciado el bot')

```  
### Ejemplo respuestas bot

```python
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  if message.text.lower() == "hola":
    bot.send_message( cid, 'hola amigo')

```
## [2] Segunda clase 31/07/2018 Explicación de como utilizar split, comando de saludo, despedida y comando de la ruleta rusa en el cual se aplica random y expulsión de usuarios de un grupo.

### Ejemplo de como utilizar split

```python
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  if  message.text.lower().startswith('bot di'):                 
    mensaje=message.text                              
    respuesta = ' '.join(mensaje.split(" ")[2:])   
    bot.send_message(cid, respuesta)  
```
    
### Respuesta a la entrada de un usuario al grupo 

```python
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def command_bienvenida(m):
    cid = m.chat.id                                   
    cname = m.chat.title                              
    bienvenida = ""                                    
    
    if (m.new_chat_member.username is None):          
        nun = m.new_chat_member.first_name            
        
        if (m.new_chat_member.last_name is not None): 
            nun += " "                        
            nun += m.new_chat_member.last_name         
            
        else:                                          
            bienvenida = "Bienvenido al grupo"         
            bienvenida += str(cname)                   
            bienvenida += " "
    else:                                              
        nun = m.new_chat_member.username               
        bienvenida = "Bienvenido al grupo "            
        bienvenida += str(cname)                      
        bienvenida += " @"

    bot.send_message(cid, str(bienvenida) + str(nun))
 ```
### Respuesta a la salida de un usuario del grupo 

```python
@bot.message_handler(func=lambda message: True, content_types=['left_chat_member'])
def command_bye(m):
    cid = m.chat.id                                    
    despedida = ""                                     
    
    if (m.left_chat_member.username is None):         
        nun = m.left_chat_member.first_name           
        
        if (m.left_chat_member.last_name is not None): 
            nun += " "
            nun += m.left_chat_member.last_name       
            
    else:                                              
        nun = m.left_chat_member.username             
        despedida = "Hasta luego "                    
        despedida += " @"

    bot.send_message(cid, str(despedida) + str(nun))   
```
### Comando para simular una ruleta rusa en grupos de Telegram

```python
@bot.message_handler(commands=['ruleta'])
def ruleta(message):

  cid = message.chat.id					
  nombreUsuario = message.from_user.username		
  idUsuario = message.from_user.id			
  rnd = randrange(0, int(5))				
  if rnd == 4:						
	
    bot.send_message(cid, "Pummmm estas muerto @" + nombreUsuario )	
    bot.kick_chat_member(cid,idUsuario)					
    bot.unban_chat_member(cid, idUsuario)				

  else:								

    bot.send_message(cid, "Te has salvado amigo @" + nombreUsuario)	
```

## [3] Tercera clase 08/08/2018 Explicación de como utilizar split y random para simular un sorteo.

```python
@bot.message_handler(func=lambda message: True)		# Respuestas del bot
def echo_message(message):
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
```
