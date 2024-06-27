import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
from handlers.start_handler import start_handler
# Mensagens Padroes
from handlers.message_handler import message_handler
from handlers.callback_query_handler import callback_query_handler
from utils.validar_placa import validar_placa
from utils.converter_placa import converter_placa
from handlers.placa_handler import placa_handler
from handlers.ajuda_handler import ajuda_handler

###

bot = telebot.TeleBot(TOKEN)
user_states = {}

# Mensagem de Inicio
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_handler(bot, message)

# Mensagem de Ajuda
@bot.message_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'Ajuda')
def handle_ajuda_2(message):
    ajuda_handler(bot, message)

@bot.message_handler(commands=['ajuda'])
def handle_ajuda(message):
    ajuda_handler(bot, message)

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'Aguardando placa')
def handle_plate(message):
    validar_placa(bot, message, user_states)
    user_state = user_states.get(message.from_user.id)
    if user_state and user_state.get('state') == 'plate_validated':
        plate = user_state.get('plate')
        placas = converter_placa(plate)
        action = user_state.get('action')
        placa_handler(bot, message, placas, action)
        user_states.pop(message.from_user.id, None)  # Resetar o estado do usuário



# Callback
@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    callback_query_handler(bot, call, user_states)

if __name__ == '__main__':
    bot.polling()
