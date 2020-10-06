import telebot
import time
import os
from flask import Flask, request
import logging
from random import randint
from Controller import Controller
TOKEN = '1311280239:AAFAOTbsernFtNC1OwPs609ovIeHMgiykYA'
bot = telebot.TeleBot(TOKEN)
order = """Радіо КВІТ
Музичний простір «КУТ»
Squad21
Гік-клуб
Хор «Момент»
КМА.МАГ
Mohylianka dance
КмаМафія
Та Могилянка
Студентська виборча комісія
Могила Арт Вик
Екоклуб «Зелена Хвиля»
Конференція студентів
KMAMNESTY
Могилянська Театральна Спільнота «4 студія»
ENACTUS NaUKMA
Асоціація студентів-політологів
KMA Legal Hackers
Moot Court Society
Fido
ФСНСТ family
East West Business
Synapce Space
Студентське біологічне товариство
Це є ФГН!
Студентська колегія"""

order_list = order.split("\n")

controller = Controller("postgres://mpmithawoffcxa:2ce8046e29865c57647220548eded28a7c709b185efce9935a7948efdd33f9be@ec2-54-155-22-153.eu-west-1.compute.amazonaws.com:5432/dbu4i5li69ulnp")
def get_actual_so(list1):
    list = list1
    string = ""
    for items in list:
        if "*" not in items[0]:
            string = string + str(items[0].replace("*","")) + ", "
    if string :
        string = string[:-2] + ". "
    return string

def get_maybe_so(list1):
    list = list1
    string = ""
    for items in list:
        if "*"  in items[0]:
            string = string + str(items[0].replace("*","")) + ", "

    if string:
        string = string[:-2] + ". "
    return string


def intersection (list1, list2):
    list3 = [item for item in list1 if item not in list2]
    return list3


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Пройти тест", callback_data="test"),
        telebot.types.InlineKeyboardButton("Інформація про СО", callback_data="info")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Про бота", callback_data="botinf"),
    )
    bot.send_message(message.chat.id,
                     '👋 Привіт, я допоможу тобі зі студентськими організаціями! Що будемо робити?',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "back")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Пройти тест", callback_data="test"),
        telebot.types.InlineKeyboardButton("Інформація про СО", callback_data="info")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Про бота", callback_data="botinf"),
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     '👋 Привіт, я допоможу тобі зі студентськими організаціями! Що будемо робити?',
                     reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id,
                     controller.get_soinfo(23)[0][0])


