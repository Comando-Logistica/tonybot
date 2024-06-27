def message_handler(bot, message):
    bot.reply_to(message, 'Você disse: ' + message.text)
