# Import Library
import os
import json
import hashlib
from colorama import init, Fore
from pathlib import Path
from Tool_Option import tool_option

# Initialize color output
init(autoreset=True)

# File's Relative Path for storing Hash

BASE_dir = Path(__file__).resolve().parent                          # Find the script directory

DATA_dir = BASE_dir.parent / "DATA"                                 # Find DATA directory

FILE_INTEGRITY_dir = DATA_dir / "File_Integrity_Data"               # Find File_Integrity_Data directory

HASH_FILE = FILE_INTEGRITY_dir / "File_Hash" / "hash_storage.json"  # Find hash file 


# Calculate SHA-256 hash of a file
def cal_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:    # "rb" = read as binary  
        while True:
            data = f.read(65536)        # Read 64KB chunks
            if not data:
                break
            sha256.update(data)

    # Return the hash in HEX
    return sha256.hexdigest()


# List only files in the selected folder
def list_files(folder):
    # File list
    files = []

    # Scan for file in a directory
    for item in os.listdir(folder):

        # Get the files full paths
        full_path = os.path.join(folder, item)  # Combine file/folder path and name 

        if os.path.isfile(full_path):           # Check if it is a file and not a folder
            files.append(full_path)             # Append the file path to file list

    return files


# Load hashes from JSON file
def load_hashes():
    # Handling for file existence
    if not HASH_FILE.exists():                  # Check for json file existence
        HASH_FILE.parent.mkdir(exist_ok=True)   # If the file folder not exist make one
        HASH_FILE.write_text("{}")              # Then create an empty json file

    with open(HASH_FILE, "r") as f:             # Open hash file as read
        try:
            return json.load(f)                 # Try to convert file content to python Dict or List
        except json.JSONDecodeError:
            return {}                           # If file empty or invalid, return empty Dict

# Save hash to JSON file
def save_hash(file_path, file_hash):
    data = load_hashes()                # Use the load hash func

    data[file_path] = {                 # Add/Update data for the file with this path
        "hash": file_hash,
        "algorithm": "SHA-256"
    }

    with open(HASH_FILE, "w") as f:     # Add/Update the hash storage using the data
        json.dump(data, f, indent=4)

    print(Fore.GREEN + "Hash saved successfully")


# Compare current hash with stored hash
def compare_hash(file_path, current_hash):
    data = load_hashes()        # Use the load hash file func

    if file_path not in data:   # Check for a file's hash data using its file path
        print(Fore.YELLOW + "No stored hash for this file")
        return

    saved_hash = data[file_path]["hash"]                # Get original hash of the file

    if saved_hash == current_hash:                      # Compare the hashes
        print(Fore.GREEN + "File integrity OK")
    else:
        print(Fore.RED + "File has been modified")


# Main program
def main():
    tool_option.loading_display()
    tool_option.clear_after(0.1)

    while True:
        print("┌───────────────────────────┐")
        print("│   File Integrity Checker  │")
        print("└───────────────────────────┘\n")

        print("    >> Press S to Start")
        print("    >> Press E to Exit")
        print("-----------------------------------")

        choice = input("Choice >> ").upper() 
        if choice == "S":
            print("Program Starting.")
            
            folder = FILE_INTEGRITY_dir / "Import_File"
            files = list_files(folder)

            if not files:
                print(Fore.YELLOW + "No files found in this folder")
                return

            print(Fore.CYAN + "\nFiles found:")
            for i, file in enumerate(files):
                print(f"    >> {i + 1}. {os.path.basename(file)}")

            # Select file
            file_selected = False
            while not file_selected:    # Only continue if file is selected
                
                try:
                    file_choice = int(input("\nSelect file number: ")) - 1

                    if file_choice < 0 or file_choice >= len(files):
                        print(Fore.RED + "Invalid number. Please select the numbers from the list.")
                        continue
                    else:
                        selected_file = files[file_choice]
                        print(Fore.GREEN + f"File: {os.path.basename(selected_file)} selected.")
                        break
                    
                except ValueError:
                    print(Fore.RED + "Invalid input. Please enter a number only.")
                    continue

            file_hash = cal_hash(selected_file)
            print(Fore.CYAN + f"\nSHA-256 Hash:\n{file_hash}")

            print(Fore.RED + "\nOperation:")
            print("    >> 1. Save hash")
            print("    >> 2. Compare hash")

            option = input("\nChoose option: ")
            if option == "1":
                save_hash(selected_file, file_hash)
            elif option == "2":
                compare_hash(selected_file, file_hash)
            else:
                print(Fore.RED + "Invalid option")
                continue
        elif choice == "E":
            print("Exiting Program.")
            break
        else:
            print("Invalid Option!")

# Main Guard
if __name__ == "__main__":
    main()
