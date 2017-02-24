"""The role of this module is to get transaction list of the account

"""
import json
import requests

def tx_record(verifying_key):
    # TODO:URL
    #url='http://127.0.0.1:9984/uniledger/v1/transaction/getTxRecord?public_key={}'.format('Gvexu49oskc6ptYwzqP9q8sL9jLxjNZNMBWgVVhUtPmD')
    url='http://127.0.0.1:9984/uniledger/v1/transaction/getTxRecord?public_key={}'.format(verifying_key)
    r=requests.get(url)
    return r.text

if __name__=='__main__':
    account = {}
    with open('.account') as fp:
        account = json.load(fp)
    try:
        verifying_key = account['verifying_key']
    except ValueError:
        exit('need .account')
    print(tx_record(verifying_key))
