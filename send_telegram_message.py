from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with the actual token of your Telegram bot
telegram_bot_token = '6570313388:AAEzmzxcvWM3gba6rCpAqnLIEpBuo3veFAg'

# Create a Bot instance
bot = Bot(token=telegram_bot_token)

# Replace 'YOUR_CHAT_ID' with the actual chat ID where you want to send the message
telegram_chat_id = '-1001665353096'

# Replace 'YOUR_MESSAGE' with the message you want to send
message_text = 'Hi'

# Send the message
bot.send_message(chat_id=telegram_chat_id, text=message_text)
