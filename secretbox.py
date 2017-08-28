import base58
import nacl.utils
from nacl import bindings as c
from cryptoconditions import crypto


def secretbox():
    msg = "hello peter"
    nonce = base58.b58encode(nacl.utils.random(24))
    private_key, public_key = (k.decode() for k in crypto.ed25519_generate_key_pair())
    print("msg:        ", msg)
    print("nonce:      ", nonce)
    print("private_key:", private_key)
    ciphertext = c.crypto_secretbox(msg.encode(), base58.b58decode(nonce), base58.b58decode(private_key))
    msg2 = c.crypto_secretbox_open(ciphertext, base58.b58decode(nonce), base58.b58decode(private_key))
    print("msg2:       ", msg2)

secretbox()
