import json
import requests
from .UTXO import UTXO
from bigchaindb.common.transaction import Transaction, Asset

def transfer_asset_tx(verifying_key,signing_key,after,amount):
    #print(verifying_key,signing_key,amount)
    # Digital Asset Definition (e.g. RMB)
    asset = Asset(data={'money':'RMB'},data_id='1',divisible=True)
    # Metadata Definition
    metadata = {'planet': 'earth'}

    #TODO:inputS
    inputs = []
    balance = 0
    UTXO = UTXO(verifying_key)
    for i in UTXO:
        f = Fulfillment.from_dict({
            'fulfillment': condition['condition']['details'],
            'input': {
                'cid': f['cid'],
                'txid': f['txid'],
             },
             'owners_before': verifying_key,
        })
        inputs.appnd(f)
        balance += f['amount']

    # create trnsaction  TODO : amount
    if balance < amount:
        exit('balance<amount')
    elif balance = amount:
        tx = Transaction.transfer(inputs, [([after],amount)], = asset)
    else
        tx = Transaction.transfer(inputs, [([after],amount),([verifying_key],balance-amount)], = asset)
    # sign with private key
    tx = tx.sign([signing_key])
    tx_id = tx.to_dict()['id']


    url='http://127.0.0.1:9984/uniledger/v1/transaction/createOrTransferTx'
    headers = {'content-type': 'application/json'}
    value = json.dumps(tx.to_dict())
    r = requests.post(url, data=value, headers=headers)
    return(r.text)

if __name__=='__main__':
    account = {}
    with open('.account') as fp:
        account = json.load(fp)
    try:
        username = account['username']
        verifying_key = account['verifying_key']
        signing_key = account['signing_key']
    except ValueError:
        exit('need .account')
    #TODO : validate
    after = input ('Please input an after:\n')
    try:
        after = int(amount)
    except ValueError:
        exit('`amount` must be an int')
    amount = input ('Please input an integer:\n')
    try:
        amount = int(amount)
    except ValueError:
        exit('`amount` must be an int')
    print(transfer_asset_tx(verifying_key,signing_key,after,amount))

