import numpy as np;

key = str(input("Enter the key: ")).replace(" ", "").upper()

def encrypt(secret):
    msg = list(secret.replace(" ", "").upper())
    keys = key * (len(msg) // len(key) + 1)

    print(msg)
    print(keys)
    crypted = []

    for i in range(0, len(msg)):
        x = ord(msg[i]) - 65
        y = ord(keys[i]) - 65

        crypted.append(chr(((x ^ y) % 26) + 65))

    return "".join(crypted)

def decrypt(secret):
    msg = list(secret.replace(" ", "").upper())
    keys = key * (len(msg) // len(key) + 1)

    print(msg)
    print(keys)

    crypted = []

    for i in range(0, len(msg)):
        x = ord(msg[i]) - 65
        y = ord(keys[i]) - 65

        crypted.append(chr(((x ^ y) % 26) + 65))

    return "".join(crypted)

while True:
    secret = str(input("Enter the secret: "))

    encrypted = encrypt(secret)
    decrypted = decrypt(encrypted)

    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

    if input("Continue? (y/n)") == 'n':
        break