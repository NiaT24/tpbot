import telebot
import config
import json

bot = telebot.TeleBot(config.token)
with open("TP.json", "r", encoding="utf-8") as file:
    tp = json.load(file)

@bot.message_handler(commands=['start'])
def welcome_start(message):
    bot.send_message(message.chat.id, 'Приветствую тебя, ' + message.from_user.first_name + ', отправь номер ТП и я покажу ее на карте')

@bot.message_handler(commands=['help'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Отправьте номер ТП')

@bot.message_handler(content_types=["text"])
def text(message):
    k=0
    ntp = message.text
    if ntp.isdigit():
        for i in tp:
            if i['ID'] == int(message.text):
                if i['LAT'] == 52.28 and i['LON'] == 76.93:
                    k = 0
                else:
                    k = 1
                    LAT = i['LAT']
                    LON = i['LON']
                    TYPE = i['TYPE']
        if k == 1:
            bot.send_message(message.from_user.id, 'У меня есть запись о ' + TYPE + '  № ' + ntp)
            bot.send_location(message.from_user.id, LAT, LON)
            k = 0
        else:
            bot.send_message(message.from_user.id, 'У меня нет записи о ТП/КТП  № ' + ntp)
    else:
        bot.send_message(message.from_user.id, 'Введите целое число!')

bot.polling()