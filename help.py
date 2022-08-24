from telebot.types import *

helpDict = {
    '/help': ('''
Синтаксис: 
    <arg> - обязательный аргумент с названием arg
    <arg>? - необязательный аргумент с названием arg
    <args>* - произвольное количество аргументов
    arg[str] - аргумент-список в формате [arg1,arg2,...] (без пробелов)
    arg(num) - числовой аргумент
    arg(int) - целочисленный аргумент
    arg1|arg2 - Один из 2 вариантов
Для вызова подробной справки по команде вызовите её без аргументов (например /echo)
/help - Возвращает общую справку
/echo <text>* - Повторяет введённый text
/plot <args>* - Строит график по указанным параметрам. /plot для подробностей
''', ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("/help"),KeyboardButton("/echo"),KeyboardButton("/plot"))),

'/echo': ('Повторяет любой введённый текст. Например "/echo Случайный текст" вернёт "Случайный текст" ',
          None),
'/plot': ('''Строит график или схему по указанным параметрам
/plot points xs[num] ys[num] - Строит линию соединяющую указанные точки, например /plot points [1,5,7,1] [6,3,8,6] построит треугольник''',
          ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/plot points')))
}

def gethelp(command):
    if command in helpDict: return helpDict[command]
    return helpDict['/help']
