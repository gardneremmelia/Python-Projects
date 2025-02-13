"""
Emmelia Gardner
Class: CS 521 - Spring 1
Date: 2/3/25
Homework Problem # 3_2
Description of Problem: Implement a Caesar Cipher that shifts each letter in a given message by a fixed number of places while preserving non-letter characters and maintaining case sensitivity.
"""
import string # Importing the string module for working with alphabets

# Constants
SHIFT = 6 # Number of positions to shift each letter
MESSAGE = "In the end, we only regret the chances we didn't take."

def caesar_cipher(text, shift):
    encoded_message = "" # Initialize an empty string to store the encoded message
    
    for char in text: # Loop through each character
        if char.isalpha(): # Only shift letters
            is_upper = char.isupper()
            alphabet = string.ascii_uppercase if is_upper else string.ascii_lowercase
            # Find the index of the character, shift it, and wrap around using modulo 26
            new_char = alphabet[(alphabet.index(char) + shift) % 26]
            encoded_message += new_char
        else:
            encoded_message += char

    return encoded_message
# Encrypt message using the defined shift value
encoded_text = caesar_cipher(MESSAGE, SHIFT)
# Print statements to display original and encrypted message
print(f"Your cleartext message was: {MESSAGE}")
print(f"The new encoded message is: {encoded_text}")
