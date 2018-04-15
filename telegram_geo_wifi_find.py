# -*- coding: utf-8 -*-
import telebot
from telebot import types
from geo_search import geo_search


bot = telebot.TeleBot('590072429:AAEjBUB5fzgp29oDsEcbhQYzvnJ6tHgNDrQ')

locate = {}

@bot.message_handler(commands=["geo"])
def geophone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Отправь мне свое местоположение и я попробую найти пароли от wifi которые рядом с тобой", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def locate(message):
    loc = message.location
    lon2 = round(float(loc.longitude), 5)
    lan2 = round(float(loc.latitude), 5)
    lon1 = round(float(lon2 - 0.001), 5)
    lan1 = round(float(lan2 - 0.001), 5)
    bot.send_message(message.chat.id, 'Подождите немного')
    
    mesg = geo_search(lan1,lan2,lon1,lon2)
    
    bot.send_message(message.chat.id , mesg)
    
@bot.message_handler(commands=['start', 'Start'])
def send_welcome(message):
        bot.send_message(message.chat.id, 'Привет я ищу пароли от wifi по твоему местоположению,' + '\n' + 'для поиска отправь /geo')


@bot.message_handler(commands=['help', 'Help'])
def send_help(message):
        bot.send_message(message.chat.id,'Для поиска паролей от wifi отправь мне свое местоположение с помощью команды /geo и подтверди отправку своего местополжения.' + '\n' + '\n' + 'Ищу с помощью сайта 3wifi.stascorp.com')


  
        
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)