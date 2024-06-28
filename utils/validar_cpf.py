# utils/validar_cpf.py

import re

def validar_cpf(bot, message, user_states):
    cpf = message.text
    valid_cpf_pattern = r'^\d{11}$'  # Padrão simples para 11 dígitos
    
    if re.match(valid_cpf_pattern, cpf) and is_valid_cpf(cpf):
        bot.send_message(message.chat.id, f'CPF {cpf} válido. Prosseguindo com a operação.')
        user_states[message.from_user.id] = {'state': 'cpf_validated', 'doc': cpf}
    else:
        bot.send_message(message.chat.id, 'CPF inválido. Por favor, insira um CPF válido.')
        user_states[message.from_user.id] = {'state': 'Aguardando cpf'}

def is_valid_cpf(cpf):
    # Função para validar o CPF com base em seus dígitos verificadores
    if len(cpf) != 11:
        return False

    # Elimina CPFs conhecidos que são inválidos
    if cpf in [str(i)*11 for i in range(10)]:
        return False

    # Validação do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10 % 11) % 10

    # Validação do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10 % 11) % 10

    return cpf[-2:] == f'{digito1}{digito2}'
