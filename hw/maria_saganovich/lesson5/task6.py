from cryptography.fernet import Fernet


def func_encryption(msg: str) -> list:
    key = Fernet.generate_key()
    fernet = Fernet(key)
    enc_code = fernet.encrypt(msg.encode())
    return [key, enc_code]


def func6(key: bytes, secret_msg: bytes) -> str:
    fernet = Fernet(key)
    return fernet.decrypt(secret_msg).decode()
