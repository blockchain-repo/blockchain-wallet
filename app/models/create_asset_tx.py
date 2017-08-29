"""A simple way to generate a `CREATE` transaction.

"""
import json
import sys

import requests

from app.models.common.transaction import Transaction, Asset


def create_asset_tx(verifying_key, signing_key, amount, host_ip, host_port):
    # print(verifying_key,signing_key,amount)
    # Digital Asset Definition (e.g. RMB)
    asset = Asset(data={'money': 'RMB'}, data_id='20170628150000', divisible=True)
    # Metadata Definition
    metadata = {'planet': 'earth'}
    # create trnsaction  TODO : amount
    tx = Transaction.create([verifying_key], [([verifying_key], amount)], metadata=metadata, asset=asset)
    # sign with private key
    tx = tx.sign([signing_key])
    tx_id = tx.to_dict()['id']

    url = 'http://{}:{}/uniledger/v1/transaction/createOrTransferTx'.format(host_ip, host_port)
    headers = {'content-type': 'application/json'}
    value = json.dumps(tx.to_dict())
    r = requests.post(url, data=value, headers=headers)
    return (r.json())


if __name__ == '__main__':
    account = {}
    with open('.account') as fp:
        account = json.load(fp)
    try:
        username = account['username']
        verifying_key = account['verifying_key']
        signing_key = account['signing_key']
    except ValueError:
        exit('need .account')

    config = {}
    with open('.config') as fp:
        config = json.load(fp)
    try:
        host_ip = config['host_ip']
        host_port = config['host_port']
    except ValueError:
        exit('need .config')

    if not len(sys.argv) == 2:
        print("Please provide one parameter of amount(int)!")
        sys.exit()
    amount = sys.argv[1]

    try:
        amount = int(amount)
    except ValueError:
        exit('`amount` must be an int')
    print(json.dumps(create_asset_tx(verifying_key, signing_key, amount, host_ip, host_port), indent=4))