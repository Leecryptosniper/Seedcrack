import json
from web3 import Web3, HTTPProvider
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Filters, MessageHandler, Updater

# Infura API key and endpoint
infura_api_key = 'c03616c36f1b4bd99dc1e13d77b40de0'
infura_endpoint = f'https://mainnet.infura.io/v3/{infura_api_key}'

# Connect to the Ethereum network using Infura
web3 = Web3(HTTPProvider(infura_endpoint))

# Your Telegram Bot Token
telegram_bot_token = '6570313388:AAEzmzxcvWM3gba6rCpAqnLIEpBuo3veFAg'

# Function to check balance and send message to Telegram
def check_and_send_balance(wallets, bot, chat_id):
    message = 'Search in Progress...'

    for wallet in wallets:
        try:
            # Check the balance of the wallet address
            balance_wei = web3.eth.get_balance(wallet["Wallet Address"])

            # If the balance is non-zero, add it to the message
            if balance_wei > 0:
                message += f'\n\nBalance Found @ {wallet["Wallet Address"]}\nSeed: {wallet["Seed"]}\nWallet Address: {wallet["Wallet Address"]}\nBalance Wei: {balance_wei}'
        except Exception as e:
            print(f'Error checking balance for address: {wallet["Wallet Address"]}\n{e}')

    # Send the message to the Telegram group or user
    bot.send_message(chat_id=chat_id, text=message)

# Command handler for starting the balance check
def start(update: Update, context: CallbackContext) -> None:
    # Read wallet information from imported_wallets.txt
    with open('imported_wallets.txt', 'r') as file:
        wallets_to_check = json.load(file)

    # Get the chat ID to send the message back to the same chat
    chat_id = update.message.chat_id

    # Call the function to check and send balance
    check_and_send_balance(wallets_to_check, context.bot, chat_id)

# Entry point of the script
def main():
    # Create the Updater and pass it your bot's token
    updater = Updater(token=telegram_bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register the start command
    dp.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
