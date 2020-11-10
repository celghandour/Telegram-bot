#Echo

from telegram.ext import Updater, MessageHandler, Filters

updater = Updater(token="ffffffff")
dispatcher = updater.dispatcher


def echo(bot, update):

    if "Hello" in update.message.text:
     bot.send_message(chat_id=update.message.chat_id,
                     text="Hello,how are you man  ?!")

    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text=" ?! ")

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
