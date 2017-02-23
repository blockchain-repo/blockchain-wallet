"""A simple way to generate a `TRANSFER` transaction.

"""
import json
import requests
from UTXO import UTXO
from bigchaindb.common.transaction import Transaction, Asset, Fulfillment, Condition

def transfer_asset_tx(verifying_key,signing_key,after,amount):
    #print(verifying_key,signing_key,amount)
    # Digital Asset Definition (e.g. RMB)
    asset = Asset(data={'money':'RMB'},data_id='1',divisible=True)
    # Metadata Definition
    metadata = {'planet': 'earth'}

    #TODO:inputS
    inputs = []
    balance = 0
    utxo = UTXO(verifying_key)
    utxo = json.loads(utxo)
    for i in utxo:
        print(i)
        f = Fulfillment.from_dict({
            'fulfillment':{"bitmask": 32 ,
                                "public_key":  "7Kc4uLWndreZYmrYi5VsE2mxJC5wVxvHioy8xUws4rLz" ,
                                "signature":"" ,
                                "type":  "fulfillment" ,
                                "type_id": 4
                          } ,
            'input': {
                'cid': i['cid'],
                'txid': i['txid'],
             },
             'owners_before': [verifying_key],
        })
        inputs.append(f)
        balance += i['amount']

    # create trnsaction  TODO : amount
    if balance < amount:
        exit('balance<amount')
    elif balance == amount:
        tx = Transaction.transfer(inputs, [([after],amount)], asset)
    else:
        tx = Transaction.transfer(inputs, [([after],amount),([verifying_key],balance-amount)],asset)
    # sign with private key
    tx = tx.sign([signing_key])
    tx_id = tx.to_dict()['id']
    print(tx.to_dict())

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
    amount = input ('Please input an integer:\n')
    try:
        amount = int(amount)
    except ValueError:
        exit('`amount` must be an int')
    print(transfer_asset_tx(verifying_key,signing_key,after,amount))