@bot.callback_query_handler(func=lambda call: call.data == "botinf")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(23)[0][0],
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "test")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так", callback_data="yes_1"),
        telebot.types.InlineKeyboardButton("Ні", callback_data="back")
    )
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     'Готовий розпочати тест?',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "info")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Соціальні проекти", callback_data="social")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Професійно наукові проекти", callback_data="prof")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Медіа(ЗМІ)", callback_data="media")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мистецькі та культурні проекти", callback_data="myst")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     'Вибери категорію',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "social")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(22)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "prof")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(19)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "media")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(20)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "myst")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(21)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "yes_1")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("ФІ 👨🏻‍💻",
                                           callback_data="fi"),
        telebot.types.InlineKeyboardButton("ФЕН 📈",
                                           callback_data="fen"),
        telebot.types.InlineKeyboardButton("ФПвН ⚖️",
                                           callback_data="fpvn")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("ФПрн 🧬",
                                           callback_data="fprn"),
        telebot.types.InlineKeyboardButton("ФГН 📜",
                                           callback_data="fgn"),
        telebot.types.InlineKeyboardButton("ФСНСТ 👨‍👩‍👧‍👦",
                                           callback_data="fsnst")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.delete_so(call.message.from_user.id)
    bot.send_message(call.message.chat.id,
                     "✅ З якого ти факультету?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fi")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFi_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFi_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fen")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFen_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFen_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fpvn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFpvn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFpvn_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fprn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFprn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFprn_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fgn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFgn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFgn_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fsnst")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, мені потрібно більше практики 🙋🏼",
                                           callback_data="practFsnst_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Навіть не знаю🤔",
                                           callback_data="practFsnst_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, мені і пар вистачає 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFi_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Fido')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFi_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Fido*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFen_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'East West Business')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFen_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'East West Business*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFprn_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Synapce Space')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFprn_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Synapce Space*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFpvn_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Moot Court Society')
    controller.add_so(call.message.from_user.id, 'KMA Legal Hackers')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFpvn_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Moot Court Society*')
    controller.add_so(call.message.from_user.id, 'KMA Legal Hackers*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFgn_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Це є ФГН!')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFgn_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id,'Це є ФГН!*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFsnst_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'ФСНСТ family')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "practFsnst_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'ФСНСТ family*')
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "pract_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Мій мозок переповнений ідеями 🎉",
                                           callback_data="ideas_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ідей поки не маю, але готовий_ва спробувати 🤚",
                                           callback_data="ideas_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "ideas_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я і був/ла президетом_кою 😎",
                                           callback_data="pres_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хотілося спробувати, але так і не наважився_лась🙇‍♂‍",
                                           callback_data="pres_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це не для мене 🙆🏻‍♀",
                                           callback_data="pres_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'ENACTUS NaUKMA')
    controller.add_so(call.message.from_user.id, 'Студентська колегія')
    bot.send_message(call.message.chat.id,
                     "Мріяв/ла стати президентом школи? 😏",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "ideas_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я і був/ла президетом_кою 😎",
                                           callback_data="pres_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хотілося спробувати, але так і не наважився_лась🙇‍♂‍",
                                           callback_data="pres_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це не для мене 🙆🏻‍♀",
                                           callback_data="pres_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'ENACTUS NaUKMA*')
    controller.add_so(call.message.from_user.id, 'Студентська колегія*')
    bot.send_message(call.message.chat.id,
                     "Мріяв/ла стати президентом школи? 😏",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "pres_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ще й як 💃🏻",
                                           callback_data="dance_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю танцювати для себе 👀 ",
                                           callback_data="dance_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'Конференція студентів')
    controller.add_so(call.message.from_user.id, 'Студентська виборча комісія')
    bot.send_message(call.message.chat.id,
                     "Ти запалюєш танцполи на тусах? 🕺🏼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "pres_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ще й як 💃🏻",
                                           callback_data="dance_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю танцювати для себе 👀 ",
                                           callback_data="dance_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'Конференція студентів*')
    controller.add_so(call.message.from_user.id, 'Студентська виборча комісія*')
    bot.send_message(call.message.chat.id,
                     "Ти запалюєш танцполи на тусах? 🕺🏼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "pres_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ще й як 💃🏻",
                                           callback_data="dance_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю танцювати для себе 👀 ",
                                           callback_data="dance_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Ти запалюєш танцполи на тусах? 🕺🏼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "ideas_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ще й як 💃🏻",
                                           callback_data="dance_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю танцювати для себе 👀 ",
                                           callback_data="dance_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Ти запалюєш танцполи на тусах? 🕺🏼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "dance_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, вже у всіх друзів взяв_ла інтерв'ю 🤩 ",
                                           callback_data="report_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла, але цікаво 🧑‍💻 ",
                                           callback_data="report_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні-ні-ні 😶",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'Mohylianka dance')
    bot.send_message(call.message.chat.id,
                     "Ти цікавишся журналістикою? 🎤",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "dance_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, вже у всіх друзів взяв_ла інтерв'ю 🤩 ",
                                           callback_data="report_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла, але цікаво 🧑‍💻 ",
                                           callback_data="report_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні-ні-ні 😶",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, 'Mohylianka dance*')
    bot.send_message(call.message.chat.id,
                     "Ти цікавишся журналістикою? 🎤",
                     reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == "dance_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Дужее 😊",
                                           callback_data="dance_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Можна спробувати✌️",
                                           callback_data="dance_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я деревце 😅",
                                           callback_data="dancelearn_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "А хотів/ла б навчитися? 🥰",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "dancelearn_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, вже у всіх друзів взяв_ла інтерв'ю 🤩 ",
                                           callback_data="report_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла, але цікаво 🧑‍💻 ",
                                           callback_data="report_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні-ні-ні 😶",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                      "Ти цікавишся журналістикою? 🎤 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "report_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не уявляю життя без цього ❕",
                                           callback_data="meet_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не був_ла на мітингу, але підтримую участників ✊",
                                           callback_data="meet_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не цікавить 💆🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Та Могилянка")
    controller.add_so(call.message.from_user.id, "Радіо КВІТ")

    bot.send_message(call.message.chat.id,
                     "Тебе можна зустріти на мітингах? ❌",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "report_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не уявляю життя без цього ❕",
                                           callback_data="meet_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не був_ла на мітингу, але підтримую участників ✊",
                                           callback_data="meet_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не цікавить 💆🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Та Могилянка*")
    controller.add_so(call.message.from_user.id, "Радіо КВІТ*")

    bot.send_message(call.message.chat.id,
                     "Тебе можна зустріти на мітингах? ❌",
                     reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "report_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не уявляю життя без цього ❕",
                                           callback_data="meet_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не був_ла на мітингу, але підтримую участників ✊",
                                           callback_data="meet_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не цікавить 💆🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))

    bot.send_message(call.message.chat.id,
                     "Тебе можна зустріти на мітингах? ❌",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "meet_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Бентежать моє серце 💚",
                                           callback_data="eco_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що стараюся не брати пакетики в магазинах 😺 ",
                                           callback_data="eco_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні 👌🏻",
                                           callback_data="eco_no")
    )
    bot.answer_callback_query(call.id)

    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "KMAMNESTY")
    bot.send_message(call.message.chat.id,
                      "Тебе турбують питання екології? 🌱",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "meet_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Бентежать моє серце 💚",
                                           callback_data="eco_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що стараюся не брати пакетики в магазинах 😺 ",
                                           callback_data="eco_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні 👌🏻",
                                           callback_data="eco_no")
    )
    bot.answer_callback_query(call.id)

    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "KMAMNESTY*")
    bot.send_message(call.message.chat.id,
                      "Тебе турбують питання екології? 🌱",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "eco_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно граю з друзями 🎲 ",
                                           callback_data="geek_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Грав_ла би, якби була компанія 🙄 ",
                                           callback_data="geek_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, краще посплю 😴",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Екоклуб «Зелена Хвиля»")
    bot.send_message(call.message.chat.id,
                      "Любиш настільні ігри так само, як відсутність пар в суботу? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "eco_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно граю з друзями 🎲 ",
                                           callback_data="geek_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Грав_ла би, якби була компанія 🙄 ",
                                           callback_data="geek_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, краще посплю 😴",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Екоклуб «Зелена Хвиля»*")
    bot.send_message(call.message.chat.id,
                      "Любиш настільні ігри так само, як відсутність пар в суботу? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "eco_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно граю з друзями 🎲 ",
                                           callback_data="geek_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Грав_ла би, якби була компанія 🙄 ",
                                           callback_data="geek_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, краще посплю 😴",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                      "Любиш настільні ігри так само, як відсутність пар в суботу? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "meet_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Бентежать моє серце 💚",
                                           callback_data="eco_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що стараюся не брати пакетики в магазинах 😺 ",
                                           callback_data="eco_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні 👌🏻",
                                           callback_data="eco_no")
    )
    bot.answer_callback_query(call.id)

    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Тебе турбують питання екології? 🌱",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "geek_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я найкращий/а у цьому 🧛‍♀",
                                           callback_data="mafia_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю мафію, але граю рідко 😶",
                                           callback_data="mafia_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це нудно 🙅🏻",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Гік-клуб")
    bot.send_message(call.message.chat.id,
                     "А в Мафію граєш з друзями? 🧛🏻",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "geek_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я найкращий/а у цьому 🧛‍♀",
                                           callback_data="mafia_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Люблю мафію, але граю рідко 😶",
                                           callback_data="mafia_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це нудно 🙅🏻",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Гік-клуб*")
    bot.send_message(call.message.chat.id,
                     "А в Мафію граєш з друзями? 🧛🏻",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "mafia_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("О, так, творю всюди 🦋",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Дивлячись що називати творчістю 🙃",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні, якось не дуже 👀",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "КмаМафія")
    bot.send_message(call.message.chat.id,
                     "Залишилось ще трошки!")
    bot.send_message(call.message.chat.id,
                     "Вважаєш себе творчою людиною? 🦄",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "mafia_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("О, так, творю всюди 🦋",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Дивлячись що називати творчістю 🙃",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні, якось не дуже 👀",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "КмаМафія*")

    bot.send_message(call.message.chat.id,
                     "Вважаєш себе творчою людиною? 🦄",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "geek_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("О, так, творю всюди 🦋",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Дивлячись що називати творчістю 🙃",
                                           callback_data="tvor_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Та ні, якось не дуже 👀",
                                           callback_data="tvor_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))

    bot.send_message(call.message.chat.id,
                     "Вважаєш себе творчою людиною? 🦄",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "tvor_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Малюю все і скрізь 👩🏻‍🎨",
                                           callback_data="art_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Поки ще нікому не показував_ла свої творіння 🙈",
                                           callback_data="art_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє це 😂",
                                           callback_data="art_no")
    )
    bot.answer_callback_query(call.id)

    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Друзі у захваті від твоїх малюнків? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "tvor_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="prefinish")
    )
    bot.answer_callback_query(call.id)

    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "art_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Невід’ємна частина мене 😌",
                                           callback_data="design_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Вмію хіба що замалювати прищик в фотошопі 😂",
                                           callback_data="design_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Байдуже, як виглядає 🙄",
                                           callback_data="design_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "КМА.МАГ")
    bot.send_message(call.message.chat.id,
                     "Любиш дизайн і креатив? 🌈 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "art_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Невід’ємна частина мене 😌",
                                           callback_data="design_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Вмію хіба що замалювати прищик в фотошопі 😂",
                                           callback_data="design_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Байдуже, як виглядає 🙄",
                                           callback_data="design_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "КМА.МАГ*")
    bot.send_message(call.message.chat.id,
                     "Любиш дизайн і креатив? 🌈 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "art_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Невід’ємна частина мене 😌",
                                           callback_data="design_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Вмію хіба що замалювати прищик в фотошопі 😂",
                                           callback_data="design_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Байдуже, як виглядає 🙄",
                                           callback_data="design_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Любиш дизайн і креатив? 🌈 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "design_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Маю таке хобі 🤞🏼 ",
                                           callback_data="film_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла 🤔",
                                           callback_data="film_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє 🙃",
                                           callback_data="film_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Squad21")
    bot.send_message(call.message.chat.id,
                     "Знімаєш ролики, займаєшся монтажем або фотографією? 📷 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "design_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Маю таке хобі 🤞🏼 ",
                                           callback_data="film_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла 🤔",
                                           callback_data="film_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє 🙃",
                                           callback_data="film_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Squad21*")
    bot.send_message(call.message.chat.id,
                     "Знімаєш ролики, займаєшся монтажем або фотографією? 📷 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "design_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Маю таке хобі 🤞🏼 ",
                                           callback_data="film_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ніколи не пробував_ла 🤔",
                                           callback_data="film_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє 🙃",
                                           callback_data="film_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Знімаєш ролики, займаєшся монтажем або фотографією? 📷 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "film_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Обожнюю співати і в мене гарно виходить 🎶",
                                           callback_data="song_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Інколи співаю для друзів 🥰",
                                           callback_data="song_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що в душі 🚿",
                                           callback_data="song_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Та Могилянка")

    bot.send_message(call.message.chat.id,
                     "Ти співаєш краще всіх? 🤩",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "film_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Обожнюю співати і в мене гарно виходить 🎶",
                                           callback_data="song_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Інколи співаю для друзів 🥰",
                                           callback_data="song_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що в душі 🚿",
                                           callback_data="song_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Та Могилянка*")

    bot.send_message(call.message.chat.id,
                     "Ти співаєш краще всіх? 🤩",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "film_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Обожнюю співати і в мене гарно виходить 🎶",
                                           callback_data="song_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Інколи співаю для друзів 🥰",
                                           callback_data="song_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що в душі 🚿",
                                           callback_data="song_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))

    bot.send_message(call.message.chat.id,
                     "Ти співаєш краще всіх? 🤩",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "song_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оо це про мене 🥁",
                                           callback_data="piano_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Знаю пару акордів 🙄",
                                           callback_data="piano_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не вмію 😝",
                                           callback_data="piano_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Хор «Момент»")
    bot.send_message(call.message.chat.id,
                     "А може ще й на музичному інструменті граєш? 🎼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "song_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оо це про мене 🥁",
                                           callback_data="piano_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Знаю пару акордів 🙄",
                                           callback_data="piano_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не вмію 😝",
                                           callback_data="piano_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Хор «Момент»*")
    bot.send_message(call.message.chat.id,
                     "А може ще й на музичному інструменті граєш? 🎼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "song_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оо це про мене 🎹",
                                           callback_data="piano_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Знаю пару акордів 🙄",
                                           callback_data="piano_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не вмію 😝",
                                           callback_data="piano_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "А може граєш на музичному  інструменті? 🎸",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "piano_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно був_ла в театральних гуртках 🤩 ",
                                           callback_data="teatr_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Потайки мрію про це 🙊",
                                           callback_data="teatr_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що роль кущика 😅",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Музичний простір «КУТ»")
    bot.send_message(call.message.chat.id,
                     "Ти хотів/ла б розвинути своє акторство на сцені? 🎭",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "piano_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно був_ла в театральних гуртках 🤩 ",
                                           callback_data="teatr_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Потайки мрію про це 🙊",
                                           callback_data="teatr_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що роль кущика 😅",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Музичний простір «КУТ»*")
    bot.send_message(call.message.chat.id,
                     "Ти хотів/ла б розвинути своє акторство на сцені? 🎭",
                     reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "piano_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, постійно був_ла в театральних гуртках 🤩 ",
                                           callback_data="teatr_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Потайки мрію про це 🙊",
                                           callback_data="teatr_yes_maybe")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що роль кущика 😅",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Ти хотів/ла б розвинути своє акторство на сцені? 🎭",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "teatr_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="prefinish")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Могилянська Театральна Спільнота «4 студія»")
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "teatr_yes_maybe")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="prefinish")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    controller.add_so(call.message.from_user.id, "Могилянська Театральна Спільнота «4 студія»*")
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "teatr_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="prefinish")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "prefinish")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отримати покликання на соц мережі",
                                           callback_data="finish")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )

    keyboard2 = telebot.types.InlineKeyboardMarkup()
    keyboard2.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )
    bot.answer_callback_query(call.id)
    try:
         bot.delete_message(call.message.chat.id, call.message.message_id)
    except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    state = randint(0, 4)
    if state == 0:
        bot.send_message(call.message.chat.id,
                         "Питаємо у зірок результати…")
    elif state == 1:
        bot.send_message(call.message.chat.id,
                         "Проводимо стохастичний аналіз відповідей…")
    elif state == 2:
        bot.send_message(call.message.chat.id,
                         "Дивимося у чарівну кулю передбачення майбутнього…")
    elif state == 3:
        bot.send_message(call.message.chat.id,
                         "Питаємо результат у штучного інтелекту…")
    else:
        bot.send_message(call.message.chat.id,
                         "Налаштовуємо нейронну мережу результатів…")
    time.sleep(1)
    full_list = controller.get_so(call.message.from_user.id)
    length = len(full_list)
    if length > 0:
        actual = stabilizate_top_list(full_list,length)
        maybe = stabilizate_bottom_list(full_list,length)
        try:
            maybe = to_string(intersection(maybe, actual))
            actual = to_string(actual)
        except Exception as error:
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))


        if actual:
            result = "Пташечка нашептала, що тобі підходять такі СО: " + actual
            if maybe:
                result = result + "Також можеш спробувати : " + maybe
            bot.send_message(call.message.chat.id,
                             result,
                             reply_markup=keyboard)
        else:
            result = "Пташечка нашептала, що тобі підходять такі СО: " + maybe
            bot.send_message(call.message.chat.id,
                             result,
                             reply_markup=keyboard)
    else:
        bot.send_message(call.message.chat.id,
                         "На жаль, ми не можемо підібрати для тебе СО 😔 \nАле ти завжди можеш вибрати щось сам зі списку або пройти тест заново",
                         reply_markup=keyboard2)



