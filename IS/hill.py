import numpy as np

multi_inv = {
    1: 1,
    3: 9,
    5: 21,
    7: 15,
    9: 3,
    11: 19,
    15: 7,
    17: 23,
    19: 11,
    21: 5,
    23: 17,
    25: 25
}

def encrypt(secret, key):
    msg = np.array([ord(x) - 65 for x in secret])

    encrypted = ""

    if len(msg) % len(key) != 0:
        msg = np.append(msg, [23] * (len(key) - (len(msg) % len(key))))
    
    msg = msg.reshape((-1, len(key)))
    key = np.array(key)

    for triplet in msg:
        multed = np.matmul(triplet, key) % 26
        encrypted += "".join([chr(x + 65) for x in multed])

    return encrypted

def decrypt(secret, key):
    msg = np.array([ord(x) - 65 for x in secret])

    decrypted = ""
    
    msg = msg.reshape((-1, len(key)))
    det = int(np.linalg.det(key))

    inv = np.round_(det * np.linalg.inv(key) * multi_inv[det % 26]).astype(int) % 26

    for triplet in msg:
        multed = np.matmul(triplet, inv) % 26
        decrypted += "".join([chr(x + 65) for x in multed])

    return decrypted

secret = str(input("Enter the secret to encrypt: ")).replace(" ", "").upper()

dims = int(input("Enter the dimensions of the key: "))

key = np.array(list(map(int, input("Enter the key: ").strip().split(" ")))).reshape((dims, dims))

encrypted = encrypt(secret, key)

victim = str(input("Enter the secret to decrypt: ")).replace(" ", "").upper()

decrypted = decrypt(victim, key)

print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)
