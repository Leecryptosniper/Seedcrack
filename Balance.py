#Balance.py
import json
from web3 import Web3, HTTPProvider

# Infura API key and endpoint
infura_api_key = 'c03616c36f1b4bd99dc1e13d77b40de0'
infura_endpoint = f'https://mainnet.infura.io/v3/{infura_api_key}'

# Connect to the Ethereum network using Infura
web3 = Web3(HTTPProvider(infura_endpoint))

# Function to check balance and print once if any non-zero balance is found
def check_and_print_progress(wallets):
    print('Search in Progress...')

    for wallet in wallets:
        try:
            # Check the balance of the wallet address
            balance_wei = web3.eth.get_balance(wallet["Wallet Address"])

            # If the balance is non-zero, print and save it
            if balance_wei > 0:
                print(f'Balance Found @ {wallet["Wallet Address"]}')
                with open('wallets_with_non_zero_balance.txt', 'a') as outfile:
                    outfile.write(f'Seed: {wallet["Seed"]}\nWallet Address: {wallet["Wallet Address"]}\nBalance Wei: {balance_wei}\n\n')
        except Exception as e:
            print(f'Error checking balance for address: {wallet["Wallet Address"]}\n{e}')

# Read wallet information from imported_wallets.txt
with open('imported_wallets.txt', 'r') as file:
    wallets_to_check = json.load(file)

# Call the function to check and print progress
check_and_print_progress(wallets_to_check)
