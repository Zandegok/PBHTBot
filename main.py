from argparse import ArgumentError

import telebot
import threading
import datetime
import time
import os

from telebot.types import CallbackQuery, Message

import markups

import help

import mathplot

print('Я родился')
bot = telebot.TeleBot(os.environ['TOKEN'])

dataParser = None


def defaultDataParser(command, message):
    global dataParser
    match command:
        case '/start',:
            bot.send_message(message.chat.id, 'Добро пожаловать!\nВыбери любую кнопку',
                             reply_markup=markups.MainMarkup().to_json())
        case '/help',:
            bot.send_message(message.chat.id, 'Просто жмякай на кнопки, пока не получится',
                     reply_markup=markups.MainMarkup().to_json())
        case '/echo', *t:
            bot.send_message(message.chat.id, ' '.join(t),
                             reply_markup=markups.MainMarkup().to_json())
        case '/plot',:
            bot.send_message(message.chat.id, 'Добро пожаловать в мастер построения графиков!',
                             reply_markup=markups.PlotMarkup().to_json())
        case '/plot', 'points':
            bot.send_message(message.chat.id, 'Введите координаты x, а затем y, Например: \n1 5 10 1\n2 8 4 2')

            def plotPoints(command, message):
                global dataParser
                if command == '/start':
                    bot.send_message(message.chat.id, 'Добро пожаловать!\nВыбери любую кнопку',
                                     reply_markup=markups.MainMarkup().to_json())
                    dataParser = None
                try:
                    cords = list(map(float, command))
                    xs = cords[:len(cords) // 2]
                    ys = cords[len(cords) // 2:]
                    bot.send_photo(message.chat.id, mathplot.makeplotByPoints( xs, ys),
                                   reply_markup=markups.PlotMarkup().to_json())
                    dataParser = None
                except Exception:
                    bot.send_message(message.chat.id, 'Добро пожаловать!\nВыбери любую кнопку',
                                     reply_markup=markups.MainMarkup().to_json())
                    dataParser = None

            dataParser = plotPoints

        case '/plot', *t:
            bot.send_photo(message.chat.id, mathplot.makeplot(*t),
                           reply_markup=markups.PlotMarkup().to_json())


@bot.callback_query_handler(func=lambda call: True)
@bot.message_handler(content_types=["text"])
def handle_text(data):
    global dataParser
    match data:
        case CallbackQuery() as query:
            message = query.message
            message.text = query.data
        case Message() as message:
            pass
        case _:
            raise ArgumentError
    command = message.text.split()
    print(message)
    if not dataParser:
        dataParser = defaultDataParser
    dataParser(command, message)


bot.polling(none_stop=True, interval=0)
