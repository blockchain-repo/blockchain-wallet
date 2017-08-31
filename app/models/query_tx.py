import json

import requests


def query_tx(tx_id, host, port):
    url = 'http://{}:{}/uniledger/v1/transaction/queryByID/'.format(host, port)
    headers = {'content-type': 'application/json'}
    data = {
        "type": "3",
        "tx_id": tx_id
    }
    data = json.dumps(data)
    r = requests.post(url, data=data, headers=headers)
    return r.text


if __name__ == '__main__':
    print(query_tx("edcc0ba046281fb418ad1532978983a56f389bfb2caac2c3cd39d4c2e87ca461", "localhost", "9984"))
