import telebot
import threading
import datetime
import time
import os

from telebot.types import ReplyKeyboardMarkup,KeyboardButton

import help

import mathplot

print('Я родился')
bot = telebot.TeleBot(os.environ['TOKEN'])
mainmarkup = ReplyKeyboardMarkup(resize_keyboard=True)
mainmarkup.add(KeyboardButton("/help"),KeyboardButton("/echo"),KeyboardButton("/plot"))
@bot.message_handler(content_types=["text"])
def handle_text(message):
    command = message.text.split()
    print(message.chat)
    match command:
        case command,:  # Любая команда без аргументов автоматически вызывает справку, для релизации другой логики пишите её выше этой строки
            bot.send_message(message.chat.id, help.gethelp(command),reply_markup=mainmarkup)
        case '/echo', *t:
            bot.send_message(message.chat.id, ' '.join(t),reply_markup=mainmarkup)
        case '/plot', *t:
            bot.send_photo(message.chat.id, mathplot.makeplot(*t),reply_markup=mainmarkup)


bot.polling(none_stop=True, interval=0)
