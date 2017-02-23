"""A simple way to generate a `CREATE` transaction.

"""
import json
import requests
from bigchaindb.common.transaction import Transaction, Asset

def create_asset_tx(verifying_key,signing_key,amount):
    #print(verifying_key,signing_key,amount)
    # Digital Asset Definition (e.g. RMB)
    asset = Asset(data={'money':'RMB'},data_id='1',divisible=True)
    # Metadata Definition
    metadata = {'planet': 'earth'}
    # create trnsaction  TODO : amount
    tx = Transaction.create([verifying_key], [([verifying_key],amount)], metadata = metadata, asset = asset)
    # sign with private key
    tx = tx.sign([signing_key])
    tx_id = tx.to_dict()['id']


    url='http://127.0.0.1:9984/uniledger/v1/transaction/createOrTransferTx'
    headers = {'content-type': 'application/json'}
    value = json.dumps(tx)
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
    amount = input ('Please input an integer:\n')
    try:
        amount = int(amount)
    except ValueError:
        exit('`amount` must be an int')
    print(create_asset_tx(verifying_key,signing_key,amount))
