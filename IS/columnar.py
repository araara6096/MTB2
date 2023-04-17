import numpy as np

def encrypt(secret, depth, key):
    msg = np.array(list(secret)) 
    #converts secret into array

    encrypted = ""
    
    if len(msg) % depth != 0:
        msg = np.append(msg, ['X'] * (depth - len(msg) % depth))
        #checks if the length of msg is not divisible by depth and 'x' to the end of msg until it is divisible 
    
    msg = msg.reshape((depth, -1))[:, np.argsort(key)].T
    #first reshape msg into 2d array with depth rows,then sort the column using indices in key and then transpose the array.
    for group in msg:
        encrypted += "".join(group)
    #concatenate characters in each row of msg to encrypted string.
    return encrypted

def decrypt(secret, depth, key):
    msg = np.array(list(secret))

    decrypted = ""
    
    msg = msg.reshape((-1, depth)).T
    #reshape msg with depth col and transpose the array
    msg = msg[:, key]
    #sort the col using key
    for group in msg:
        decrypted += "".join(group)
    #concatenate msg to decrypted string
    return decrypted

secret = str(input("Enter the secret: ")).replace(" ", "").upper()
#takes input string and remove any spaces
depth = int(input("Enter the depth: "))

key = list(map(int, input("Enter the key: ").strip().split()))

if key == []:
    key = np.arange(len(secret) // depth + 1)

encrypted = encrypt(secret, depth, key)
double_encrypted = encrypt(encrypted, depth, key)

decrypted = decrypt(encrypted, depth, key)
double_decrypted = decrypt(decrypt(double_encrypted, depth, key), depth, key)

print("Encrypted: ", encrypted)
print("Double Encrypted: ", double_encrypted)

print("Decrypted: ", decrypted)
print("Double Decrypted: ", double_decrypted)