import base58
import nacl.utils
from nacl import bindings as c
from nacl.exceptions import CryptoError


def secretbox(private, plaintext):
    nonce = base58.b58encode(nacl.utils.random(24))
    ciphertext = base58.b58encode(
        c.crypto_secretbox(plaintext.encode(), base58.b58decode(nonce), base58.b58decode(private)))

    return ciphertext, nonce


def open_secretbox(private, ciphertext, nonce):
    try:
        plaintext = c.crypto_secretbox_open(base58.b58decode(ciphertext), base58.b58decode(nonce),
                                            base58.b58decode(private))
    except CryptoError:
        msg = "Decryption failed. Ciphertext failed verification.\n"+"（解密失败，用户将留言设置为私密）"
        return msg.encode('utf-8')
    return plaintext


if __name__ == '__main__':
    print(open_secretbox("6iXMPtr7oT4ch1GXFFaiqexHNPFemN54oFwHiH4kAFDG",
                         "2o459znSXS1tHkRVhQxtZj3cM1SvhtEzsdzvGHeBJbE2eCsDpiT",
                         "HSYZo8HrMTRV4HAzmgJHje6ELQWPz1xU5").decode())
    print(open_secretbox("UzGKkAkBMbjrkTgYjSExGAZsgnTMFpKeahCxHfjPhUW",
                         "2o459znSXS1tHkRVhQxtZj3cM1SvhtEzsdzvGHeBJbE2eCsDpiT",
                         "HSYZo8HrMTRV4HAzmgJHje6ELQWPz1xU5").decode())
5
