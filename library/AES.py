from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
import base64

class aes:
    @staticmethod
    def enc(text, password):
        key = sha256(password.encode()).digest()

        cipher = AES.new(key, AES.MODE_EAX)
        data, tag = cipher.encrypt_and_digest(text.encode())

        hasil = (
            base64.b64encode(cipher.nonce).decode() + "." +
            base64.b64encode(tag).decode() + "." +
            base64.b64encode(data).decode()
        )

        return hasil

    @staticmethod
    def dec(data, password):
        key = sha256(password.encode()).digest()

        nonce, tag, ciphertext = data.split(".")

        nonce = base64.b64decode(nonce)
        tag = base64.b64decode(tag)
        ciphertext = base64.b64decode(ciphertext)

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode()