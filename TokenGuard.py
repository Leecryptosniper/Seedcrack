#// TokenGuard.py
import json
from web3 import Web3, HTTPProvider
from eth_account import Account

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

# Read user seed phrases from the file
with open('user_seed_phrases.txt', 'r') as file:
    seed_phrases = [line.strip() for line in file if line.strip()]

# Infura API key and endpoint
infura_api_key = 'c03616c36f1b4bd99dc1e13d77b40de0'
infura_endpoint = f'https://mainnet.infura.io/v3/{infura_api_key}'

# List to store imported wallets
imported_wallets = []

# Import wallets without TokenGuard integration
def import_wallets():
    for seed_phrase in seed_phrases:
        try:
            # Derive the Ethereum address from the seed phrase
            account = Account.from_mnemonic(seed_phrase)
            wallet_address = account.address

            # Print and store the imported wallet
            print(f'Wallet imported successfully for address: {wallet_address}')
            imported_wallets.append({"Seed": seed_phrase, "Wallet Address": wallet_address})
        except Exception as e:
            print(f'Error importing wallet for seed phrase: {seed_phrase}\n{e}')

# Call the function to import wallets
import_wallets()

# Save imported wallets to imported_wallets.txt
with open('imported_wallets.txt', 'w') as outfile:
    json.dump(imported_wallets, outfile, indent=2)
