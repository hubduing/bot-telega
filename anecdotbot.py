import random
import telebot
import time


# Токен, который выдает @botfather
bot = telebot.TeleBot('5050991282:AAFuc0r25hKOosChdoU4F2dKY49XOCNvMsY')


# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@nedo_anecdot'


# Загружаем список шуток
f = open('data/anecdots.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()


# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(2)


bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")