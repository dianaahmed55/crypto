
import string
import random

alphabet = string.ascii_lowercase

# encryption
def caesar_encrypt(plaintext, key):
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            shifted_char = chr((ord(char.lower()) - ord('a') + key) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            ciphertext += shifted_char
        else:
            ciphertext += char

    return ciphertext

# decryption
def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# helper function
def get_random_key():
    return random.randint(1, 25)

# demo
key = get_random_key()
plaintext = "I love cryptography"

print(f"===== Caesar encryption demo =====\nplaintext: {plaintext}, key: {key}")
encrypted_text = caesar_encrypt(plaintext, key)
print(f"encrypted: {encrypted_text}")
print("---------------------------------------------")

print(f"===== Caesar decryption demo =====\nciphertext: {encrypted_text}, key: {key}")
decrypted_text = caesar_decrypt(encrypted_text, key)
print(f"decrypted: {decrypted_text}")




# import string
# import random

# def caesar_cipher(text, shift, action):
#     """
#     Caesar Cipher encryption and decryption.

#     :param text: The text to be processed.
#     :param shift: The shift value for encryption/decryption.
#     :param action: 'encrypt' for encryption, 'decrypt' for decryption.
#     :return: The processed text.
#     """
#     if action not in ['encrypt', 'decrypt']:
#         raise ValueError("Invalid action. Use 'encrypt' or 'decrypt'.")

#     alphabet = string.ascii_lowercase
#     result = ''

#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             char = char.lower()

#             if action == 'encrypt':
#                 index = (alphabet.index(char) + shift) % 26
#             else:  # action == 'decrypt'
#                 index = (alphabet.index(char) - shift) % 26

#             result += alphabet[index].upper() if is_upper else alphabet[index]
#         else:
#             result += char

#     return result

# def get_random_shift():
#     return random.randint(1, 25)

# # demo
# plaintext = "I love cryptography"
# shift = get_random_shift()

# encrypted_text = caesar_cipher(plaintext, shift, 'encrypt')
# print(f"===== Caesar encryption demo =====\nplaintext: {plaintext}, shift: {shift}")
# print(f"encrypted: {encrypted_text}")
# print("---------------------------------------------")

# decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')
# print(f"===== Caesar decryption demo =====\nciphertext: {encrypted_text}, shift: {shift}")
# print(f"decrypted: {decrypted_text}")
