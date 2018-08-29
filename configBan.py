import json
import requests
import telebot
from telebot import *
from os import environ

bot = telebot.TeleBot(environ['TELEGRAM_TOKEN']) 

banConf = types.InlineKeyboardMarkup()
banConf.add(types.InlineKeyboardButton('Configuración Grupo', callback_data='config'))
banConf.add(types.InlineKeyboardButton('Nivel Flanders', callback_data='creador'))
banConf.add(types.InlineKeyboardButton('Configuración Flanders', callback_data='creador'))
            
            
@bot.message_handler(commands=['config'])
def start_handler(m):
  cid = m.chat.id
  bot.send_message(cid, "Vamos a configurar el grupo", reply_markup=banConf, parse_mode="Markdown")
  
  
  
  
  
  
  
  
  
  
  

