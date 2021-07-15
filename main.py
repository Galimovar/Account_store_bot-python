import telebot
import constant
import random
import requests
from datetime import datetime, date, time, timedelta
from telebot import types

bot = telebot.TeleBot(constant.token)

#restart button output
def add_replykeyboard(message):
    user_markup = types.ReplyKeyboardMarkup(True, False)
    user_markup.row('🔄 Начать сначала')
    bot.send_message(chat_id=message.chat.id, text="Магазин аккаунтов Facebook и Google", reply_markup=user_markup)

#keyboard of main menu
def mainmenu_inline(message):
    keyboard_main = types.InlineKeyboardMarkup()
    choose_button = types.InlineKeyboardButton(text="Аккаунты", callback_data="choose")
    info_button = types.InlineKeyboardButton(text="Info", callback_data="info")
    support_button = types.InlineKeyboardButton(text='Поддержка', url=constant.support_name)
    faq_button = types.InlineKeyboardButton(text="Инструкция", callback_data="faq")
    keyboard_main.row(choose_button).row(info_button).row(faq_button).row(support_button)
    sst = str(
        "Добро пожаловать в бот по проддаже аккунтов Facebook и Google")
    bot.send_message(message.chat.id, text=sst, reply_markup=keyboard_main, parse_mode='MarkdownV2')


#invalid value message facebook
def invalid_value_facebook(message):
    keyboard_facebook = types.InlineKeyboardMarkup(row_width=1)
    st_fbru50 = "Facebook 🇷🇺RU50$ пак 10шт. = {0}руб".format(constant.fbru50_rub_sum)
    st_fbua50 = "Facebook 🇺🇦UA50$ пак 10шт. = {0}руб".format(constant.fbua50_rub_sum)
    st_fbgb250 = "Facebook 🇬🇧GB250$ пак 10шт. = {0}руб".format(constant.fbgb250_rub_sum)
    st_fbusa250 = "Facebook 🇺🇸USA250$ пак 10шт. = {0}руб".format(constant.fbusa250_rub_sum)
    fbru50_button = types.InlineKeyboardButton(text=st_fbru50,
                                               callback_data="fbru50")
    fbua50_button = types.InlineKeyboardButton(text=st_fbua50,
                                               callback_data=" fbua50")
    fbgb250_button = types.InlineKeyboardButton(text=st_fbgb250,
                                                callback_data="fbgb250")
    fbusa250_button = types.InlineKeyboardButton(text=st_fbusa250,
                                                 callback_data="fbusa250")
    choose_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="choose")
    keyboard_facebook.add(fbru50_button, fbua50_button, fbgb250_button, fbusa250_button, choose_button)
    st = str(
        "Выберите аккаунты\n\n\*Текстовый блок информации об аккаунтах\n\nlog:pass:useragent:\{json\_cookie\}:mail:pass")
    st1 = ("_Число некорректное, попробуйте еще раз\!:_\n\n")
    st1 = st1 + st
    bot.send_message(chat_id=message.chat.id,
                     text=st1,
                     reply_markup=keyboard_facebook, parse_mode='MarkdownV2')

#invalid value message google
def invalid_value_google(message):
    keyboard_facebook = types.InlineKeyboardMarkup(row_width=1)
    st_ggworld = "Google 🌏World пак 10шт. = {0}руб".format(constant.ggworld_rub_sum)
    st_ggeu = "Google 🇪🇺EU пак 10шт. = {0}руб".format(constant.ggeu_rub_sum)
    st_ggusatop = "Google 🇺🇸USA top пак 10шт. = {0}руб".format(constant.ggusatop_rub_sum)
    ggworld_button = types.InlineKeyboardButton(text=st_ggworld, callback_data="ggworld")
    ggeu_button = types.InlineKeyboardButton(text=st_ggeu, callback_data="ggeu")
    ggusatop_button = types.InlineKeyboardButton(text=st_ggusatop,
                                                 callback_data="ggusatop")
    choose_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="choose")
    keyboard_facebook.add(ggworld_button, ggeu_button, ggusatop_button, choose_button)
    st = str("Выберите аккаунты\n\n*Текстовый блок информации об аккаунтах\n\n*Описание особеноостей аккаунтов")
    st1 = ("_Число некорректное, попробуйте еще раз\!:_\n\n")
    st1 = st1 + st
    bot.send_message(chat_id=message.chat.id,
                     text=st1,
                     reply_markup=keyboard_facebook, parse_mode='MarkdownV2')

