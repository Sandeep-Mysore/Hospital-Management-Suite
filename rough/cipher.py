from cryptography.fernet import Fernet
import pickle
import sys

# key = Fernet.generate_key()

key = b'5HFFdBeSChtl1oWaEWwDhTi5Cr7s4LohO5W2zIngmHU='
password = sys.argv[1]
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(password.encode())   #required to be bytes
print("ciphered_text: ", ciphered_text)

unciphered_text = (cipher_suite.decrypt(ciphered_text))
print("unciphered_text: ", unciphered_text.decode())
