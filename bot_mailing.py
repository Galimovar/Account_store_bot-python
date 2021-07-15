#mailing sending messages from the bot to users
import telebot
import time
from telebot import types

#telegram token to access the HTTP API
token = "1000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAexample"
bot = telebot.TeleBot(token)

#where data is stored
primary_chat_id = 1111111111

#mailing sending messages from the bot to users
def mailing():
    # read list of user IDs
    msg = bot.forward_message(chat_id=primary_chat_id, from_chat_id=primary_chat_id, message_id=6)
    bot.delete_message(chat_id=primary_chat_id, message_id=msg.message_id)
    msg = msg.text
    # mailing message from *txt file
    st = open("E:/bot_mailing_text.txt", "r", encoding="utf-8")
    st1 = st.read()
    j = ""
    for i in msg:
        if (i != ","):
            j = j + i
        else:
            try:
                keyboard = types.InlineKeyboardMarkup()
                continue_button = types.InlineKeyboardButton(text="Продолжить", callback_data="mainmenu")
                keyboard.row(continue_button)
                bot.send_message(chat_id=j, text=st1, reply_markup=keyboard)
                time.sleep(0.04)
                print('id=', j, " success")
                j = ""
            except Exception as ex:
                print('id=', j, " failed")
                j = ""

def answer():
    print('Рассылка будет производится из текстового документа E:/bot_mailing_text.txt\nЧто бы продолжить введите - yes')
    a = str(input())
    if (a != 'yes'):
        answer()
    else:
        mailing()

answer()
print('END')
input()







