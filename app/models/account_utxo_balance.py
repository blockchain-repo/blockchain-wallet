"""The role of this module is to get UTXO of the account

"""
import json
import requests


def UTXO(public, host, port):
    url = 'http://{}:{}/uniledger/v1/condition/getUnspentTxs?unspent=true&public_key={}'.format(host, port,
                                                                                                public)
    r = requests.get(url)
    return r.text

# if __name__ == '__main__':
#     account = {}
#     with open('.account') as fp:
#         account = json.load(fp)
#     try:
#         verifying_key = account['verifying_key']
#     except ValueError:
#         exit('need .account')
#     config = {}
#     with open('.config') as fp:
#         config = json.load(fp)
#     try:
#         host_ip = config['host_ip']
#         host_port = config['host_port']
#     except ValueError:
#         exit('need .config')
#
#     utxo = json.loads(UTXO(verifying_key, host_ip, host_port))["data"]
#     # utxo = json.dumps(utxo)
#     # print(utxo)
#     for u in utxo:
#         # print(u)
#         u.pop('details')
#     print(json.dumps(utxo, indent=4))
