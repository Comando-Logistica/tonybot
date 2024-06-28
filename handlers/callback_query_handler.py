from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def callback_query_handler(bot, call, user_states):
    
    keyboard = InlineKeyboardMarkup()

    if call.data == 'ajuda':
        user_states[call.from_user.id] = {'state': 'Ajuda', 'action': call.data}

    elif call.data == 'veiculos':
        crlv_button = InlineKeyboardButton(text='CRLV', callback_data='crlv')
        civ_button = InlineKeyboardButton(text='CIV', callback_data='civ')
        cipp_button = InlineKeyboardButton(text='CIPP', callback_data='cipp')
        ctpp_button = InlineKeyboardButton(text='CTPP', callback_data='ctpp')
        nf_button = InlineKeyboardButton(text='NF', callback_data='nf')
        tara_button = InlineKeyboardButton(text='Tara', callback_data='tara')
        todos_button = InlineKeyboardButton(text='TODOS', callback_data='todos_veiculo')

        keyboard.add(crlv_button, civ_button, cipp_button, ctpp_button, nf_button, tara_button, todos_button)
        bot.send_message(call.message.chat.id, 'Escolha um documento de veículo:', reply_markup=keyboard)

    elif call.data == 'motoristas':
        cnh_button = InlineKeyboardButton(text='CNH', callback_data='cnh')
        endereco_button = InlineKeyboardButton(text='Endereço', callback_data='endereco')
        mopp_button = InlineKeyboardButton(text='MOPP', callback_data='mopp')
        nr20 = InlineKeyboardButton(text='NR20', callback_data='nr20')
        nr35 = InlineKeyboardButton(text='NR35', callback_data='nr35')
        todos_button = InlineKeyboardButton(text='TODOS', callback_data='todos_motorista')
        keyboard.add(cnh_button, endereco_button, mopp_button, nr20, nr35, todos_button)
        bot.send_message(call.message.chat.id, 'Escolha um documento de motorista:', reply_markup=keyboard)
    
    elif call.data in ['todos_veiculo', 'crlv', 'civ', 'cipp', 'ctpp', 'nf', 'tara']:
        bot.send_message(call.message.chat.id, 'Por favor, insira a placa do veículo:')
        user_states[call.from_user.id] = {'state': 'Aguardando placa', 'action': call.data}
    
    elif call.data in ['todos_motorista', 'cnh', 'endereco', 'mopp', 'nr20', 'nr35']:
        bot.send_message(call.message.chat.id, 'Por favor, insira o CPF do motorista:')
        user_states[call.from_user.id] = {'state': 'Aguardando CPF', 'action': call.data}

    bot.answer_callback_query(call.id)
