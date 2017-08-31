import base58
import nacl.utils
from nacl import bindings as c


def secretbox(private, plaintext):
    nonce = base58.b58encode(nacl.utils.random(24))
    ciphertext = base58.b58encode(
        c.crypto_secretbox(plaintext.encode(), base58.b58decode(nonce), base58.b58decode(private)))

    return ciphertext, nonce


def open_secretbox(private, ciphertext, nonce):
    plaintext = c.crypto_secretbox_open(base58.b58decode(ciphertext), base58.b58decode(nonce),
                                        base58.b58decode(private))
    return plaintext


if __name__ == '__main__':
    print(open_secretbox("6iXMPtr7oT4ch1GXFFaiqexHNPFemN54oFwHiH4kAFDG",
                         "2o459znSXS1tHkRVhQxtZj3cM1SvhtEzsdzvGHeBJbE2eCsDpiT",
                         "HSYZo8HrMTRV4HAzmgJHje6ELQWPz1xU5").decode())
