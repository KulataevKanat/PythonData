import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_msg(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('Hello')
    markup.row('World')
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)
