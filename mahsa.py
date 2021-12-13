import os
import telebot
from fuzzywuzzy import fuzz


# Создаем бота, пишем свой токен
bot = telebot.TeleBot('5050991282:AAFuc0r25hKOosChdoU4F2dKY49XOCNvMsY')


# Загружаем список фраз и ответов в массив
mass = []
if os.path.exists('data/boltun.txt'):
    f=open('data/boltun.txt', 'r', encoding='UTF-8')
    for line in f:
        if(len(line.strip()) > 2):
            mass.append(line.strip().lower())
    f.close()
    

# С помощью fuzzywuzzy вычисляем наиболее похожую фразу и выдаем в качестве ответа следующий элемент списка
def answer(text):
    try:
        text=text.lower().strip()
        if os.path.exists('data/boltun.txt'):
            a = 0
            n = 0
            nn = 0
            for q in mass:
                if('u: ' in q):
                    # С помощью fuzzywuzzy получаем, насколько похожи две строки
                    aa=(fuzz.token_sort_ratio(q.replace('u: ',''), text))
                    if(aa > a and aa!= a):
                        a = aa
                        nn = n
                n = n + 1
            s = mass[nn + 1]
            return s
        else:
            return 'Ошибка'
    except:
        return 'Ошибка'


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне Привет )')


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def handle_message(message):
    # Запись логов
    f=open('data/' + str(message.chat.id) + '_log.txt', 'a', encoding='UTF-8')
    s=answer(message.text)
    f.write('u: ' + message.text + '\n' + s +'\n')
    f.close()
    # Отправка ответа
    bot.send_message(message.chat.id, s)
# Запускаем бота
bot.polling(none_stop=True, interval=0)    