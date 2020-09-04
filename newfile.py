from telegram.ext import Updater, MessageHandler,Filters

def echo(update,context):
 update.message.reply_text(
 update.message.text
 )

updater = Updater('1094960117:AAGPhTxUnFMN1mPAer-YCBNPEYJ95RqRUsw',use_context=True)

updater.dispatcher.add_handler(
MessageHandler(
Filters.text,echo)
)

updater.start_polling( )
updater.idle( )