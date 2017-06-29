import nacl.secret
import nacl.utils
import base64
import os


class SecureMessage:

    @staticmethod
    def generate_key():
        return nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE)

    @staticmethod
    def encrypt(message):
        if message:
            box = nacl.secret.SecretBox(bytes(os.environ.get('SECRET_KEY'), 'iso-8859-1'))
            cypher_text = box.encrypt(bytes(message, "utf-8"))
            encoded_cypher_text = base64.urlsafe_b64encode(cypher_text)
            return encoded_cypher_text
        else:
            return None

    @staticmethod
    def decrypt(token64):
        if token64:
            token = base64.urlsafe_b64decode(token64)
            box = nacl.secret.SecretBox(bytes(os.environ.get('SECRET_KEY'), 'iso-8859-1'))
            decrypted_token = box.decrypt(token)
            string_decrypted_token = decrypted_token.decode("utf-8")
            return string_decrypted_token
        else:
            return None
