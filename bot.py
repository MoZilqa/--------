import telebot
from random import *

bot=telebot.TeleBot("8135763668:AAHUsBHw5hhJG71O2x45Hiz0vYTX5T_p6a8")
file=open('ic.txt', 'rb')
x=file.readline()
a=[x for x in file]


@bot.message_handler(commands=['SWAGA'])
def main(message):
    bot.send_message(message.chat.id, choice(a))

bot.polling(none_stop=True)