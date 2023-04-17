import numpy as np

letters = [chr(x + 65) for x in range(26)]
#it creates a list containing uppercase alphabet letters
print("".join(letters))
#concatenates the list into a single string

np.random.shuffle(letters)
#shuffle the letters randomly
print("".join(letters))

def encrypt(secret):
    encrypted = []

    for letter in secret:
        if letter.isalpha():
            encrypted.append(letters[ord(letter) - 97])
            #if the current character is a letter then it adds the corresponding shuffled letter.
        else:
            encrypted.append(letter)
    return "".join(encrypted)

def decrypt(secret):
    decrypted = []

    for letter in secret:
        if letter.isalpha():
            decrypted.append(chr(letters.index(letter) + 97)
            #this line adds corresponding unshuffled letter
        else:
            decrypted.append(letter)

    return "".join(decrypted)

secret = str(input("Enter the secret: "))

encrypted = encrypt(secret)
decrypted = decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)