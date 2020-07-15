from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton

BUTTON1_VIEW = '/view'
BUTTON2_ADD = '/add'
BUTTON3_EDIT = '/edit'
BUTTON4_SEARCH = '/search'
BUTTON5_DELETE = '/delete'
BUTTON6_BACK_TO_START = 'Back to start'
BUTTON7_BACK_TO_STEP_ONE = 'Back to step one'
BUTTON8_BACK_TO_STEP_TWO = 'Back to step two'
BUTTON9_BACK_TO_STEP_THREE = 'Back to step three'
BUTTON10_BACK_TO_STEP_FOUR = 'Back to step four'
BUTTON11_BACK_TO_STEP_FIVE = 'Back to step five'

def get_base_reply_keyboard():
    keyboard = [
        [
        KeyboardButton(BUTTON1_VIEW),
        KeyboardButton(BUTTON2_ADD),
            ],
        [
        KeyboardButton(BUTTON3_EDIT),
        KeyboardButton(BUTTON4_SEARCH),
        KeyboardButton(BUTTON5_DELETE),
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard,resize_keyboard=True)

def keyboard_back():
    keyboard = [InlineKeyboardButton(BUTTON6_BACK_TO_START, callback_data='m1')]
    return InlineKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)