#cost calculation
def pay(message, quantity, rub_sum, invalid_value):
    chat_id = message.chat.id
    text2 = message.text
    j = 0
    i = 0
    j2 = 0
    try:
        i = int(text2)
        j = 1
    except Exception:
        pass
    try:
        quant = int(quantity)
        j2 = 1
    except Exception:
        pass
    if (j == 1 and i >= 1 and i <= quant and j2 == 1):
        global q
        q = int(text2)
        q = q * rub_sum
        keyboard = types.InlineKeyboardMarkup()
        payqiwi_button = types.InlineKeyboardButton(text="оплатить Qiwi", callback_data="payqiwi")
        paybtc_button = types.InlineKeyboardButton(text="оплатить Btc", callback_data="paybtc")
        mainmenu_button = types.InlineKeyboardButton(text="◀️ Главное меню", callback_data="mainmenu")
        keyboard.row(payqiwi_button, paybtc_button).row(mainmenu_button)
        st = str("Итого стоимость:\n`{0}`руб\n\n_Выберите способ оплаты:_".format(q))
        msg = bot.send_message(chat_id, text=st, reply_markup=keyboard, parse_mode='MarkdownV2')
    else:
        invalid_value(message)

#read number of accounts
def read_quantity(id):
    msg = bot.forward_message(chat_id=constant.primary_chat_id, from_chat_id=constant.primary_chat_id, message_id=id)
    bot.delete_message(chat_id=constant.primary_chat_id, message_id=msg.message_id)
    return msg.text

#next step handler, after input quantity fbru50
def pay_fbru50(message):
    pay(message, quant_fbru50, constant.fbru50_rub_sum, invalid_value_facebook)

#next step handler, after input quantity fbua50
def pay_fbua50(message):
    pay(message, quant_fbua50, constant.fbua50_rub_sum, invalid_value_facebook)

#next step handler, after input quantity fbgb250
def pay_fbgb250(message):
    pay(message, quant_fbgb250, constant.fbgb250_rub_sum, invalid_value_facebook)

#next step handler, after input quantity fbusa250
def pay_fbusa250(message):
    pay(message, quant_fbusa250, constant.fbusa250_rub_sum, invalid_value_facebook)

#next step handler, after input quantity ggworld
def pay_ggworld(message):
    pay(message, quant_ggworld, constant.ggworld_rub_sum, invalid_value_google)

#next step handler, after input quantity ggeu
def pay_ggeu(message):
    pay(message, quant_ggeu, constant.ggeu_rub_sum, invalid_value_google)

#next step handler, after input quantity ggusatop
def pay_ggusatop(message):
    pay(message, quant_ggusatop, constant.ggusatop_rub_sum, invalid_value_google)

#read list of user IDs
def read_user_ids(id):
    msg = bot.forward_message(chat_id=constant.primary_chat_id, from_chat_id=constant.primary_chat_id, message_id=id)
    bot.delete_message(chat_id=constant.primary_chat_id, message_id=msg.message_id)
    return msg.text

#add unique ID
def add_new_id(message):
    m = read_user_ids(constant.buyer_IDs)
    j = ""
    n = 0
    new_id = str(message.chat.id)
    for i in m:
        if (i != ","):
            j = j + i
        else:
            if (j == new_id):
                n = n + 1
                break
            j = ""
    if n == 0:
        m = m + new_id + ","
        bot.edit_message_text(text=m, chat_id=constant.primary_chat_id, message_id=6)

#moscow time
def time():
    t1 = str(datetime.now() + timedelta(minutes=180))
    t2 = t1[-15:]
    t2 = t2[:5]
    tf = t2[:2]
    tl = t2[-2:]
    t1 = tf + "\:" + tl
    return t1

#moscow time +30m
def time210():
    t1 = str(datetime.now() + timedelta(minutes=210))
    t2 = t1[-15:]
    t2 = t2[:5]
    tf = t2[:2]
    tl = t2[-2:]
    t1 = tf + "\:" + tl
    return t1

