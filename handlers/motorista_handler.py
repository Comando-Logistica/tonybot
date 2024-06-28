import os

def buscar_arquivo(caminho, nome_arquivo, extensoes):
    for arquivo in os.listdir(caminho):
        arquivo_completo = os.path.join(caminho, arquivo)
        if os.path.isfile(arquivo_completo):
            if any(arquivo.endswith(ext) for ext in extensoes) and nome_arquivo in arquivo:
                return arquivo_completo
        else:
            resultado = buscar_arquivo(arquivo_completo, nome_arquivo, extensoes)
            if resultado:
                return resultado
    return None

def procurar_documento(bot, message, documento, action, caminhos):
    extensoes = ['.pdf', '.png', '.jpeg', '.jpg']
    for caminho in caminhos:
        path = caminho.replace('\\\\', '\\').replace('\\1', '\\\\1')
        resultado = buscar_arquivo(path, documento, extensoes)
        if resultado:
            send_doc(bot, message, resultado, action)
            return
    bot.reply_to(message, f"{action} não encontrado.")

def send_doc(bot, message, doc_file, action):
    with open(doc_file, 'rb') as doc:
        bot.reply_to(message, f"Enviando {action.upper()}.")
        bot.send_document(message.chat.id, doc, reply_to_message_id=message.message_id)

def motorista_handler(bot, message, documento, action):
    caminhos = {
            'cnh': [
                '\\\\192.168.2.8\\cnh_motorista\\Carteira Nacional de Habilitação Padronizadas\\',
                '\\\\192.168.2.8\\cnh_motorista\\Carteira Nacional de Habilitação Não Padronizadas\\'
            ],
            'endereco': [
                '\\\\192.168.2.8\\cnh_motorista\\Comprovantes de Endereços Padronizados\\',
                '\\\\192.168.2.8\\cnh_motorista\\Comprovantes de Endereços Não Padronizados\\'
            ],
            'mopp': [
                '\\\\192.168.2.8\\cnh_motorista\\MOPP - Padronizado\\',
                '\\\\192.168.2.8\\cnh_motorista\\MOPP - Não Padronizado\\'
            ],
            'nr20': [
                '\\\\192.168.2.8\\cnh_motorista\\NR20 - Padronizado\\',
                '\\\\192.168.2.8\\cnh_motorista\\NR20 - Não Padronizado\\'
            ],
            'nr35': [
                '\\\\192.168.2.8\\cnh_motorista\\NR35 - Padronizado\\',
                '\\\\192.168.2.8\\cnh_motorista\\NR35 - Não Padronizado\\'
            ]
    }

    if action == 'todos_motorista':
        for doc_type, paths in caminhos.items():
            procurar_documento(bot, message, documento, doc_type, paths)
    else:
        procurar_documento(bot, message, documento, action, caminhos.get(action, []))
