from telebot import *

botTimeWeb=TeleBot('7440807701:AAGJK0j-qCejKuZsFtUu3MbgHbgLjWRTsOE')

@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess="Здравствуйте! Чего изволите?"
    markup=types.InlineKeyboardMarkup()

    button_yes=types.InlineKeyboardButton(text='Информация о кофейне',callback_data='yes')
    button_sales=types.InlineKeyboardButton(text='Меню',callback_data='no')
    button_events=types.InlineKeyboardButton(text='Мероприятия',callback_data='No')
    button_blogs=types.InlineKeyboardButton(text='Наш блог:',callback_data='111')

    markup.add(button_yes)
    markup.add(button_sales)
    markup.add(button_events)
    markup.add(button_blogs)

    botTimeWeb.send_message(message.chat.id,first_mess,parse_mode='html',reply_markup=markup)

@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
  if function_call.message:
     if function_call.data == "yes":
        second_mess = "Кофейня «Секретер» — это уютное место, где вы можете насладиться чашечкой кофе, чая или какао, приготовленных профессиональными баристами-психологами. Они помогут вам выбрать напиток в соответствии с вашими предпочтениями, а также расскажут о различных техниках заваривания кофе."

        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://c-secrete.ru/"))

        botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

        fifth_mess='Наш адрес: г.Санкт-Петербург, Аптекарская набережная,д.6, рядом с Ботаническим садом. Вход с ул.Профессора Попова'

        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Как добраться',url='https://yandex.ru/maps/org/sekreter/162501215933/?ll=30.327555%2C59.972812&z=16'))

        botTimeWeb.send_message(function_call.message.chat.id, fifth_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

     elif function_call.data=="no":
         third_mess = "Меню"

         markup = types.InlineKeyboardMarkup()
         markup.add(types.InlineKeyboardButton("Наше меню", url="https://c-secrete.ru/menu"))

         botTimeWeb.send_message(function_call.message.chat.id, third_mess, reply_markup=markup)
         botTimeWeb.answer_callback_query(function_call.id)

     elif function_call.data == "No":
         fourth_mess="Афиша"
         fifth_mess = 'Также рекомендуем подписать на наш телеграмм-канал, чтобы первым узнавать о всех наших мероприятиях :)'

         #Афиша
         markup=types.InlineKeyboardMarkup()

         markup.add(types.InlineKeyboardButton("Наша афиша",url="https://c-secrete.ru/events"))
         botTimeWeb.send_message(function_call.message.chat.id,fourth_mess,reply_markup=markup)
         botTimeWeb.answer_callback_query(function_call.id)

         #Телеграмм-канал
         markup = types.InlineKeyboardMarkup()

         markup.add(types.InlineKeyboardButton('Секретер', url='https://t.me/secretaire_c'))
         botTimeWeb.send_message(function_call.message.chat.id, fifth_mess, reply_markup=markup)
         botTimeWeb.answer_callback_query(function_call.id)

     #Блог
     else:
        sixth_mess='Блог Секретера ведёт наша команда, включая поваров! Каждый из нас делиться профессиональным и жизненным опытом, поэтому  блог получается как картинки в калейдоскопе, где каждый может найти для себя что-то любопытное и информативное. '
        markup = types.InlineKeyboardMarkup()

        markup.add(types.InlineKeyboardButton("Блог Секретера", url="https://c-secrete.ru/blog"))
        botTimeWeb.send_message(function_call.message.chat.id, sixth_mess, reply_markup=markup)
        botTimeWeb.answer_callback_query(function_call.id)

botTimeWeb.infinity_polling()