def ajuda_handler(bot, message):

	msg = '''
Olá, eu sou o Tony o assistente virtual da Comando!

Funcionando:

⚫/placa [PLACA] - Reterna a documentação da placa
⚫/cpf [cpf do motorista] - retorna documentos do motorista (se enviada pelo RH ou responsável)
⚫/conduta - Retorna os codigo de contuda
⚫/cartaocnpj [cidade da filial] - Retorna o Cartao CNPJ
⚫/apresentacao - retorna a Apresentação Institucional

Em progresso:

⚫/conhecimento EMPRESA CTE (/conhecimento COFCO 89543) - Retorna os dados do Globus
'''
	
	bot.reply_to(message, msg)