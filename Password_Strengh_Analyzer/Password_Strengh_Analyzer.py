from getpass import getpass

dict_file_history = {} #store username with file.txt to file : history_dict.txt

dict_temp = {} #use as temp for store every history of each user

def load_data(filename):#load data from file store in dictionary
    file = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                 continue
            if "=" in line:
                key, value = line.split("=", 1)
                file[key.strip()] = value.strip()
    return file

def save_data_to_File(dict, filename, key, value):#save data from dictionary to file
    dict[key] = value
    with open(filename, "a") as file:
        file.write(f"{key} = {value}\n")


def main_password_check(username):
    while True:

        print("┌───────────────────────────────┐")
        print("│   Password Strength Analyzer  │")
        print("└───────────────────────────────┘\n")

        print("    >> Press C to Check Password")
        print("    >> Press H to History")
        print("    >> Press E to Exis\n")
        print("-----------------------------------")

        choice = input("Choice >> ").upper()

        if choice not in ["C", "H", "E"]:
            print("Invalid!!!")
            print("Input Only [C], [H], [E]\n")
        elif choice == "C":
            check_password(username)
            continue
        elif choice == "H":
            display_history(username)
            continue
        elif choice == "E":
            break

class Password:
    def __init__(self, input_password):
        self.PW_str = input_password 

    def check_is_Num(self):
        number = "1234567890"
        for character in self.PW_str:
            if(character in number):  #number check
                return True

    def check_is_Case(self):
        upper = False
        lower = False
        for character in self.PW_str:
            if character.isupper():
                upper = True
            if character.islower():
                lower = True    
        return upper and lower
    
    def check_is_SC(self):
        special= r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
        for character in self.PW_str:
            if character in special:
                return True
    
    def check_is_char(self):
        for character in self.PW_str:
            if "a" <= character <= "z" or "A" <= character <= "Z":
                return True
class Character_12(Password):
    
    def check_percentage(self):
        temp = None
        if self.check_is_Case() and self.check_is_Num() and self.check_is_SC():
            temp = 99
            print("Password strengh: 99%")
            print("Your password is extremely strong. Perfect!")
        elif self.check_is_Case() and self.check_is_Num():
            temp = 95
            print("Password strengh: 95%")
            print("Excellent! But adding a special character can make it even stronger.")
        return temp
        
class Character_8(Password):
    
    def check_percentage(self):
        temp = None
        if len(self.PW_str) < 8:
            temp = 30
            print("Password strengh: 30%")
            print("Your password is too short. Please use at least 8 characters!!!\n\n")
        else:
            if self.check_is_Case() and self.check_is_Num() and self.check_is_SC():
                temp = 90
                print("Password strengh: 90%")
                print("Great! Your password is very strong and secure.\n\n")
            elif self.check_is_Case() and self.check_is_Num():
                temp = 80
                print("Password strengh: 80%")
                print("Good job, but adding a special character can make it even better.\n\n")

            elif self.check_is_Num() and self.check_is_char():
                temp = 50
                print("Password strengh: 50%")
                print("Your password still weak. Add uppercase letters and special characters for better protection.\n\n")
            elif self.check_is_Num():
                temp = 40
                print("Password strengh: 40%")
                print("Your password is weak. Try adding letters or special characters to make it stronger.\n\n")
        return temp
    
def check_password(username):
    user_input = input("Enter your password to check:")

    if len(user_input) > 20:
        print("Your password too long!!!")
    elif len(user_input) < 12:
        C_8 = Character_8(user_input)  

        save_history_data_to_file(username, user_input, C_8.check_percentage())
    else:
        C_12 = Character_12(user_input)

        save_history_data_to_file(username, user_input, C_12.check_percentage())

dict_file_history = load_data("DATA/history_dict.txt")

def history_account(username): #store data username with their history account
    dict_file_history[username] = "History_each_user/" + username + ".txt"
    
    save_data_to_File(dict_file_history, "DATA/history_dict.txt", username,dict_file_history[username])

def create_file_each_user_account(username):#create file for each account use in signup function
    
    if username in dict_file_history:
        with open(dict_file_history[username], "a"):
            pass

def save_history_data_to_file(username, password, percent):#record data after check strengh password
    save_data_to_File(dict_temp, dict_file_history[username], password, percent)

def display_history(username):
    
    dict_temp = load_data(dict_file_history[username])

    print("╔════════════════════════════╦════════════════════╗")
    print("║       Password Check       ║   Result (%)       ║")
    print("╠════════════════════════════╬════════════════════╣")

    for key, value in dict_temp.items():
        print("║ {:26} ║ {:18} ║".format(key, value))

    print("╚════════════════════════════╩════════════════════╝")