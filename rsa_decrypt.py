#   a212_rsa_decrypt.py
import rsa as rsa
import validateinput
properKeyProvided = False

while (properKeyProvided == False):
    key = input("Enter the Decryption Key: " )
    mod_value = input("Enter the Modulus: " )
    encrypted_msg = input("What message would you like to decrypt (No brackets): ")
    if (validateinput.ValidateInteger(key) and validateinput.ValidateInteger(mod_value)):
        msg = encrypted_msg.split(", ")
        print (rsa.decrypt(key,mod_value , msg))
        properKeyProvided = True
    else:
        print("Nuh uh.")

#break apart the list that is cut/copied over on ", "
