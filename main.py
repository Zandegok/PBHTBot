import telebot

print('Я родился')
bot = telebot.TeleBot('5679403254:AAEijeWHM9ub9MxaTRuhFrL5iIFj4Tjlp_I')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    command = message.text.split()
    match command:
        case '/echo', *t:
            bot.send_message(message.chat.id, ' '.join(t))


bot.polling(none_stop=True, interval=0)
