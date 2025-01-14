import base64, binascii
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

class EncryptionUtil():
    iv = b'\x00'*16
    
    @staticmethod
    def aesDecryptFromBase64(clearText, keyBase64):
        pass

    @staticmethod
    def aesDecryptFromBase64(encryptedText, selfEncryptionKey):
        ciphertext = binascii.a2b_base64(encryptedText)
        key = binascii.a2b_base64(selfEncryptionKey)
        cipher = Cipher(algorithms.AES(key), modes.CTR(EncryptionUtil.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        # Unpad the plaintext using PKCS7 padding
        padder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = padder.update(plaintext) + padder.finalize()

        # Print the decrypted plaintext
        return plaintext.decode('utf-8')
    
    @staticmethod
    def generateRSAKeyPair():
        pass

    @staticmethod
    def generateAESKeyBase64():
        pass

    @staticmethod
    def rsaDecryptFromBase64(cipherText, privateKeyBase64):
        pass

    @staticmethod
    def rsaEncryptToBase64(clearText, publicKeyBase64):
        pass

    @staticmethod
    def signSHA256RSA(input_data, private_key):
        hash_data = SHA256.new(input_data.encode('utf-8'))
        signature = pkcs1_15.new(private_key).sign(hash_data)
        return base64.b64encode(signature).decode('utf-8')
    
    @staticmethod
    def publicKeyFromBase64(s):
        pass

    @staticmethod
    def privateKeyFromBase64(s):
        key_bytes = base64.b64decode(s.encode('utf-8'))
        key_spec = RSA.import_key(key_bytes)
        return key_spec

    