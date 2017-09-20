"""A simple way to generate a `TRANSFER` transaction to merge utxo.

"""
import json

import requests

from app.models.account_utxo_balance import UTXO
from app.models.common.transaction import Transaction, Asset, Fulfillment


def merge_utxo(verifying_key, signing_key, host_ip, host_port):
    asset = Asset(data={'money': 'RMB'}, data_id='20170628150000', divisible=True)
    metadata = {'type': 'merge'}

    inputs = []
    balance = 0
    utxo = UTXO(verifying_key, host_ip, host_port)
    utxo = json.loads(utxo)['data']
    length = len(utxo)
    print(utxo)
    for i in utxo:
        f = Fulfillment.from_dict({
            'fulfillment': i['details'],
            'input': {
                'cid': i['cid'],
                'txid': i['txid'],
            },
            'owners_before': [verifying_key],
        })
        inputs.append(f)
        balance += i['amount']

    if balance <= 0:
        return 'No need to merge, because of lack of balance'
    elif length <= 1:
        return 'No need to merge, because utxo len = 1'
    else:
        tx = Transaction.transfer(inputs, [([verifying_key], balance)], metadata=metadata, asset=asset)
        tx = tx.sign([signing_key])

        url = 'http://{}:{}/uniledger/v1/transaction/createOrTransferTx'.format(host_ip, host_port)
        headers = {'content-type': 'application/json'}
        value = json.dumps(tx.to_dict())
        r = requests.post(url, data=value, headers=headers)
        return r.json()


if __name__ == '__main__':
    account = {}
    with open('../.unichain-account') as fp:
        account = json.load(fp)
    try:
        username = account['username']
        public = account['keypair']['public']
        private = account['keypair']['private']
        host = account['server']['host']
        port = account['server']['port']
        print(json.dumps(merge_utxo(public, private, host, port), indent=4))
    except ValueError:
        exit('can not find ../.unichain-account')
