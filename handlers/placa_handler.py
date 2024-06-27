import os

def buscar_arquivo(caminho, nome_arquivo, extensoes):
    for arquivo in os.listdir(caminho):
        arquivo_completo = os.path.join(caminho, arquivo)
        if os.path.isfile(arquivo_completo):
            if any(arquivo.endswith(ext) for ext in extensoes) and arquivo.startswith(nome_arquivo):
                return arquivo_completo
        else:
            resultado = buscar_arquivo(arquivo_completo, nome_arquivo, extensoes)
            if resultado:
                return resultado
    return None

def procurar_documento(bot, message, placas, action, caminhos):
    extensoes = ['.pdf', '.png', '.jpeg', '.jpg']
    for placa in placas:
        for caminho in caminhos:
            path = caminho.replace('\\\\', '\\').replace('\\1', '\\\\1')
            resultado = buscar_arquivo(path, placa, extensoes)
            if resultado:
                send_doc(bot, message, resultado, action)
                return
    bot.reply_to(message, f"{action} não encontrado.")

def send_doc(bot, message, doc_file, action):
    with open(doc_file, 'rb') as doc:
        bot.reply_to(message, f"Enviando {action.upper()}.")
        bot.send_document(message.chat.id, doc, reply_to_message_id=message.message_id)

def placa_handler(bot, message, placas, action):
    caminhos = {
        'crlv': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS BOITUVA\\2024\\',
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS BOITUVA\\2023\\',
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS RONDONOPOLIS\\Licenciamento 2024\\',
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS RONDONOPOLIS\\Licenciamento 2023\\',
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS PE\\',
        ],
        'civ': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS TONY\\CIV\\2024\\'
        ],
        'cipp': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS TONY\\CIPP\\2024\\'
        ],
        'ctpp': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS TONY\\CTPP\\2024\\'
        ],
        'tara': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS TONY\\TARA\\2024\\'
        ],
        'nf': [
            '\\\\192.168.2.8\\DocsFrotas\\DOCUMENTOS TONY\\NF\\2024\\'
        ]
    }

    if action == 'todos_veiculo':
        for doc_type, paths in caminhos.items():
            procurar_documento(bot, message, placas, doc_type, paths)
    else:
        procurar_documento(bot, message, placas, action, caminhos.get(action, []))
