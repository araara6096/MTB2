def encrypt(secret, key):
    encrypted = []

    for letter in secret:
        if letter.isalpha():
            encrypted.append(chr(((ord(letter) - 97 + key) % 26) + 65))
        else:
            encrypted.append(letter)

    return "".join(encrypted)

def decrypt(secret, key):
    decrypted = []

    for letter in secret:
        if letter.isalpha():
            decrypted.append(chr(((ord(letter) - 65 - key) % 26) + 97))
        else:
            decrypted.append(letter)

    return "".join(decrypted)

secret = str(input("Enter the secret: "))

key = int(input("Enter the key: "))

encrypted = encrypt(secret, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)