from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def send_document(bot, call, doc):
    with open(doc, 'rb') as out:
        bot.send_document(call.message.chat.id, out, reply_to_message_id=call.message.message_id)

def send_doc_info(bot, call, action):
    documents = {
        'diesel': "\\\\192.168.2.8\\cnh_motorista\\Código de Conduta\\Código de Conduta - Comando Diesel - Assinado.pdf",
        'graos': "\\\\192.168.2.8\\cnh_motorista\\Código de Conduta\\Código de Conduta - Comando Grãos - Assinado.pdf",
        'duquedecaxias': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\DUQUE DE CAXIAS (RJ).pdf',
        'teresopolis': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\TERESOPOLIS (RJ).pdf',
        'rondonopolis': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\RONDONOPOLIS (MT).pdf',
        'boituva': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\BOITUVA (SP).pdf',
        'portovelho': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\PORTO VELHO (RO).pdf',
        'sapucaiadosul': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\SAPUCAIA DO SUL (RS).pdf',
        'curitiba': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\CURITIBA (PR).pdf',
        'palhoca': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\PALHOCA (SC).pdf',
        'campogrande': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\CAMPO GRANDE (MS).pdf',
        'goiania': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\GOIANIA (GO).pdf',
        'saojosedoscampos': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\SAO JOSE DOS CAMPOS (SP).pdf',
        'alagoinhas': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\ALAGOINHAS (BA).pdf',
        'itapissuma': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\ITAPISSUMA (PE).pdf',
        'novoprogresso': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\NOVO PROGRESSO (PA).pdf',
        'fortaleza': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\FORTALEZA (CE).pdf',
        'uberaba': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\UBERABA (MG).pdf',
        'teresina': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\TERESINA (PI).pdf',
        'mogiguacu': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\MOGI-GUAÇU (SP).pdf',
        'saoluis': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\SAO LUIS (MA).pdf',
        'nossasenhoradosocorro': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\NOSSA SENHORA DO SOCORRO (SE).pdf',
        'sinop': '\\\\192.168.2.8\\cnh_motorista\\Cartão CNPJ\\SINOP (MT).pdf',
        'apresentacao': '\\\\192.168.2.8\\cnh_motorista\\Apresentação Institucional\\Apresentação Institucional.pdf'
    }
    
    if action in documents:
        send_document(bot, call, documents[action])