def to_string(list):

    result = ""
    iter = 0
    for i in list:
        result = result + i
        if iter == len(list)-1:
            result = result + ". "
        else:
            result = result + ", "
        iter += 1

    return result


def stabilizate_top(list):

    result = ""
    iter = 0
    for i in order_list:
        for y in list:
            y[0].replace('*', '')
            if i == y[0]:
                result = result + i

                if iter == 2:
                    result = result + ". "
                else:
                    result = result + ", "
                iter += 1
                if iter > 2:
                    return result




def stabilizate_bottom(list):

    result = ""
    iter = 0
    for i in range(len(order_list)):
        for y in list:
            y[0].replace('*','')
            if order_list[len(order_list)-i-1] == y[0]:
                result = result + y[0]
                if iter == 2:
                    result = result + ". "
                else:
                    result = result + ", "
                iter += 1
                if iter > 2:
                    return result


def stabilizate_top_list(list,len):

    result = ["1","Конференція студентів","Студентська колегія"]
    iter = 0
    for i in order_list:
        for y in list:
            y[0].replace('*', '')
            if i == y[0].replace('*', ''):
                result[iter] = y[0].replace('*', '')
                iter += 1
                if iter > 2:
                    return result
                if len == iter + 1:
                    try:
                        result.remove("1")
                        result.remove("Конференція студентів")
                        result.remove("Студентська колегія")
                    except Exception as error:
                        print("Oops! An exception has occured:", error)
                        print("Exception TYPE:", type(error))
                    return result
    return result



