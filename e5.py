third_mess = 'Также рекомендуем подписать на наш телеграмм канал, чтобы первым узнавать о всех наших мероприятиях :)'
markup = types.InlineKeyboardMarkup()
markup.add(types.InlineKeyboardButton('Секретер', url='https://t.me/secretaire_c'))
botTimeWeb.send_message(function_call.message.chat.id, third_mess, reply_markup=markup)
botTimeWeb.answer_callback_query(function_call.id)
