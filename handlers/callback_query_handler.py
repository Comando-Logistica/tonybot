from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def callback_query_handler(bot, call, user_states):
    
    keyboard = InlineKeyboardMarkup()

    if call.data == 'ajuda':
        user_states[call.from_user.id] = {'state': 'Ajuda', 'action': call.data}

    elif call.data == 'veiculos':
        todos_button = InlineKeyboardButton(text='TODOS', callback_data='todos_veiculo')
        crlv_button = InlineKeyboardButton(text='CRLV', callback_data='crlv')
        civ_button = InlineKeyboardButton(text='CIV', callback_data='civ')
        cipp_button = InlineKeyboardButton(text='CIPP', callback_data='cipp')
        ctpp_button = InlineKeyboardButton(text='CTPP', callback_data='ctpp')
        nf_button = InlineKeyboardButton(text='NF', callback_data='nf')
        tara_button = InlineKeyboardButton(text='Tara', callback_data='tara')
        keyboard.add(todos_button, crlv_button, civ_button, cipp_button, ctpp_button, nf_button, tara_button)
        bot.send_message(call.message.chat.id, 'Escolha um documento de veículo:', reply_markup=keyboard)

    elif call.data == 'motoristas':
        cnh_button = InlineKeyboardButton(text='CNH', callback_data='cnh')
        endereco_button = InlineKeyboardButton(text='Endereço', callback_data='endereco')
        keyboard.add(cnh_button, endereco_button)
        bot.send_message(call.message.chat.id, 'Escolha um documento de motorista:', reply_markup=keyboard)
    
    elif call.data in ['todos_veiculo', 'crlv', 'civ', 'cipp', 'ctpp', 'nf', 'tara']:
        bot.send_message(call.message.chat.id, 'Por favor, insira a placa do veículo:')
        user_states[call.from_user.id] = {'state': 'Aguardando placa', 'action': call.data}
    
    elif call.data in ['cnh', 'endereco']:
        bot.send_message(call.message.chat.id, f'Você escolheu o documento: {call.data.upper()}')
        user_states[call.from_user.id] = {'state': 'Aguardando documento', 'action': call.data}

    bot.answer_callback_query(call.id)
