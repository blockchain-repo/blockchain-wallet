"""The role of this module is to get transaction list of the account

"""
import time
import json
import requests


def time_stamp(timeNum):
    timeStamp = float(timeNum)/1000
    timeArray = time.localtime(timeStamp)
    tm = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return(tm)

def tx_record(verifying_key,host_ip,host_port):
    # TODO:URL
    #url='http://127.0.0.1:9984/uniledger/v1/transaction/getTxRecord?public_key={}'.format('Gvexu49oskc6ptYwzqP9q8sL9jLxjNZNMBWgVVhUtPmD')
    url='http://{}:{}/uniledger/v1/transaction/getTxRecord?public_key={}'.format(host_ip,host_port,verifying_key)
    r=requests.get(url)
    return(r.text)

if __name__=='__main__':
    account = {}
    with open('.account') as fp:
        account = json.load(fp)
    try:
        verifying_key = account['verifying_key']
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


    txs = json.loads(tx_record(verifying_key,host_ip,host_port))
    for t in txs:
        t['timestamp'] = time_stamp(t['timestamp'])
        t.pop('id')
    print(json.dumps(txs,indent=4))
