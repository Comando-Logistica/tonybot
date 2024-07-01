from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

def callback_query_handler(bot, call, user_states):
    
    keyboard = InlineKeyboardMarkup()

    if call.data == 'ajuda':
        user_states[call.from_user.id] = {'state': 'Ajuda', 'action': call.data}

    elif call.data == 'conduta':
        diesel = InlineKeyboardButton(text='DIESEL', callback_data='diesel')
        graos = InlineKeyboardButton(text='GRAOS', callback_data='graos')
        keyboard.add(diesel, graos)
        bot.send_message(call.message.chat.id, 'Escolha a empresa do código de conduta:', reply_markup=keyboard)

    elif call.data == 'apresentacao':
        bot.send_message(call.message.chat.id, 'Enviando Apresentação Institucional')
        user_states[call.from_user.id] = {'state': 'Apresentação', 'action': call.data}

    elif call.data in ['diesel', 'graos']:
        user_states[call.from_user.id] = {'state': 'Codigo de Conduta', 'action': call.data}
        pass
        
    elif call.data == 'cartao_cnpj':
        duquedecaxias = InlineKeyboardButton(text='DUQUE DE CAXIAS (RJ)', callback_data='duquedecaxias')
        teresopolis = InlineKeyboardButton(text='TERESOPOLIS (RJ)', callback_data='teresopolis')
        rondonopolis = InlineKeyboardButton(text='RONDONOPOLIS (MT', callback_data='rondonopolis')
        boituva = InlineKeyboardButton(text='BOITUVA (SP)', callback_data='boituva')
        portovelho = InlineKeyboardButton(text='PORTO VELHO (RO)', callback_data='portovelho')
        sapucaiadosul = InlineKeyboardButton(text='SAPUCAIA DO SUL (RS)', callback_data='sapucaiadosul')
        curitiba = InlineKeyboardButton(text='CURITIBA (PR)', callback_data='curitiba')
        palhoca = InlineKeyboardButton(text='PALHOCA (SC)', callback_data='palhoca')
        campogrande = InlineKeyboardButton(text='CAMPO GRANDE (MS)', callback_data='campogrande')
        goiania = InlineKeyboardButton(text='GOIANIA (GO)', callback_data='goiania')
        saojosedoscampos = InlineKeyboardButton(text='SAO JOSE DOS CAMPOS (SP)', callback_data='saojosedoscampos')
        alagoinhas = InlineKeyboardButton(text='ALAGOINHAS (BA)', callback_data='alagoinhas')
        itapissuma = InlineKeyboardButton(text='ITAPISSUMA (PE)', callback_data='itapissuma')
        novoprogresso = InlineKeyboardButton(text='NOVO PROGRESSO (PA)', callback_data='novoprogresso')
        fortaleza = InlineKeyboardButton(text='FORTALEZA (CE)', callback_data='fortaleza')
        uberaba = InlineKeyboardButton(text='UBERABA (MG)', callback_data='uberaba')
        teresina = InlineKeyboardButton(text='TERESINA (PI)', callback_data='teresina')
        mogiguacu = InlineKeyboardButton(text='MOGI-GUAÇU (SP)', callback_data='mogiguacu')
        saoluis = InlineKeyboardButton(text='SAO LUIS (MA)', callback_data='saoluis')
        nossasenhoradosocorro = InlineKeyboardButton(text='NOSSA SENHORA DO SOCORRO (SE)', callback_data='nossasenhoradosocorro')
        sinop = InlineKeyboardButton(text='SINOP (MT)', callback_data='sinop')
        keyboard.row(duquedecaxias, teresopolis, rondonopolis)
        keyboard.row(boituva, portovelho, sapucaiadosul)
        keyboard.row(curitiba, palhoca, campogrande)
        keyboard.row(goiania, saojosedoscampos, alagoinhas)
        keyboard.row(itapissuma, novoprogresso, fortaleza)
        keyboard.row(uberaba, teresina, mogiguacu)
        keyboard.row(saoluis, nossasenhoradosocorro, sinop)
        bot.send_message(call.message.chat.id, 'Escolha a empresa do código do Cartao CNPJ:', reply_markup=keyboard)

    elif call.data in ['duquedecaxias', 'teresopolis', 'rondonopolis', 'boituva', 'portovelho', 'sapucaiadosul', 'curitiba', 'palhoca', 'campogrande', 'goiania', 'saojosedoscampos', 'alagoinhas', 'itapissuma', 'novoprogresso', 'fortaleza', 'uberaba', 'teresina', 'mogiguacu', 'saoluis', 'nossasenhoradosocorro', 'sinop']:
        user_states[call.from_user.id] = {'state': 'Cartão CNPJ', 'action': call.data}
        pass

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
