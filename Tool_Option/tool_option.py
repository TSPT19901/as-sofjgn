#import module to make connection each other 
from Password_Strength_Analyzer import Password_Strength_Analyzer
from Encryption_Decryption import Encryption_Decryption
import os
import time
import sys

#display option for users
def tool_option(username):
    loading_display()
    clear_after(0.1)
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
            #get into Password strength analyzer for using tool
            Password_Strength_Analyzer.main_password_check(username)
            continue
        elif choice == "2":
            pass
        elif choice == "3":
            #get into Encryption/Decryption for using tool
            Encryption_Decryption.display_and_execute()
        elif choice == "4":
            break

#function clear previous screen
def clear_after(seconds):
    time.sleep(seconds)
    os.system('cls' if os.name == 'nt' else 'clear')
#function display loading...
def loading_display():
    for i in range(10):
        sys.stdout.write("\r       Loading" + "." * (i % 4))
        sys.stdout.flush()
        time.sleep(0.5)