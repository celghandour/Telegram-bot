
#Echo

from telegram.ext import Updater, MessageHandler, Filters



updater = Updater(token="1253254814:AAFlzuRtLylHykSZ0kK0LGFm9TDjoWJ164g")
dispatcher = updater.dispatcher


def echo(bot, update):

    if "hello" in update.message.text:
     bot.send_message(chat_id=update.message.chat_id,
                     text="Hello,how are you baby ?!")
    elif "love" in update.message.text:
        bot.send_message(chat_id=update.message.chat_id,
                         text="I mooooouuuuuuut 3likkkkk my Sghikiwta")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text="nti Basslaaaaa ?! ")

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
