import telebot
import threading
import datetime
import time
import os
print('Я родился')
bot = telebot.TeleBot(os.environ['TOKEN'])
# timeManagers = eval(open('docs/time managers').read())


# def checkTime():
#     b = False
#     while True:
#         if datetime.datetime.now().second.real == 0 and not b:
#             for chatid in timeManagers:
#                 bot.send_message(chatid, 'Начало минуты:' + str(datetime.datetime.now()))
#             b = True
#         if datetime.datetime.now().second.real == 30 and b:
#             for chatid in timeManagers:
#                 bot.send_message(chatid, 'Середина минуты:' + str(datetime.datetime.now()))
#             b = False
#
#
# threading.Thread(target=checkTime, args=(), name='Timer').start()


@bot.message_handler(content_types=["text"])
def handle_text(message):
    command = message.text.split()
    print(message.chat)
    match command:
        # case '/start'|'/help':
        case '/echo', *t:
            bot.send_message(message.chat.id, ' '.join(t))
        # case '/timemanage', 'on':
        #     timeManagers.append(message.chat.id)
        #     open('docs/time managers', 'w').write(str(timeManagers))
        #     bot.send_message(message.chat.id,'Менеджмент времени подключён')
        # case '/timemanage', 'off':
        #     timeManagers.remove(message.chat.id)
        #     open('docs/time managers', 'w').write(str(timeManagers))
        #     bot.send_message(message.chat.id, 'Менеджмент времени отключён')


bot.polling(none_stop=True, interval=0)
