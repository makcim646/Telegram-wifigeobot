# -*- coding: utf-8 -*-
import telebot
from telebot import types
import requests
from geo_search import wifi_search

bot = telebot.TeleBot('you token')

locate = {}

@bot.message_handler(commands=["geo"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Отправь мне свое местоположение и я попробую найти пароли от wifi которые рядом с тобой", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def locate(message):
    bot.send_message(message.chat.id, 'Подождите немного')
    locate = str(message.location)
    lon2 = float(locate[13:21])
    lan2 = float(locate[36:44])
    lon1 = float(lon2 - 0.001)
    lan1 = float(lan2 - 0.001)
    
    msg = wifi_search(lan1,lan2,lon1,lon2)
    
    bot.send_message(message.chat.id, msg)
    
    
    
@bot.message_handler(commands=['start', 'Start'])
def send_welcome(message):
        bot.send_message(message.chat.id, 'Привет я ищу пароли от wifi по твоему местоположению,' + '\n' + 'для поиска отправь /geo' + '\n' + '\n' + 'Ищу с помощью сайта 3wifi.stascorp.com')




  
        
bot.polling(none_stop=True)