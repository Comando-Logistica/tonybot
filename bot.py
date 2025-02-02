import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
from handlers.start_handler import start_handler
from handlers.message_handler import message_handler
from handlers.callback_query_handler import callback_query_handler
from utils.validar_placa import validar_placa
from utils.validar_cpf import validar_cpf
from utils.converter_placa import converter_placa
from handlers.placa_handler import placa_handler
from handlers.motorista_handler import motorista_handler
from handlers.ajuda_handler import ajuda_handler
from data.user_management import has_permission, register_user, is_admin, load_users
from handlers.documentos_handler import send_doc_info

bot = telebot.TeleBot(TOKEN)
user_states = {}

# Verificar se já existe algum usuário registrado como administrador
def is_any_admin():
    users = load_users()
    for user in users.values():
        if user['privilege_level'] == 'admin':
            return True
    return False

# Mensagem de Inicio
@bot.message_handler(commands=['start'])
def handle_start(message):
    #print(f'Checking permission for user {message.from_user.id} to use "start" command.')
    if has_permission(message.from_user.id, 'start'):
        start_handler(bot, message)
        user_states.pop(message.from_user.id, None)
    else:
        bot.reply_to(message, f"Você não tem permissão para usar este comando. Seu ID é {message.from_user.id}")
        print(f"START | ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

@bot.callback_query_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'Ajuda')
def handle_ajuda(message):
    if has_permission(message.from_user.id, 'ajuda'):
        print('111')
        msg = '''
    Olá, eu sou o Tony o assistente virtual da Comando!

    Você pode selecionar a opção desejada clicando nos botões do menu:

    Funcionando:

    ⚫Placa - Reterna a documentação da placa
    ⚫Motorista - retorna documentos do motorista (se enviada pelo RH ou responsável)
    ⚫Codigo de Conduta - Retorna os codigo de contuda
    ⚫Cartao CNPJ - Retorna o Cartao CNPJ
    ⚫Apresentacao - retorna a Apresentação Institucional

    Em progresso:

    ⚫CTE/CTRC (Busca por CTE/CTRC) - Retorna os dados do Globus
    '''

        bot.reply_to(message.chat.id, msg)
        #bot.send_message(message.chat.id, 'Escolha uma opção:', reply_markup=keyboard)
        
        #action = user_states.get(call.from_user.id, {}).get('action')
        #ajuda_handler(bot, call)
        user_states.pop(message.from_user.id, None)
    else:
        print(f"AJUDA | ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'Aguardando placa')
def handle_plate(message):
    #print(f'Checking permission for user {message.from_user.id} to use "placa" command.')
    if has_permission(message.from_user.id, 'placa'):
        action = user_states.get(message.from_user.id, {}).get('action')
        validar_placa(bot, message, user_states)
        user_state = user_states.get(message.from_user.id)
        if user_state and user_state.get('state') == 'plate_validated':
            plate = user_state.get('plate')
            placas = converter_placa(plate)
            placa_handler(bot, message, placas, action)
            user_states.pop(message.from_user.id, None)  # Resetar o estado do usuário
    else:
        bot.reply_to(message, "Você não tem permissão para usar este comando.")
        print(f"PLACA | ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

@bot.callback_query_handler(func=lambda call: user_states.get(call.from_user.id, {}).get('state') == 'Apresentação')
def handle_apresentacao(call):
    if has_permission(call.from_user.id, 'apresentacao'):
        action = user_states.get(call.from_user.id, {}).get('action')
        send_doc_info(bot, call, action)
        user_states.pop(call.from_user.id, None)
    else:
        bot.answer_callback_query(call.id, "Você não tem permissão para usar este comando.")
        print(f"APRESENTAÇÃO | ID {call.from_user.id} sem permissão! {call.from_user.first_name}")


@bot.callback_query_handler(func=lambda call: user_states.get(call.from_user.id, {}).get('state') == 'Codigo de Conduta')
def handle_conduta(call):
    if has_permission(call.from_user.id, 'conduta'):
        action = user_states.get(call.from_user.id, {}).get('action')
        send_doc_info(bot, call, action)
        user_states.pop(call.from_user.id, None) 
    else:
        bot.answer_callback_query(call.id, "Você não tem permissão para usar este comando.")
        print(f"CONDUTA | ID {call.from_user.id} sem permissão! {call.from_user.first_name}")

@bot.callback_query_handler(func=lambda call: user_states.get(call.from_user.id, {}).get('state') == 'Cartão CNPJ')
def handle_cartao_cnpj(call):
    print('cartao_cnpj')
    if has_permission(call.from_user.id, 'cartao_cnpj'):
        action = user_states.get(call.from_user.id, {}).get('action')
        print(action)
        send_doc_info(bot, call, action)
        user_states.pop(call.from_user.id, None) 
    else:
        bot.answer_callback_query(call.id, "Você não tem permissão para usar este comando.")
        print(f"CNPJ | ID {call.from_user.id} sem permissão! {call.from_user.first_name}")

@bot.message_handler(func=lambda message: user_states.get(message.from_user.id, {}).get('state') == 'Aguardando CPF')
def handle_cpf(message):
    if has_permission(message.from_user.id, 'motorista'):
        action = user_states.get(message.from_user.id, {}).get('action')
        validar_cpf(bot, message, user_states)
        user_state = user_states.get(message.from_user.id)
        if user_state and user_state.get('state') == 'cpf_validated':
            cpf = user_state.get('doc')
            motorista_handler(bot, message, cpf, action)
            user_states.pop(message.from_user.id, None)  # Resetar o estado do usuário
    else:
        bot.reply_to(message, "Você não tem permissão para usar este comando.")
        print(f"CPF | ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    #print(f'Checking permission for user {message.from_user.id} to use "message" command.')
    #if has_permission(message.from_user.id, 'message'):
        #message_handler(bot, message)
    #else:
        #bot.reply_to(message, "Você não tem permissão para usar este comando.")
    #print(f'Checking permission for user {message.from_user.id} to use "start" command.')
    if has_permission(message.from_user.id, 'start'):
        start_handler(bot, message)
        user_states.pop(message.from_user.id, None)
    else:
        bot.reply_to(message, f"Você não tem permissão para usar este comando. Seu ID é {message.from_user.id}")
        print(f"Qualquer| ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    #print(f'Checking permission for user {call.from_user.id} to use "callback" command.')
    if has_permission(call.from_user.id, 'callback'):
        callback_query_handler(bot, call, user_states)
    else:
        bot.answer_callback_query(call.id, "Você não tem permissão para realizar esta ação.")
        print(f"Callback| ID {call.from_user.id} sem permissão! {call.from_user.first_name}")

# Novo Comando de Registro
@bot.message_handler(commands=['registrar'])
def handle_register(message):
    if not is_any_admin() or is_admin(message.from_user.id):
        try:
            user_id, nome, cargo = message.text.split(', ')#, privilege_level, *commands
            user_id = str(user_id.split(' ')[-1].strip())
            nome = nome.strip()
            cargo = cargo.strip()
            #privilege_level = privilege_level.strip()
            #commands = [cmd.strip() for cmd in commands]
            register_user(user_id, nome, cargo)#, privilege_level, commands)
            bot.reply_to(message, f"Usuário {user_id} registrado com sucesso.")
        except ValueError:
            bot.reply_to(message, "Formato incorreto. Use: /registrar user_id, nome, cargo")
    else:
        bot.reply_to(message, "Você não tem permissão para registrar usuários.")
        print(f"Registrar| ID {message.from_user.id} sem permissão! {message.from_user.first_name}")

def main():
    try:
        bot.polling()
    except:
        main()

if __name__ == '__main__':
    main()
