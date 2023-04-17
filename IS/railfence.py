import numpy as np

def encrypt(secret, depth):
    msg = np.array(list(secret))
    print(msg)
    if len(msg) % depth != 0:
        msg = np.append(msg, ['X'] * (depth - (len(msg) % depth)))
    print(msg)
    msg = msg.reshape((depth, -1), order='F')
    print(msg)
    return "".join(msg.flatten())

def decrypt(secret, depth):
    msg = np.array(list(secret))
    msg = msg.reshape((-1, depth), order='F')

    return "".join(msg.flatten())

secret = str(input("Enter the secret to encrypt: ")).replace(" ", "").upper()

depth = int(input("Enter the depth: "))

encrypted = encrypt(secret, depth)
decrypted = decrypt(encrypted, depth)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

