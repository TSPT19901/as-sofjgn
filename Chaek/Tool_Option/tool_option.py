from Password_Strengh_Analyzer import Password_Strengh_Analyzer
from Encryption_Decryption import Encryption_Decryption

def tool_option(username):
    while True:
        
        print("\n==============================")
        print("     SECURITY TOOLKIT MENU")
        print("==============================")
        print("  [1] Password Strength Analyzer")
        print("  [2] File Integrity Checker")
        print("  [3] Encryption/Decryption")
        print("  [4] Exit")
        print("==============================")
        
        choice = input("Select: ")
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid!!!")
            print("Input Only [1], [2], [3], [4]\n")
        elif choice == "1":
            Password_Strengh_Analyzer.main_password_check(username)
            continue
        elif choice == "2":
            pass
        elif choice == "3":
            Encryption_Decryption.display_and_execute()
        elif choice == "4":
            break

# def update()