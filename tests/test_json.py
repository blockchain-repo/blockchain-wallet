import requests

url = 'http://localhost:9984/uniledger/v1/transaction/recharge'
res = requests.post(url, json={'target': '9GxFx9CueGAm37qfEDEuhrkV4Dss4yF2FVgcKd9ZCSKf',
                               'amount': 1000,
                               'msg': ''
                               })
print(res.json())
