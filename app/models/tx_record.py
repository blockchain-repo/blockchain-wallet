"""The role of this module is to get transaction list of the account

"""
import json
import time
import requests


def format_time(time_num):
    timestamp = float(time_num) / 1000
    time_array = time.localtime(timestamp)
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
    return tm


def tx_record(public, host, port):
    size = 100
    num = 1
    url = 'http://{}:{}/uniledger/v1/transaction/getTxRecord?public_key={}&pageSize={}&pageNum={}'.format(host, port,
                                                                                                          public, size,
                                                                                                          num)
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
#
#     config = {}
#     with open('.config') as fp:
#         config = json.load(fp)
#     try:
#         host_ip = config['host_ip']
#         host_port = config['host_port']
#     except ValueError:
#         exit('need .config')
#
#     txs = json.loads(tx_record(verifying_key, host_ip, host_port))
#     for t in txs:
#         t['timestamp'] = time_stamp(t['timestamp'])
#         t.pop('id')
#     print(json.dumps(txs, indent=4))
