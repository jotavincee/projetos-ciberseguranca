
#!/usr/bin/env python3
"""
SECURE SECRETS MANAGER
Information Security | Cryptography
"""

import argparse
import base64
import getpass
import json
import os

from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

from cryptography.hazmat.primitives import hashes

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


VAULT = Path("vault.enc")
SALT_FILE = Path("vault.salt")


def derive_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600000
    )

    return base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )


def load_vault(password):

    if not VAULT.exists():
        return {}

    if not SALT_FILE.exists():
        raise ValueError("Salt file missing.")

    salt = SALT_FILE.read_bytes()

    key = derive_key(password, salt)

    cipher = Fernet(key)

    try:

        decrypted = cipher.decrypt(
            VAULT.read_bytes()
        )

        return json.loads(decrypted.decode())

    except InvalidToken:

        raise ValueError(
            "Incorrect password or invalid vault."
        )


def save_vault(password, data):

    if SALT_FILE.exists():
        salt = SALT_FILE.read_bytes()

    else:
        salt = os.urandom(16)
        SALT_FILE.write_bytes(salt)

    key = derive_key(password, salt)

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        json.dumps(data).encode()
    )

    VAULT.write_bytes(encrypted)

    try:
        os.chmod(VAULT, 0o600)
        os.chmod(SALT_FILE, 0o600)
    except OSError:
        pass


def main():

    parser = argparse.ArgumentParser(
        description="Secure Secrets Manager"
    )

    commands = parser.add_subparsers(
        dest="command",
        required=True
    )

    add = commands.add_parser("set")
    add.add_argument("name")

    get = commands.add_parser("get")
    get.add_argument("name")

    commands.add_parser("list")

    args = parser.parse_args()

    password = getpass.getpass(
        "Master password: "
    )

    data = load_vault(password)

    if args.command == "set":

        secret = getpass.getpass(
            "Secret value: "
        )

        data[args.name] = secret

        save_vault(password, data)

        print("Secret stored successfully.")

    elif args.command == "get":

        if args.name not in data:
            print("Secret not found.")
            return

        print(data[args.name])

    elif args.command == "list":

        print("\nStored secrets:")

        for name in sorted(data):
            print("-", name)


if __name__ == "__main__":
    main()
