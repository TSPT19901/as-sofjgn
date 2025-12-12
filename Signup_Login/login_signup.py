from Tool_Option import tool_option
from Password_Strengh_Analyzer import Password_Strengh_Analyzer
from getpass import getpass

dict_store_account = {} #store username password to file : account.txt

def load_data(filename):#load data from file store in dictionary
    file = {}
    try:
        f = open(filename, "r")
    except Exception:
        print("File not exist")
    else:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                file[key.strip()] = value.strip()
        f.close()
        return file

def save_data_to_File(dict, filename, key, value):#save data from dictionary to file
    dict[key] = value
    with open(filename, "a") as file:
        file.write(f"{key} = {value}\n")


def sign_up_login():
    while True:
        
        print("┌───────────────────────────────┐")
        print("│   PERSONAL SECURITY TOOLKIT   │")
        print("└───────────────────────────────┘\n")

        print("    >> Press L to Login")
        print("    >> Press S to Sign Up")
        print("    >> Press E to Exit program\n")

        print("-----------------------------------")
        
        input_choice = input("Choice >> ").upper()

        if input_choice not in ["S", "L", "E"]:
            print("\n\n")
            print("Invalid!!!")
            print("Input Only [S], [L], [E]\n")
        elif input_choice == "L":
            login()
            
            continue
        elif input_choice == "S":
            sign_up()
            continue
        elif input_choice == "E":
            break

dict_store_account = load_data("DATA/account.txt")

def sign_up(): #Sign up account
    
    while True:
        username = input("Username: ")

        if len(username) > 20:
            print("Your username too long!\n\n\n")
            continue
        if username in dict_store_account:
            print("Username already exists!!\n\n\n")
            continue
        break
    while True:
        password = input("Password: ")  
        has_number= False
        has_upper=False
        has_special=False
        has_lower=False

        special= r"!#$%&()*+,-./:;<=>?@[\]^_`{|}~'"
        numbers='01234567890'
        
        if (len(password)<8):
            print("Please input at least 8 characters")
            continue
        if (len(password)>=8):
            for character in password:
                if(character.isupper()): #upper check
                    has_upper=True
                if(character in numbers):  #number check
                    has_number=True
                if(character in special):    #special check
                    has_special=True
                if (character.islower()):
                    has_lower=True        #lower check
        if (has_number and has_special and has_upper and has_lower):
            print("Sign up seccessfully!!!\n\n")
            save_data_to_File(dict_store_account, "DATA/account.txt", username, password)
            Password_Strengh_Analyzer.history_account(username)
            part = "History_each_user/" + username + ".txt"

            with open(part, "w"):
                pass
            break

class authentication:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def compare_private_password(self, password_attempt): #login account   
        if password_attempt == self.__password:
            print("Login successfully <3\n\n")

            tool_option.tool_option(self.username)
        else:
            print("Invalid password!!!\n\n")
      
    def getter_password(self):
        return self.__password    

def login(): #login account   
        username = input("Username: ")
        if username in dict_store_account:
            user1 = authentication(username , dict_store_account[username]) #object and pass value to attribute of class
            password = getpass("Password: ")
            user1.compare_private_password(password)
            
        else:
            print("Username does not exist!!!\n\n") 








