"""A simple way to generate a `TRANSFER` transaction.

"""
import sys
import json
import requests

from app.models.account_utxo_balance import UTXO
from app.models.common.transaction import Transaction, Asset, Fulfillment
from app.models.secretbox import secretbox


def transfer_asset_tx(public, private, target, amount, msg, private_flag, host, port):
    # print(verifying_key,signing_key,amount)
    # Digital Asset Definition (e.g. RMB)
    asset = Asset(data={'money': 'RMB'}, data_id='20170628150000', divisible=True)
    # Metadata Definition
    if private_flag is True:
        encrypted, nonce = secretbox(private, msg)
        metadata = {'encrypted': encrypted, 'nonce': nonce, 'public': public}
    else:
        metadata = {'raw': msg}

    inputs = []
    balance = 0
    utxo = UTXO(public, host, port)
    utxo = json.loads(utxo)["data"]
    for i in utxo:
        f = Fulfillment.from_dict({
            'fulfillment': i['details'],
            'input': {
                'cid': i['cid'],
                'txid': i['txid'],
            },
            'owners_before': [public],
        })
        inputs.append(f)
        balance += i['amount']

    # create transaction
    if balance < amount:
        return 'balance<amount'
    elif balance == amount:
        tx = Transaction.transfer(inputs, [([target], amount)], asset, metadata)
    else:
        tx = Transaction.transfer(inputs, [([target], amount), ([public], balance - amount)], asset, metadata)
    # sign with private key
    tx = tx.sign([private])
    url = 'http://{}:{}/uniledger/v1/transaction/createOrTransferTx'.format(host, port)
    headers = {'content-type': 'application/json'}
    value = json.dumps(tx.to_dict())
    r = requests.post(url, data=value, headers=headers)
    return r.json()

# if __name__ == '__main__':
#     account = {}
#     with open('.account') as fp:
#         account = json.load(fp)
#     try:
#         username = account['username']
#         verifying_key = account['verifying_key']
#         signing_key = account['signing_key']
#     except ValueError:
#         exit('need .account')
#
#     config = {}
#     with open('.config') as fp:
#         config = json.load(fp)
#     try:
#         host_ip = config['host_ip']
#         host_port = config['host_port']
#     except ValueError:
#         exit('need .config')
#
#     # TODO : validate
#     if not len(sys.argv) == 3:
#         print("Please provide two parameters for owner_after(key) and amount(int)!")
#         sys.exit()
#     after = sys.argv[1]
#     amount = sys.argv[2]
#     try:
#         amount = int(amount)
#     except ValueError:
#         exit('`amount` must be an int')
#     print(json.dumps(transfer_asset_tx(verifying_key, signing_key, after, amount, host_ip, host_port), indent=4))
