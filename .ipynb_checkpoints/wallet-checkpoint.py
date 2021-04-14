import subprocess
import json
from dotenv import load_dotenv
import os
from web3 import Web3
from bit import *

from constants import *

load_dotenv()

mnemonic = os.getenv('mnemonic', 'split egg survey arctic nasty inspire critic sibling february happy vital meat divorce cruel city')

command = './derive -g --mnemonic='{mnemonic}' --cols=path,address,privkey,pubkey --format=json'

def derive_wallets(mnemonic, coin, numderive):
    
    command = './derive -g --mnemonic='{mnemonic}' --coin='{coin}' --numderive='{numderive}' --cols=path,address,privkey,pubkey --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()

    keys = json.loads(output)
    return keys

coins = {'btc','eth','btc-test'}

def priv_key_to_account(coin, priv_key):
    
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    if coin ==BTCTEST:
        return PrivateKeyTestnet(priv_key)
    
def create_tx(coin, account, to, amount):
    if coin ==ETH:
        


