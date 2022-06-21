import os
from cryptography.fernet import Fernet

files = []

folder = input("enter path for your folder here")

for file in os.listdir("/Users/raphaelbialystok-joly/Documents/Code/Python/Testencrypt"):
    if file == "Decrypt.py" or file == " Encrypt.py" or file == "README.md" or file == "cryptkey.key":
        continue
    if os.path.isfile(file):
        files.appened(file)

print (files) 
"""        
print (files)

key = Fernet.generate_key()

with open("cryptkey.key", "wb") as cryptkey:
    cryptkey.write(key)
    
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
"""