def stabilizate_bottom_list(list,length):
    result = ["1","Конференція студентів","Студентська колегія"]
    iter = 0
    for i in range(len(order_list)):
        for y in list:
            y[0].replace('*','')
            if order_list[len(order_list)-i-1] == y[0].replace('*', ''):
                result[iter] =y[0].replace('*', '')
                iter += 1
                if iter > 2:
                    return result
                if length == iter + 1:
                    try:
                        result.remove("1")
                        result.remove("Конференція студентів")
                        result.remove("Студентська колегія")
                    except Exception as error:
                        print("Oops! An exception has occured:", error)
                        print("Exception TYPE:", type(error))
                    return result
    return result

@bot.callback_query_handler(func=lambda call: call.data == "finish")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )
    bot.answer_callback_query(call.id)
    full_list = controller.get_so(call.message.from_user.id)
    length = len(full_list)
    actual = stabilizate_top_list(full_list,length)
    maybe = stabilizate_bottom_list(full_list,length)
    try:
        concat = maybe + actual
    except Exception as error:
            concat = []
            print("Oops! An exception has occured:", error)
            print("Exception TYPE:", type(error))
    print(concat)
    controller.normalization()
    controller.add_so(call.message.from_user.id,'Студентська колегія')
    controller.add_so(call.message.from_user.id, 'Конференція студентів')
    for i in controller.get_soinfo_fromuser(call.message.from_user.id):
        if i[0] in concat:
            bot.send_message(call.message.chat.id, i[1])

    bot.send_message(call.message.chat.id,"You're rock!🤩\nЩоб дізнатися про інші організації переходь у відповідний розділ головного меню!", reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id,'Скористайся кнопкою /start')


bot.polling(none_stop=True)
