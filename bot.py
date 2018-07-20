import telebot
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN'])

bot_text = '''
Howdy, how are you doing?
Source code on https://glitch.com/~{}
'''.format(environ['PROJECT_NAME'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, bot_text)

  
@bot.message_handler(commands=['ayuda'])
def ayuda(message):
	bot.reply_to(message, 'ahora mismo te ayudo')
  

  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  cid = message.chat.id
  
  if message.text.lower() == "holi":
    username = message.from_user.username
    id = message.from_user.id
    cid = message.chat.id
    
    nombre = message.from_user.first_name
    
    bot.send_message(cid, 'holi ' + nombre + '\n cvcvhxcvjhoxjhnocvnkl')
    
    bot.send_message( cid, str(message))

    if id == 239822769:
        bot.send_message( cid, 'Hola mi creador 😙')
        
    elif id == 115659666 :
      bot.send_message( cid, 'Holi rocio')
      bot.send_message( 115659666, 'Holi manuel')
      
    elif id == 270803389 :
      bot.send_message( cid, 'Holi manuel')
      bot.send_message( 270803389, 'Holi manuel')
      
    
    elif id == 366380917:
      bot.send_message(cid, 'hola yael')

    else:
      
       bot.send_message( cid, 'No estas registrado')
  
  if message.text.lower() == "mensaje":
    bot.send_message( cid, str(message))
    
    
  if message.text.lower() == "minion":
    cid = message.chat.id
    
    bot.send_message(cid, 'minion')
    bot.send_photo( cid, open( 'assets/minionglitch.jpg', 'rb'))
  
  
  
  
  
  
  
  
  
  
  
  
  
bot.set_webhook("https://{}.glitch.me/{}".format(environ['PROJECT_NAME'], environ['TELEGRAM_TOKEN']))