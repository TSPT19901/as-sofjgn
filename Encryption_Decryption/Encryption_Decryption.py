import rsa
import os
import ast
from Tool_Option import tool_option

# create a base Key class
class Key:
    def __init__(self, public_key=None, private_key=None):
        self.__public_key = public_key
        self.__private_key = private_key
#create the functon to get public/private key from init function
    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key
#function to generate key(both public and private)
    def new_key(self):
        self.__public_key, self.__private_key = rsa.newkeys(2048)
        return self.__public_key, self.__private_key
#function for save both key to file.pem 
    def save_public_key(self, filename="Encryption_Decryption/public.pem"):
        with open(filename, "wb") as f:
            f.write(self.__public_key.save_pkcs1("PEM"))

    def save_private_key(self, filename="Encryption_Decryption/private.pem"):
        with open(filename, "wb") as f:
            f.write(self.__private_key.save_pkcs1("PEM"))
#function to load key from file.pem
    def load_keys(self, pub_file="Encryption_Decryption/public.pem", priv_file="Encryption_Decryption/private.pem"):
        with open(pub_file, "rb") as f:
            self.__public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(priv_file, "rb") as f:
            self.__private_key = rsa.PrivateKey.load_pkcs1(f.read())

#create class for 2 methods encrypton and decryption
class EncryptionDecryption(Key):
    def encryption(self, msg):
        encrypted = rsa.encrypt(msg.encode(), self.get_public_key())
        return encrypted

    def decryption(self, encrypted):
        decrypted = rsa.decrypt(encrypted, self.get_private_key())
        return decrypted.decode()
#function to display and execute all methods here
def display_and_execute():
#style loading
    tool_option.loading_display()
    tool_option.clear_after(0.1)
    re_file =0 #variable for track if user start encrypt again or not 
    #create object using EncryptionDecryption class
    obj = EncryptionDecryption()
    #condition here to check is key file is existed or not
    if not os.path.exists("Encryption_Decryption/public.pem") or not os.path.exists("Encryption_Decryption/private.pem"):
        obj.new_key()
        obj.save_public_key()
        obj.save_private_key()
    else:
        obj.load_keys()              

    print("┌───────────────────────────────┐")
    print("│      Encryption/Decryption    │")
    print("└───────────────────────────────┘\n")    

    while True:
        print("\nPlease choose an option:\n[1] Encrypt text\n[2] Decrypt text\n[3] Exit")
        option = input("Option: ")
        #for option 1, when user encrypt the new text, file will override
        if option == "1":
            if re_file==0:
                text = input("Enter the text to encrypt: ")
                encrypted = obj.encryption(text)
                #we use encoding="utf-8" to tell python how to covert data from byte to string for save to file 
                with open("Encryption_Decryption/HistoryText.txt", "w", encoding="utf-8") as f:
                    #we use repr function to convert from byte to strign here 
                    #The file will be use to decrypt for entire text in the file 
                    f.write(repr(encrypted) + "\n") 
                re_file+=1
            elif re_file>0:
                text = input("Enter the text to encrypt: ")
                encrypted = obj.encryption(text)
                with open("Encryption_Decryption/HistoryText.txt", "a", encoding="utf-8") as f:
                    f.write(repr(encrypted) + "\n")
            print("\nEncrypted data:\n", encrypted)

        elif option == "2":
            file_name= input("Please input your file name: ")
            if (file_name.startswith('"') and file_name.endswith('"')) or (file_name.startswith("'") and file_name.endswith("'")):
                file_name = file_name[1:-1]
            #to check if encrypted file is exist or not 
            if not os.path.exists(file_name):
                print("No history found.")
                continue
            #then if file is existed, open that file and start reading 
            with open(file_name, "r", encoding="utf-8") as f:
                lines = f.readlines()
            print("\nDecrypted messages:")
            for line in lines:
                #we make new variable and use ast.literal_eval to convert back from strign to byte
                encrypted_bytes = ast.literal_eval(line.strip())  # use .strip() to eliminate or skip the new line
                #after convert, we can call our function decryption
                decrypted_text = obj.decryption(encrypted_bytes)
                print(decrypted_text)

        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please choose 1, 2, or 3.")

