#   a212_rsa_encrypt.py
import rsa as rsa
properKeyProvided = False

while (properKeyProvided == False):
    key = input("Enter the Encryption Key: " )
    mod_value = input("Enter the Modulus: " )
    plaintext = input("Enter a message to encrypt: ")
    if (key.isdigit() and mod_value.isdigit()):
        encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
        print("Encrypted Message:", encrypted_msg)
        properKeyProvided = True
    else:
        print("Nuh uh.")