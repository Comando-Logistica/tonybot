import re

def validar_placa(bot, message, user_states):
    plate = message.text
    valid_plate_pattern1 = r'^[A-Za-z]{3}[0-9]{4}$'  # AAA1234
    valid_plate_pattern2 = r'^[A-Za-z]{3}[0-9][A-Za-z][0-9]{2}$'  # AAA1A34

    if re.match(valid_plate_pattern1, plate) or re.match(valid_plate_pattern2, plate):
        user_states[message.from_user.id].update({'state': 'plate_validated', 'plate': plate})  # Armazenar a placa validada
    else:
        bot.send_message(message.chat.id, 'Placa inválida. Por favor, insira uma placa válida.')
        user_states[message.from_user.id].update({'state': 'Aguardando placa'})  # Manter o estado de espera por uma placa válida
