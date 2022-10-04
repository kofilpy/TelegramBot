import COVID19Py
import telebot


bot = telebot.TeleBot("5710841632:AAGkQBFCgmbF_a3tey6VmmvzVEuMhXx5tiM")


@bot.message_handler(commands=['start'])
def start(message: telebot.types.ChatMemberUpdated):
    send_mess = f"Привіт, <b>{message.from_user.username}!</b>\nВведіть країну"
    bot.send_message(message.chat.id, send_mess, parse_mode='html')


bot.polling(none_stop=True)


# covid19 = COVID19Py.COVID19()
#
# latest = covid19.getLatest()

