import telebot

bot = telebot.TeleBot('1787990663:AAEIJyghW9vUhp5x9qpnk22OBu4rtdkCnyY')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'test')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Я хз!')

bot.polling(none_stop=True)