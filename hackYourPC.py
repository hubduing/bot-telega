# 5050991282:AAFuc0r25hKOosChdoU4F2dKY49XOCNvMsY

# 1) Echo bot - easy
import telebot


# Создаем экземпляр бота
bot = telebot.TeleBot("5050991282:AAFuc0r25hKOosChdoU4F2dKY49XOCNvMsY")
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали ' + message.text)


bot.polling(non_stop=True, interval=0)