@bot.message_handler(commands=['start'])
def handle_start(message):
    add_new_id(message)
    add_replykeyboard(message)
    mainmenu_inline(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == '🔄 Начать сначала':
        mainmenu_inline(message)

#inline keyboard
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    #return to main menu
    if call.data == "mainmenu":
        mainmenu_inline(call.message)

    #select type of accounts
    elif call.data == "choose":
        keyboard_choose = types.InlineKeyboardMarkup()
        facebook_button = types.InlineKeyboardButton(text="Facebook", callback_data="facebook")
        google_button = types.InlineKeyboardButton(text="Google", callback_data="google")
        mainmenu_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="mainmenu")
        keyboard_choose.row(facebook_button, google_button).row(mainmenu_button)
        sst = str(
            "Выберите тип аккаунтов:")
        bot.send_message(call.message.chat.id, text=sst, reply_markup=keyboard_choose, parse_mode='MarkdownV2')

    #select facebook accounts
    elif call.data == "facebook":
        keyboard_facebook = types.InlineKeyboardMarkup(row_width=1)
        st_fbru50 = "Facebook 🇷🇺RU50$ пак 10шт. = {0}руб".format(constant.fbru50_rub_sum)
        st_fbua50 = "Facebook 🇺🇦UA50$ пак 10шт. = {0}руб".format(constant.fbua50_rub_sum)
        st_fbgb250 = "Facebook 🇬🇧GB250$ пак 10шт. = {0}руб".format(constant.fbgb250_rub_sum)
        st_fbusa250 = "Facebook 🇺🇸USA250$ пак 10шт. = {0}руб".format(constant.fbusa250_rub_sum)
        fbru50_button = types.InlineKeyboardButton(text=st_fbru50,
                                                   callback_data="fbru50")
        fbua50_button = types.InlineKeyboardButton(text=st_fbua50,
                                                   callback_data=" fbua50")
        fbgb250_button = types.InlineKeyboardButton(text=st_fbgb250,
                                                    callback_data="fbgb250")
        fbusa250_button = types.InlineKeyboardButton(text=st_fbusa250,
                                                     callback_data="fbusa250")
        choose_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="choose")
        keyboard_facebook.add(fbru50_button, fbua50_button, fbgb250_button, fbusa250_button, choose_button)
        st = str("Выберите аккаунты\n\n*Текстовый блок информации об аккаунтах\n\nlog:pass:useragent:{json_cookie}:mail:pass")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                              reply_markup=keyboard_facebook)

    #select google accounts
    elif call.data == "google":
        keyboard_facebook = types.InlineKeyboardMarkup(row_width=1)
        st_ggworld = "Google 🌏World пак 10шт. = {0}руб".format(constant.ggworld_rub_sum)
        st_ggeu = "Google 🇪🇺EU пак 10шт. = {0}руб".format(constant.ggeu_rub_sum)
        st_ggusatop = "Google 🇺🇸USA top пак 10шт. = {0}руб".format(constant.ggusatop_rub_sum)
        ggworld_button = types.InlineKeyboardButton(text=st_ggworld, callback_data="ggworld")
        ggeu_button = types.InlineKeyboardButton(text=st_ggeu, callback_data="ggeu")
        ggusatop_button = types.InlineKeyboardButton(text=st_ggusatop,
                                                     callback_data="ggusatop")
        choose_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="choose")
        keyboard_facebook.add(ggworld_button, ggeu_button, ggusatop_button, choose_button)
        st = str("Выберите аккаунты\n\n*Текстовый блок информации об аккаунтах\n\n*Описание особеноостей аккаунтов")
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                              reply_markup=keyboard_facebook)

    #payment qiwi
    elif call.data == "payqiwi":
        a = random.randint(1000000, 9999999)
        idname = call.message.chat.id
        #payment comment
        com = "id:" + str(idname) + ":" + str(a)
        t180 = time()
        t210 = time210()
        qiw_url = str(
            "https://qiwi.com/payment/form/99?extra['account']={0}&amountInteger={2}&amountFraction=0&extra['comment']={1}&blocked[0]=account&blocked[1]=sum&blocked[2]=comment".format(
                constant.qiw_tel, com, q))
        qiw_keyboard = types.InlineKeyboardMarkup()
        qiw_pay_button = types.InlineKeyboardButton(text="Оплатить", url=qiw_url)
        manager_button = types.InlineKeyboardButton(text='Менеджер', url=constant.support_name)
        qiw_back_button = types.InlineKeyboardButton(text="⏹  Отмена(Главное меню)", callback_data="mainmenu")
        qiw_keyboard.row(qiw_pay_button).row(manager_button).row(qiw_back_button)
        strqiwi = "_\-Меню оплаты\-_\n\nПереведите `{3}`руб на Qiwi\-кошелек:\n`{1}`\nукажите комментарий:\n`{0}`\n" \
                  "_Либо нажмите кнопу [Оплатить]({2}) \(Данные будут заполнены автоматически\)_ \n\n".format(
            com, constant.qiw_tel, qiw_url, q)
        strqiwi2 = "Оплатите в течении 30 минут\nдо `{0}`по МСК\ncейчас `{1}` по МСК\n\n_\(После оплаты отпишите менеджеру, переслав это сообщение\)_".format(t210, t180)
        strqiwi3 = strqiwi + strqiwi2
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=strqiwi3,
                              reply_markup=qiw_keyboard, parse_mode='MarkdownV2')

    #payment bitcoin
    elif call.data == "paybtc":
        #crypto exchange public api
        url = 'https://yobit.net/api/2/btc_rur/ticker'
        response = requests.get(url).json()
        #json response parse
        price = response['ticker']['sell']
        a = (1 / price) * q
        a = round(a, 8)
        text = str(a)
        t180 = time()
        t210 = time210()
        keyboard = types.InlineKeyboardMarkup()
        manager_button = types.InlineKeyboardButton(text='Менеджер', url=constant.support_name)
        btc_back_button = types.InlineKeyboardButton(text="⏹  Отмена(Главное меню)", callback_data="mainmenu")
        keyboard.row(manager_button).row(btc_back_button)
        st = "_\-Меню оплаты\-_\n\nПереведите:`\n{1}`btc\nНа кошелек:\n`{4}`\n\nСовершите платеж" \
             " в течении 30 минут\nдо `{2}`по МСК\ncейчас `{3}` по МСК\n\nПосле пополнения отпишите [Менеджеру]({0})," \
             " переслав это сообщение".format(
            constant.support_name, a, t210, t180, constant.btc_wlt)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                              reply_markup=keyboard, parse_mode='MarkdownV2')

    elif call.data == "info":
        keyboard_personal = types.InlineKeyboardMarkup()
        mainmenu_button = types.InlineKeyboardButton(text="◀️ Назад", callback_data="mainmenu")
        support_button = types.InlineKeyboardButton(text='Поддержка', url=constant.support_name)
        keyboard_personal.row(mainmenu_button, support_button)
        st = str("Информация об аккаунте {2} {3}\n\nID - {0}\nusername - @{1}".format(
            call.message.chat.id, call.message.chat.username, call.message.chat.first_name,
            call.message.chat.last_name))
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                              reply_markup=keyboard_personal)


    elif call.data == "faq":
        st1 = "Выберите _Аккаунты_" \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st2 = "Выберите нужную позицию" \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st3 = "Укажите количество" \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st4 = "Выберите _Пополнить Qiwi_ или _BTC_" \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st5 = "Выберите _Оплатить_, либо совершите перевод самостоятельно, указав в переводе комментарий\. Для отмены выберите _Отменить оплату_\." \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st6 = "Пополните указанный Btc\-кошелек, на указанную сумму\." \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        st7 = "После проведения оплаты напишите менеджеру, переслав сообщение \-Меню Оплаты\-" \
              "\n\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-" \
              "\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-"
        try:
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img1, caption=st1, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img2, caption=st2, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img3, caption=st3, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img4, caption=st4, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img5, caption=st5, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img6, caption=st6, parse_mode='MarkdownV2')
            bot.send_photo(chat_id=call.message.chat.id, photo=constant.img7, caption=st7, parse_mode='MarkdownV2')
        except Exception:
            pass
        mainmenu_inline(call.message)

    #input quantity of fbru50
    elif call.data == "fbru50":
        global quant_fbru50
        quant_fbru50 = read_quantity(constant.fbru50)
        st = "_Facebook 🇷🇺RU50$ пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_fbru50, constant.fbru50_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_fbru50)

    #input quantity of fbua50
    elif call.data == "fbua50":
        global quant_fbua50
        quant_fbua50 = read_quantity(constant.fbua50)
        st = "_Facebook 🇺🇦UA50$ пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_fbua50, constant.fbua50_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_fbua50)

    #input quantity of fbgb250
    elif call.data == "fbgb250":
        global quant_fbgb250
        quant_fbgb250 = read_quantity(constant.fbgb250)
        st = "_Facebook 🇬🇧GB250$ пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_fbgb250, constant.fbgb250_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_fbgb250)

    #input quantity of fbusa250
    elif call.data == "fbusa250":
        global quant_fbusa250
        quant_fbusa250 = read_quantity(constant.fbusa250)
        st = "_Facebook 🇺🇸USA250$ пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_fbusa250, constant.fbusa250_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_fbusa250)

    #input quantity of ggworld
    elif call.data == "ggworld":
        global quant_ggworld
        quant_ggworld = read_quantity(constant.ggworld)
        st = "_Google 🌏World пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_ggworld, constant.ggworld_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_ggworld)

    #input quantity of ggeu
    elif call.data == "ggeu":
        global quant_ggeu
        quant_ggeu = read_quantity(constant.ggeu)
        st = "_Google 🇪🇺EU пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_ggeu, constant.ggeu_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_ggeu)

    #input quantity of ggusatop
    elif call.data == "ggusatop":
        global quant_ggusatop
        quant_ggusatop = read_quantity(constant.ggusatop)
        st = "_Google 🇺🇸USA пак 10шт\. \= {1}руб_\.\n\nОсталось \- `{0}` пак\(ов\)" \
            " \n\nВведите кол\-во пакетов аккаунтов, которое вы хотите приобрести \(от `1` до `{0}`\)".format(quant_ggusatop, constant.ggusatop_rub_sum)
        msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=st,
                                    parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, pay_ggusatop)

bot.polling(none_stop=True, interval=0)