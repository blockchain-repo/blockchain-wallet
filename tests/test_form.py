import requests

url = 'http://localhost:5000/recharge'
requests.post(url, data={'target': '9GxFx9CueGAm37qfEDEuhrkV4Dss4yF2FVgcKd9ZCSKf', 'private_flag': 'true',
                         'btc_amount': '511'})
