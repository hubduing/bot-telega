# 2) Wikipedia bot
import wikipedia, telebot, re


# Создаем экземпляр бота
bot = telebot.TeleBot('5050991282:AAFuc0r25hKOosChdoU4F2dKY49XOCNvMsY')


# Устанавливаем язык
wikipedia.set_lang('ru')


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        firstpage = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = firstpage.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikisubtext = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for state in wikimas:
            if not ('==' in state):
                # Если в строке осталось больше трех символов, добавляем ее к нашей 
                # переменной и возвращаем утерянные при разделении строк точки на место
                if(len(state.strip())>3):
                    wikisubtext=wikisubtext + state + '.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikisubtext=re.sub('\([^()]*\)', '', wikisubtext)
        wikisubtext=re.sub('\([^()]*\)', '', wikisubtext)
        wikisubtext=re.sub('\{[^\{\}]*\}', '', wikisubtext)
        # Возвращаем текстовую строку
        return wikisubtext
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')


# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)