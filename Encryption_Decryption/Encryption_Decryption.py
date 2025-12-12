import rsa
import os
import ast

class Key:
    def __init__(self, public_key=None, private_key=None):
        self.__public_key = public_key
        self.__private_key = private_key

    def get_public_key(self):
        return self.__public_key

    def get_private_key(self):
        return self.__private_key

    def new_key(self):
        self.__public_key, self.__private_key = rsa.newkeys(2048)
        return self.__public_key, self.__private_key

    def save_public_key(self, filename="Encryption_Decryption/public.pem"):
        with open(filename, "wb") as f:
            f.write(self.__public_key.save_pkcs1("PEM"))

    def save_private_key(self, filename="Encryption_Decryption/private.pem"):
        with open(filename, "wb") as f:
            f.write(self.__private_key.save_pkcs1("PEM"))

    def load_keys(self, pub_file="Encryption_Decryption/public.pem", priv_file="Encryption_Decryption/private.pem"):
        with open(pub_file, "rb") as f:
            self.__public_key = rsa.PublicKey.load_pkcs1(f.read())
        with open(priv_file, "rb") as f:
            self.__private_key = rsa.PrivateKey.load_pkcs1(f.read())


class EncryptionDecryption(Key):
    def encryption(self, msg):
        encrypted = rsa.encrypt(msg.encode(), self.get_public_key())
        return encrypted

    def decryption(self, encrypted):
        decrypted = rsa.decrypt(encrypted, self.get_private_key())
        return decrypted.decode()

def display_and_execute():
    re_file =0
    obj = EncryptionDecryption()
    if not os.path.exists("Encryption_Decryption/public.pem") or not os.path.exists("Encryption_Decryption/private.pem"):
        obj.new_key()
        obj.save_public_key()
        obj.save_private_key()
    else:
        obj.load_keys()              

    print("Welcome to Encryption/Decryption Tool!")

    while True:
        print("\nPlease choose an option:\n1. Encrypt text\n2. Decrypt text\n3. Exit")
        option = input("Option: ")
        if option == "1":
            if re_file==0:
                text = input("Enter the text to encrypt: ")
                encrypted = obj.encryption(text)
                with open("Encryption_Decryption/HistoryText.txt", "w", encoding="utf-8") as f:
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
            if not os.path.exists(file_name):
                print("No history found.")
                continue
            with open(file_name, "r", encoding="utf-8") as f:
                lines = f.readlines()
            print("\nDecrypted messages:")
            for line in lines:
                encrypted_bytes = ast.literal_eval(line.strip())
                decrypted_text = obj.decryption(encrypted_bytes)
                print(decrypted_text)

        elif option == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid option! Please choose 1, 2, or 3.")

