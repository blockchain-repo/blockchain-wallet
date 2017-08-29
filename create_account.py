"""The role of this module is to create an account and write to the '.account' file

"""
from collections import namedtuple
from cryptoconditions import crypto
import json
import os
import sys

CryptoKeypair = namedtuple('CryptoKeypair', ('signing_key', 'verifying_key'))


def generate_keypair():
    """Generates a cryptographic key pair.

    Returns:
        :class:`~bigchaindb_driver.crypto.CryptoKeypair`: A
        :obj:`collections.namedtuple` with named fields
        :attr:`~bigchaindb_driver.crypto.CryptoKeypair.signing_key` and
        :attr:`~bigchaindb_driver.crypto.CryptoKeypair.verifying_key`.

    """
    return CryptoKeypair(
        *(k.decode() for k in crypto.ed25519_generate_key_pair()))


def create_account(username):
    keypair = generate_keypair()

    account = {
        'verifying_key': keypair.verifying_key,
        'signing_key': keypair.signing_key,
        'username': username
    }

    f = open('.account', 'w')
    json_account = json.dumps(account)
    f.write(json_account)
    f.close()
    return (account)


if __name__ == '__main__':
    isAccoutExist = os.path.exists('.account')
    if isAccoutExist:
        print("this client already exists an account.")
        sys.exit()
    if not len(sys.argv) == 2:
        print("Please provide one parameter of username!")
        sys.exit()
    username = sys.argv[1]
    # username = input ('Please input an username:\n')
    print(json.dumps(create_account(username), indent=4))
