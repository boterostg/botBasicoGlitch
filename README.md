# BOT BÁSICO PARA TELEGRAM 

## Este bot esta hecho en Python3 para mostrar ejemplos de funciones de bots de Telegram.

## 1.- Primero de todo leed el tutorial que está explicado aquí -> http://telegra.ph/Creando-Bots-en-Telegram-06-09

## 2.- Si habéis leído la explicación y habéis seguido todos los pasos ya podéis mirar el glitch del bot: (Donde realmente está el ejemplo entero) : entrad en este enlace https://glitch.com/~botbasico y luego pinchad en View Source para ver el proyecto bot y meter las funciones que hay de ejemplo y adaptarlas a vuestro bot :D

## 3.- Documentación: TELEGRAM BOT API (aquí está toda la información que se necesita para añadir funcionalidades a un bot): https://core.telegram.org/bots/api

## 4.- Las funcionalidades del bot están en bot.py  -> https://github.com/boterostg/botBasicoGlitch/blob/master/bot.py y en https://glitch.com/~botbasico

## Este proyecto surge del grupo de Telegram http://t.me/boterostg . Dado que hay mucha gente con ganas de aprender, hemos decidido crear un bot desde cero con https://glitch.com/ y Python3. Se utilizará el bot como ejemplo mientras se dan clases/charlas y poco a poco irá aumentando el código de dicho bot. Cualquier duda sobre el código o gente interesada en colaborar solo tiene que entrar al grupo :)

## Esto es posible gracias a https://github.com/sanguchi que creó toda la estructura del proyecto y el siguiente tutorial de como utilizarlo: http://telegra.ph/Creando-Bots-en-Telegram-06-09

## [1] Primera clase 19/07/2018 Explicación de como utilizar glitch, bot reply y bot send message:
   
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
