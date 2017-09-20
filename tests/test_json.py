import multiprocessing
import requests
import time
from bigchaindb.common.crypto import generate_key_pair  # pri,pub
from bigchaindb import Bigchain


def key_pair_queue(num):
    while True:
        # keys = generate_key_pair()
        if accounts.full():
            print("q")
            break
        print(2)
        accounts.put(1)
        print(1)


def post_txs(num):
    url = 'http://localhost:9984/uniledger/v1/transaction/recharge'
    while True:
        pub = accounts.get()[1]
        # print(pid, ":", pub)
        requests.post(url, json={'target': pub,
                                 'amount': 1,
                                 'msg': ''
                                 })


num_clients = 1
count = 1025
accounts = multiprocessing.Queue(maxsize=count)

# generate_key_pair
start = time.time()
for x in range(num_clients):
    p = multiprocessing.Process(target=key_pair_queue, args=(x,))
    p.start()

while True:
    print(accounts.qsize())
    if accounts.qsize() == count:
        end = time.time()
        print(end - start)
        print(count / (end - start))
        break
    time.sleep(1)

#
# # post_txs with mp.Process and mp.Queue
# start = time.time()
# for x in range(num_clients):
#     multiprocessing.Process(target=post_txs, args=(x,)).start()
# end = time.time()
# print(end - start)
# print(count / (end - start))
#
# # count backlog
# b = Bigchain()
# while True:
#     print(b.get_backlog_tx_number())
#     time.sleep(1)
