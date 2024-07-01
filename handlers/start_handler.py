from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def start_handler(bot, message):
    bot.send_message(message.chat.id, "Olá, eu sou o Tony, o bot da Comando Logistica. Estou em desenvolvimento, talvez não funcione direito por enquanto. Para ver meus comandos digite /ajuda ou clique nos botões do menu abaixo:")

    keyboard = InlineKeyboardMarkup()
    veiculos = InlineKeyboardButton(text='Docs de Veiculos', callback_data='veiculos')
    motoristas = InlineKeyboardButton(text='Docs de Motoristas', callback_data='motoristas')
    ajuda = InlineKeyboardButton(text='Ajuda', callback_data='ajuda')
    conduta = InlineKeyboardButton(text='Código de Conduta', callback_data='conduta')
    cartao_cnpj  = InlineKeyboardButton(text='Cartão CNPJ', callback_data='cartao_cnpj')
    apresentacao = InlineKeyboardButton(text='Apresentação Institucional', callback_data='apresentacao')
    keyboard.add(veiculos, motoristas, ajuda, conduta, cartao_cnpj, apresentacao)
    
    bot.send_message(message.chat.id, 'Escolha uma opção:', reply_markup=keyboard)
