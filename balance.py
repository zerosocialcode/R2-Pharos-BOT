from web3 import Web3
from eth_account import Account
from colorama import Fore, Style
import json
import os
import asyncio

# --- CONFIGURATION (copy from bot.py) ---
RPC_URL = "https://testnet.dplabs-internal.com/"
USDC_CONTRACT_ADDRESS = "0x8bebfcbe5468f146533c182df3dfbf5ff9be00e2"
R2USD_CONTRACT_ADDRESS = "0x4f5b54d4AF2568cefafA73bB062e5d734b55AA05"
sR2USD_CONTRACT_ADDRESS = "0xF8694d25947A0097CB2cea2Fc07b071Bdf72e1f8"
ERC20_CONTRACT_ABI = json.loads('''[
    {"type":"function","name":"balanceOf","stateMutability":"view","inputs":[{"name":"address","type":"address"}],"outputs":[{"name":"","type":"uint256"}]}
]''')

def mask_address(address):
    return address[:6] + "*" * 6 + address[-6:]

def generate_address(private_key):
    try:
        account = Account.from_key(private_key)
        return account.address
    except Exception:
        return None

def get_token_balance(web3, address, contract_address):
    try:
        token_contract = web3.eth.contract(address=web3.to_checksum_address(contract_address), abi=ERC20_CONTRACT_ABI)
        balance = token_contract.functions.balanceOf(address).call()
        # All tokens are 6 decimals
        return balance / (10 ** 6)
    except Exception as e:
        print(f"{Fore.RED}Error fetching balance: {e}{Style.RESET_ALL}")
        return None

async def main():
    if not os.path.exists('accounts.txt'):
        print(f"{Fore.RED}accounts.txt not found!{Style.RESET_ALL}")
        return

    with open('accounts.txt', 'r') as file:
        accounts = [line.strip() for line in file if line.strip()]

    web3 = Web3(Web3.HTTPProvider(RPC_URL))

    print(f"{Fore.YELLOW + Style.BRIGHT}Checking balances for {len(accounts)} accounts...{Style.RESET_ALL}")
    print("="*70)
    for pk in accounts:
        address = generate_address(pk)
        if not address:
            print(f"{Fore.RED}Invalid private key: {pk}{Style.RESET_ALL}")
            continue

        usdc = get_token_balance(web3, address, USDC_CONTRACT_ADDRESS)
        r2usd = get_token_balance(web3, address, R2USD_CONTRACT_ADDRESS)
        sr2usd = get_token_balance(web3, address, sR2USD_CONTRACT_ADDRESS)

        print(f"{Fore.CYAN}Address: {Style.RESET_ALL}{mask_address(address)}")
        print(f"{Fore.BLUE}USDC:   {Fore.WHITE}{usdc}{Style.RESET_ALL} | "
              f"{Fore.BLUE}R2USD:  {Fore.WHITE}{r2usd}{Style.RESET_ALL} | "
              f"{Fore.BLUE}sR2USD: {Fore.WHITE}{sr2usd}{Style.RESET_ALL}")
        print("-" * 70)
    print(f"{Fore.YELLOW}Done.{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())
