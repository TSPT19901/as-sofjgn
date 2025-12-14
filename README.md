# CHAEK Toolkit

A comprehensive Python toolkit for file integrity checking, password strength analysis, encryption/decryption, and utility management.  
This toolkit helps users secure files, verify integrity, and manage passwords efficiently.

---

## Features

- **File Integrity Checker**: Compute and store SHA-256 hashes for files, and compare them to detect modifications.  
- **Password Strength Analyzer**: Evaluate user passwords and provide security recommendations.  
- **Encryption/Decryption**: Encrypt or decrypt text files securely.  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/TSPT19901/Chaek.git
cd CHAEK
```

2. Install necessary libraries

```bash
pip install colorama
pip install rsa
```

3. Run the program
```bash
python -m main
```

---

## Notes

- JSON files (like `hash_storage.json`) are automatically created if missing.
- Python cache files (`__pycache__`) are auto-generated and ignored in Git.
- Make sure to run scripts from the project root (`cd CHAEK`) to avoid path errors.
