import numpy as np;

letters = [chr(i) for i in range(65, ord('I'))] + [chr(i) for i in range(ord('J')+1, 91)]

key = str(input("Enter the key: ")).replace(" ", "").upper()

if 'I' not in key and 'J' not in key:
    key += 'I'

key = list(dict.fromkeys(list(key) + letters))

print(np.array(key).reshape(-1, 5))

def encrypt(secret):
    msg = list(secret.replace(" ", "").upper())
    crypted = []

    if len(msg) % 2:
        msg.append('X')
    
    for i in range(0, len(msg), 2):
        if msg[i] == 'J':
            msg[i] = 'I'
        if msg[i+1] == 'J':
            msg[i+1] = 'I'
        
        a = key.index(msg[i])
        b = key.index(msg[i+1])

        rowA, rowB = a // 5, b // 5
        colA, colB = a % 5, b % 5

        if rowA == rowB:
            crypted.append(key[(a+1) % 5 + rowA * 5])
            crypted.append(key[(b+1) % 5 + rowB * 5])
        elif colA == colB:
            crypted.append(key[(a+5) % 25])
            crypted.append(key[(b+5) % 25])
        else:
            crypted.append(key[rowA * 5 + colB % 5])
            crypted.append(key[rowB * 5 + colA % 5])
    
    return "".join(crypted)

def decrypt(secret):
    msg = list(secret.replace(" ", "").upper())
    decrypted = []

    for i in range(0, len(msg), 2):
        a = key.index(msg[i])
        b = key.index(msg[i+1])

        rowA, rowB = a // 5, b // 5
        colA, colB = a % 5, b % 5

        if rowA == rowB:
            decrypted.append(key[(a-1) % 5 + rowA * 5])
            decrypted.append(key[(b-1) % 5 + rowB * 5])
        elif colA == colB:
            decrypted.append(key[(a-5) % 25])
            decrypted.append(key[(b-5) % 25])
        else:
            decrypted.append(key[rowA * 5 + colB % 5])
            decrypted.append(key[rowB * 5 + colA % 5])
    
    return "".join(decrypted)

while True:
    secret = str(input("Enter the secret: ")).replace(" ", "").upper()

    for i in range(65, 65+26):
        double = chr(i) * 2
        fixed = chr(i) + 'X' + chr(i) 
        secret = secret.replace(double, fixed)

    encrypted = encrypt(secret)
    decrypted = decrypt(encrypted)

    print("Encrypted: ", encrypted)
    print("Decrypted: ", decrypted)

    if input("Continue? (y/n)") == 'n':
        break