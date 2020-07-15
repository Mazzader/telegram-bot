from telegram import Bot
from telegram import Update
from telegram import ReplyKeyboardRemove
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, ReplyKeyboardMarkup,InlineKeyboardMarkup
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import ConversationHandler
from telegram.utils.request import Request
from logging import getLogger
from db import init_db
from db import add_message
from buttons import keyboard_back
from db import list_messages
from db import delete_from_db
from buttons import get_base_reply_keyboard

ITEM_NAME,ITEM_PRICE,ITEM_CITY,ITEM_STATE, CONFIRMATION = range(5)
need_to_database = []

def run_the_backward(update, context):
    pass


def catch_item_name(update, context):
    text = update.message.text
    need_to_database.append(text)
    update.message.reply_text('pls send me price')
    return ITEM_PRICE


def catch_item_price(update, context):
    text = update.message.text
    need_to_database.append(text)
    update.message.reply_text(
        'pls send me item City')
    return ITEM_CITY


def catch_item_city(update, context):
    text = update.message.text
    need_to_database.append(text)
    update.message.reply_text(
        'pls send me item state')
    return ITEM_STATE


def catch_item_state(update, context):
    text = update.message.text
    need_to_database.append(text)
    update.message.reply_text(
        'pls send me item category')
    return CONFIRMATION


def add(update, context):
    update.message.reply_text("Would you like to add new item to menu?")
    return ITEM_NAME

def keyboard_callback_handler(bot: Bot, update: Update, chat_data=None, **kwargs):
    query = update.callback_query
    data = query.data

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == 'yes':
        return ITEM_NAME


def cancel(update, context):
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def start(update, context):
    update.message.reply_text('Hi, choose a command that you need', reply_markup=get_base_reply_keyboard())

def edit(update, context):
    pass


def search(update, context):
    pass

def view(update, context):
    items = list_messages()
    for item in items:
        update.message.reply_text('item id: '+str(item[0])+'\n'+'item name: '+item[1]+'\n'+'item price: '+item[2]+
                                  '\n'+'item city: '+item[3]+'\n'+'item state: '+item[4]+'\n'+'item category: '+item[5])
def try_fix(update, context):
    text = update.message.from_user
    text.split()
    print(text)
    delete_from_db(text)
    update.message.reply_text('sucsess')

def delete(updater, context):
    updater.message.reply_text('Send id that object you want to delete')



def catch_item_category(update, context):
    text = update.message.text
    need_to_database.append(text)
    add_message(item_name=need_to_database[0], item_price=need_to_database[1],
                item_city=need_to_database[2], item_state=need_to_database[3],
                item_category=need_to_database[4])
    need_to_database.clear()
    update.message.reply_text('sucess')
    return ConversationHandler.END


def main():
    req = Request(
        connect_timeout=0.5,
        read_timeout=1.0,
    )
    bot = Bot(
        token=TOKEN,
        request=req,
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add)],

        states={

            ITEM_NAME: [MessageHandler(Filters.text, catch_item_name)],

            ITEM_PRICE: [MessageHandler(Filters.text, catch_item_price)],

            ITEM_CITY: [MessageHandler(Filters.text, catch_item_city)],

            ITEM_STATE: [MessageHandler(Filters.text, catch_item_state)],
            
            CONFIRMATION: [MessageHandler(Filters.text, catch_item_category)]

        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )
    updater.dispatcher.add_handler(conv_handler)
    updater.dispatcher.add_handler(CommandHandler('start',start))
    updater.dispatcher.add_handler(CommandHandler('view',view))
    updater.dispatcher.add_handler(CommandHandler('add', add))
    updater.dispatcher.add_handler(CommandHandler('edit', edit))
    updater.dispatcher.add_handler(CommandHandler('search', search))
    updater.dispatcher.add_handler(CommandHandler('delete', delete))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
	main()
