import telebot
from Controller import Controller

bot = telebot.TeleBot('1311280239:AAFAOTbsernFtNC1OwPs609ovIeHMgiykYA')


controller = Controller("d16665sat556v8", "ccggvsufkajsus",
                        "0416de0b350e129e665a0fedf34c68a489aec8cf84ad657007446593d365b7d7",
                        "ec2-46-137-124-19.eu-west-1.compute.amazonaws.com")

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
    bot.delete_message(call.message.chat.id, call.message.message_id)
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
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(23)[0][0],
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "test")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так", callback_data="yes_1"),
        telebot.types.InlineKeyboardButton("Ні", callback_data="no_1")
    )
    bot.delete_message(call.message.chat.id, call.message.message_id)
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
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     'Вибери категорію',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "social")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(22)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "prof")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(19)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "media")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(20)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "myst")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.delete_message(call.message.chat.id, call.message.message_id)
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="info")
    )
    bot.send_message(call.message.chat.id,
                     controller.get_soinfo(21)[0][0], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "no_1")
def statistic(call):
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     23
                     )


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
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.delete_so(call.message.from_user.id)
    bot.send_message(call.message.chat.id,
                     "✅ З якого ти факультету?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fi")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFi_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fen")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFen_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fpvn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFpvn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fprn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFprn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fgn")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFgn_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш практикувати те, що слухаєш на лекціях? 🧐",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "fsnst")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звісно, лекції нудні 🙋🏼",
                                           callback_data="practFsnst_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Теорія one love 🤓",
                                           callback_data="pract_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'Fido')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'East West Business')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'Студентське біологічне товариство')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'Moot Court Society')
    controller.add_so(call.message.from_user.id, 'Kma Legal Hackers')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'Це є ФГН')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id,'Асоціація студентів політологів')
    controller.add_so(call.message.from_user.id, 'ФСНСТ family')
    controller.add_so(call.message.from_user.id, 'IR НаУКМА')
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
        telebot.types.InlineKeyboardButton("І так всього вистачає 🙅🏻",
                                           callback_data="ideas_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Хочеш реалізувати свої ідеї в КМА? ✨",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "ideas_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Звичайно 😎",
                                           callback_data="pres_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це не для мене 🙆🏻‍♀",
                                           callback_data="pres_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, 'СК')
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
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, 'КС')
    controller.add_so(call.message.from_user.id, 'СВК')
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
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
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
        telebot.types.InlineKeyboardButton("Ой, ні 🙈",
                                           callback_data="dance_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Ти запалюєш танцполи на тусах? 🕺🏼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "dance_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("А як інакше 🤩",
                                           callback_data="report_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні-ні-ні 😶",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, 'Могилянка денс')
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
        telebot.types.InlineKeyboardButton("Я деревце 😅",
                                           callback_data="dancelearn_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "А хотів/ла б навчитися? 🥰",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "dancelearn_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("А як інакше 🤩",
                                           callback_data="report_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні-ні-ні 😶",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                      "Ти цікавишся журналістикою? 🎤 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "report_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("О таак 🤫",
                                           callback_data="radio_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це ще актуально? 🤭",
                                           callback_data="report_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "ТА")
    controller.add_so(call.message.from_user.id, "СВ family")
    bot.send_message(call.message.chat.id,
                      "А радіожурналістикою? 📻",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "radio_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не уявляю життя без цього ❕",
                                           callback_data="meet_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не беру участі 💆🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "РадіоКвіт")
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
        telebot.types.InlineKeyboardButton("Не беру участі 💆🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
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
        telebot.types.InlineKeyboardButton("Та ні 👌🏻",
                                           callback_data="meet_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "Кма Амнесті")
    controller.add_so(call.message.from_user.id, "Енактус")
    bot.send_message(call.message.chat.id,
                      "Тебе турбують питання екології? 🌱",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "eco_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, це весело 🎲",
                                           callback_data="geek_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, краще посплю 😴",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "ЕкоКлуб")
    bot.send_message(call.message.chat.id,
                      "Любиш настільні ігри так само, як відсутність пар в суботу? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "meet_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Так, це весело 🎲",
                                           callback_data="geek_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ні, краще посплю 😴",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Любиш настільні ігри так само, як відсутність пар в суботу? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "geek_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Я найкращий/а у цьому 🧛‍♀",
                                           callback_data="mafia_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Це нудно 🙅🏻",
                                           callback_data="geek_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "ГікКлаб")
    bot.send_message(call.message.chat.id,
                     "А в Мафію граєш з друзями? 🧛🏻",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "mafia_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Малюю все і скрізь 👩🏻‍🎨",
                                           callback_data="art_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ага 😂",
                                           callback_data="art_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "КмаМафія")
    bot.send_message(call.message.chat.id,
                     "Друзі у захваті від твоїх малюнків? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "geek_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Малюю все і скрізь 👩🏻‍🎨",
                                           callback_data="art_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Ага 😂",
                                           callback_data="art_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Друзі у захваті від твоїх малюнків? 😍",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "art_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Невід’ємна частина мене 😌",
                                           callback_data="design_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Байдуже, як виглядає 🙄",
                                           callback_data="art_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "КМА МАГ")
    bot.send_message(call.message.chat.id,
                     "Любиш дизайн і креатив? 🌈 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "design_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хобі мого життя 🤞🏼",
                                           callback_data="film_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє 🙃",
                                           callback_data="film_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "Сквад")
    controller.add_so(call.message.from_user.id, "Могила Арт Вик")
    bot.send_message(call.message.chat.id,
                     "Знімаєш ролики, займаєшся монтажем або фотографією? 📷 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "art_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хобі мого життя 🤞🏼",
                                           callback_data="film_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не моє 🙃",
                                           callback_data="film_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Знімаєш ролики, займаєшся монтажем або фотографією? 📷 ",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "film_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Обожнюю 🍿",
                                           callback_data="kino_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Рідко 📲",
                                           callback_data="kino_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "ТА")
    bot.send_message(call.message.chat.id,
                     "А фільми любиш дивитися? 🎬",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "film_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Обожнюю 🍿",
                                           callback_data="kino_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Рідко 📲",
                                           callback_data="kino_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "А фільми дивитись любиш? 🎬",
                     reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: call.data == "kino_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Роблю це постійно 🎶",
                                           callback_data="song_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що в душі 🚿",
                                           callback_data="song_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "Кіноклуб")
    bot.send_message(call.message.chat.id,
                     "Ти співаєш краще всіх? 🤩",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "kino_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Роблю це постійно 🎶",
                                           callback_data="song_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що в душі 🚿",
                                           callback_data="song_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Ти співаєш краще всіх? 🤩",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "song_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оо це про мене 🎹",
                                           callback_data="piano_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не вмію 😝",
                                           callback_data="piano_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "Хор")
    bot.send_message(call.message.chat.id,
                     "А може ще й на музичному інструменті граєш? 🎼",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "song_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Оо це про мене 🥁",
                                           callback_data="piano_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Не вмію 😝",
                                           callback_data="piano_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "А може граєш на музичному  інструменті? 🎸",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "piano_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Потайки мрію про це 🙊",
                                           callback_data="teatr_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що роль кущика 😅",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "КУТ")
    bot.send_message(call.message.chat.id,
                     "Ти хотів/ла б розвинути своє акторство на сцені? 🎭",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "piano_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Потайки мрію про це 🙊",
                                           callback_data="teatr_yes")
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Хіба що роль кущика 😅",
                                           callback_data="teatr_no")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Ти хотів/ла б розвинути своє акторство на сцені? 🎭",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "teatr_yes")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="finish")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    controller.add_so(call.message.from_user.id, "Театри")
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "teatr_no")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("Тиць",
                                           callback_data="finish")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id,
                     "Натисни, щоб завершити тест і отримати результати?",
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == "finish")
def statistic(call):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton("🔙 Повернутися", callback_data="back")
    )
    bot.answer_callback_query(call.id)
    bot.delete_message(call.message.chat.id, call.message.message_id)
    string = "Отже ми підібрали для тебе студентські організації! Сміливо можеш вступати до "
    list = controller.get_so(call.message.from_user.id)
    for items in list:
        if items != list[len(list)-1]:
            string = string + str(items[0]) + ", "
        else:
            string = string + str(items[0]) + ". "
    string = string + "Щоб більше дізнатися про ці СО скористайся командою /start . Ось посилання на деякі з них... "
    bot.send_message(call.message.chat.id,string)
    for i in controller.get_soinfo_fromuser(call.message.from_user.id):
         bot.send_message(call.message.chat.id, i)

    bot.send_message(call.message.chat.id,"Дякую за увагу!", reply_markup=keyboard)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.send_message(message.chat.id,'Скористайся кнопкою /start')


bot.polling(none_stop=True, interval=0)