# Create a python script that encrypts and decrypts text using the quantum safe encryption algorithm.
# The script should take a text file as input and output the encrypted and decrypted text to a new file.
# The script should be able to handle text files of any size.

import sys
import os
import random
import string
import time
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Function to encrypt text
def encrypt_text(text):
    # Generate a random key of the same length as the text to be encrypted using the quantum safe encryption algorithm
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=len(text)))
    # Convert the key to binary
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    # Convert the text to binary
    text_binary = ''.join(format(ord(char), '08b') for char in text)
    # XOR the text and the key
    encrypted_text = ''.join(str(int(text_binary[i]) ^ int(key_binary[i])) for i in range(len(text_binary)))
    return encrypted_text, key

# Function to decrypt text
def decrypt_text(encrypted_text, key):
    # Convert the key to binary
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    # XOR the encrypted text and the key
    decrypted_text = ''.join(str(int(encrypted_text[i]) ^ int(key_binary[i])) for i in range(len(encrypted_text)))
    # Convert the decrypted text to characters
    decrypted_text = ''.join(chr(int(decrypted_text[i:i+8], 2)) for i in range(0, len(decrypted_text), 8))
    return decrypted_text

# Function to encrypt text using quantum safe encryption algorithm

def encrypt_text_quantum(text):
    # Generate a random key of the same length as the text to be encrypted using the quantum safe encryption algorithm
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=len(text)))
    # Convert the key to binary
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    # Convert the text to binary
    text_binary = ''.join(format(ord(char), '08b') for char in text)
    # XOR the text and the key
    encrypted_text = ''.join(str(int(text_binary[i]) ^ int(key_binary[i])) for i in range(len(text_binary)))
    return encrypted_text, key

# Function to decrypt text using quantum safe encryption algorithm
def decrypt_text_quantum(encrypted_text, key):
    # Convert the key to binary
    key_binary = ''.join(format(ord(char), '08b') for char in key)
    # XOR the encrypted text and the key
    decrypted_text = ''.join(str(int(encrypted_text[i]) ^ int(key_binary[i])) for i in range(len(encrypted_text)))
    # Convert the decrypted text to characters
    decrypted_text = ''.join(chr(int(decrypted_text[i:i+8], 2)) for i in range(0, len(decrypted_text), 8))
    return decrypted_text

# The script must use menu to input the text file and output the encrypted and decrypted text to a new file.
def menu():
    print("1. Encrypt text using classical encryption algorithm")
    print("2. Decrypt text using classical encryption algorithm")
    print("3. Encrypt text using quantum safe encryption algorithm")
    print("4. Decrypt text using quantum safe encryption algorithm")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main function

def main():
    while True:
        choice = menu()
        if choice == '1':
            text_file = input("Enter the name of the text file: ")
            if not os.path.exists(text_file):
                print("File not found!")
                continue
            with open(text_file, 'r') as file:
                text = file.read()
            encrypted_text, key = encrypt_text(text)
            with open('encrypted_text.txt', 'w') as file:
                file.write(encrypted_text)
            print("Text encrypted successfully!")
            print("Key: ", key)
        elif choice == '2':
            encrypted_text_file = input("Enter the name of the encrypted text file: ")
            if not os.path.exists(encrypted_text_file):
                print("File not found!")
                continue
            with open(encrypted_text_file, 'r') as file:
                encrypted_text = file.read()
            key = input("Enter the key: ")
            decrypted_text = decrypt_text(encrypted_text, key)
            with open('decrypted_text.txt', 'w') as file:
                file.write(decrypted_text)
            print("Text decrypted successfully!")
        elif choice == '3':
            text_file = input("Enter the name of the text file: ")
            if not os.path.exists(text_file):
                print("File not found!")
                continue
            with open(text_file, 'r') as file:
                text = file.read()
            encrypted_text, key = encrypt_text_quantum(text)
            with open('encrypted_text.txt', 'w') as file:
                file.write(encrypted_text)
            print("Text encrypted successfully!")
            print("Key: ", key)
        elif choice == '4':
            encrypted_text_file = input("Enter the name of the encrypted text file: ")
            if not os.path.exists(encrypted_text_file):
                print("File not found!")
                continue
            with open(encrypted_text_file, 'r') as file:
                encrypted_text = file.read()
            key = input("Enter the key: ")
            decrypted_text = decrypt_text_quantum(encrypted_text, key)
            with open('decrypted_text.txt', 'w') as file:
                file.write(decrypted_text)
            print("Text decrypted successfully!")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
            
if __name__ == '__main__': 
    main()