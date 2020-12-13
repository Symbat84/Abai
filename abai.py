import telebot
from telebot import types

# токен-бота
bot = telebot.TeleBot('1443145963:AAFYhV8ephiDWOfVrM3QiXJuyEOQikv7MxY')


# если /help, /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! "
                     + message.from_user.first_name
                     + ", В боте можно прочитать фундаментальное произведение казахского просветителя слова назидания Абая, приятного чтения!",
                     reply_markup=markup_menu)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Слова назидания 1-15')
btn_2 = types.KeyboardButton('Слова назидания 16-30')
btn_3 = types.KeyboardButton('Слова назидания 31-45')
markup_menu.add(btn_1, btn_2, btn_3)


Abai1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a1 = types.KeyboardButton('Слова назидания 1')
btn_a2 = types.KeyboardButton('Слова назидания 2')
btn_a3 = types.KeyboardButton('Слова назидания 3')
btn_a4 = types.KeyboardButton('Слова назидания 4')
btn_a5 = types.KeyboardButton('Слова назидания 5')
btn_a6 = types.KeyboardButton('Слова назидания 6')
btn_a7 = types.KeyboardButton('Слова назидания 7')
btn_a8 = types.KeyboardButton('Слова назидания 8')
btn_a9 = types.KeyboardButton('Слова назидания 9')
btn_a10 = types.KeyboardButton('Слова назидания 10')
btn_a11 = types.KeyboardButton('Слова назидания 11')
btn_a12 = types.KeyboardButton('Слова назидания 12')
btn_a13 = types.KeyboardButton('Слова назидания 13')
btn_a14 = types.KeyboardButton('Слова назидания 14')
btn_a15 = types.KeyboardButton('Слова назидания 15')
btn_a16 = types.KeyboardButton('В меню')
Abai1.add(btn_a1, btn_a2, btn_a3, btn_a4, btn_a5, btn_a6, btn_a7, btn_a8, btn_a9, btn_a10, btn_a11, btn_a12, btn_a13, btn_a14, btn_a15, btn_a16)


Abai2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a17 = types.KeyboardButton('Слова назидания 16')
btn_a18 = types.KeyboardButton('Слова назидания 17')
btn_a19 = types.KeyboardButton('Слова назидания 18')
btn_a20 = types.KeyboardButton('Слова назидания 19')
btn_a21 = types.KeyboardButton('Слова назидания 20')
btn_a22 = types.KeyboardButton('Слова назидания 21')
btn_a23 = types.KeyboardButton('Слова назидания 22')
btn_a24 = types.KeyboardButton('Слова назидания 23')
btn_a25 = types.KeyboardButton('Слова назидания 24')
btn_a26 = types.KeyboardButton('Слова назидания 25')
btn_a27 = types.KeyboardButton('Слова назидания 26')
btn_a28 = types.KeyboardButton('Слова назидания 27')
btn_a29 = types.KeyboardButton('Слова назидания 28')
btn_a30 = types.KeyboardButton('Слова назидания 29')
btn_a31 = types.KeyboardButton('Слова назидания 30')
btn_a32 = types.KeyboardButton('В меню')
Abai2.add(btn_a17, btn_a18, btn_a19, btn_a20, btn_a21, btn_a22, btn_a23, btn_a24, btn_a25, btn_a26, btn_a27, btn_a28, btn_a29, btn_a30, btn_a31, btn_a32)


Abai3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a33 = types.KeyboardButton('Слова назидания 31')
btn_a34 = types.KeyboardButton('Слова назидания 32')
btn_a35 = types.KeyboardButton('Слова назидания 33')
btn_a36 = types.KeyboardButton('Слова назидания 34')
btn_a37 = types.KeyboardButton('Слова назидания 35')
btn_a38 = types.KeyboardButton('Слова назидания 36')
btn_a39 = types.KeyboardButton('Слова назидания 37')
btn_a40 = types.KeyboardButton('Слова назидания 38')
btn_a41 = types.KeyboardButton('Слова назидания 39')
btn_a42 = types.KeyboardButton('Слова назидания 40')
btn_a43 = types.KeyboardButton('Слова назидания 41')
btn_a44 = types.KeyboardButton('Слова назидания 42')
btn_a45 = types.KeyboardButton('Слова назидания 43')
btn_a46 = types.KeyboardButton('Слова назидания 44')
btn_a47 = types.KeyboardButton('Слова назидания 45')
btn_a48 = types.KeyboardButton('В меню')
Abai3.add(btn_a33, btn_a34, btn_a35, btn_a36,btn_a37, btn_a38, btn_a39, btn_a40,btn_a41, btn_a42, btn_a43, btn_a44,btn_a45, btn_a46, btn_a47, btn_a48)




vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Слова назидания 1-15":
        bot.reply_to(message, "Выберите номер назидания от 1-15", reply_markup=Abai1)
    if message.text == "Слова назидания 16-30":
        bot.reply_to(message, "Выберите номер назидания от 16-30", reply_markup=Abai2)
    if message.text == "Слова назидания 31-45":
        bot.reply_to(message, "Выберите номер назидания от 31-45", reply_markup=Abai3)
    if message.text == "Слова назидания 1":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B1%D1%96%D1%80%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 2":
        bot.reply_to(message, """https://www.inform.kz/kz/asyl-mura-abaydyn-ekinshi-kara-sozi_a2471636""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 3":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%AF%D1%88%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 4":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/Абайдың_қара_сөздері/Абайдың_төртінші_қара_сөзі""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 5":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B1%D0%B5%D1%81%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 6":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B0%D0%BB%D1%82%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 7":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B5%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 8":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D1%81%D0%B5%D0%B3%D1%96%D0%B7%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 9":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D1%82%D0%BE%D2%93%D1%8B%D0%B7%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 10":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 11":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D0%B1%D1%96%D1%80%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 12":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D0%B5%D0%BA%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 13":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D2%AF%D1%88%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 14":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D1%82%D3%A9%D1%80%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 15":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D0%B1%D0%B5%D1%81%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai1)
    if message.text == "Слова назидания 16":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D0%B0%D0%BB%D1%82%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 17":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D0%B6%D0%B5%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 18":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D1%81%D0%B5%D0%B3%D1%96%D0%B7%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 19":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D0%BD_%D1%82%D0%BE%D2%93%D1%8B%D0%B7%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 20":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0%D1%81%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 21":
        bot.reply_to(message, """https://kk.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D0%B1%D1%96%D1%80%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 22":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D0%B5%D0%BA%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 23":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D2%AF%D1%88%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 24":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D1%82%D3%A9%D1%80%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 25":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D0%B1%D0%B5%D1%81%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 26":
        bot.reply_to(message, """http://kitap-palatasy.kz/zhanalyktar/2056-abaydy-zhiyrma-altynshy-ara-sz.html""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 27":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D0%B6%D0%B5%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 28":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D1%81%D0%B5%D0%B3%D1%96%D0%B7%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 29":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%B6%D0%B8%D1%8B%D1%80%D0%BC%D0%B0_%D1%82%D0%BE%D2%93%D1%8B%D0%B7%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 30":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai2)
    if message.text == "Слова назидания 31":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D0%B1%D1%96%D1%80%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 32":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D0%B5%D0%BA%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 33":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D2%AF%D1%88%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 34":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D1%82%D3%A9%D1%80%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 35":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D0%B1%D0%B5%D1%81%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 36":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D0%B0%D0%BB%D1%82%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 37":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D0%B6%D0%B5%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 38":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D1%81%D0%B5%D0%B3%D1%96%D0%B7%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 39":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D0%BE%D1%82%D1%8B%D0%B7_%D1%82%D0%BE%D2%93%D1%8B%D0%B7%D1%8B%D0%BD%D1%88%D1%8B_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 40":
        bot.reply_to(message, """https://bilimdiler.kz/okushi/28273-kara-sozder-abaydyn-kyrykynshy-kara-sozi.html""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 41":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D1%8B%D1%80%D1%8B%D2%9B_%D0%B1%D1%96%D1%80%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 42":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D1%8B%D1%80%D1%8B%D2%9B_%D0%B5%D0%BA%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 43":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D1%8B%D1%80%D1%8B%D2%9B_%D2%AF%D1%88%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 44":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D1%8B%D1%80%D1%8B%D2%9B_%D1%82%D3%A9%D1%80%D1%82%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
    if message.text == "Слова назидания 45":
        bot.reply_to(message, """https://kk.m.wikibooks.org/wiki/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D0%B4%D0%B5%D1%80%D1%96/%D0%90%D0%B1%D0%B0%D0%B9%D0%B4%D1%8B%D2%A3_%D2%9B%D1%8B%D1%80%D1%8B%D2%9B_%D0%B1%D0%B5%D1%81%D1%96%D0%BD%D1%88%D1%96_%D2%9B%D0%B0%D1%80%D0%B0_%D1%81%D3%A9%D0%B7%D1%96""",
                     reply_markup=Abai3)
bot.polling()
