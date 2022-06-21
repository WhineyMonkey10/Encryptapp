import os
from cryptography.fernet import Fernet

finalenc = []
#creates list that will be used to know what to encrypt

folder = str(input("enter path for your folder here"))
#defining the directory we want

direc = os.listdir(folder)
#sets the list of files as a varialbe

os.chdir(folder)

for file in direc: #loops for all the files in the list
    print(file)

    if file == "Decrypt.py" or file == " Encrypt.py" or file == "README.md" or file == "cryptkey.key":
        continue
    if os.path.isfile(folder):
        finalenc.appened(file)

key = Fernet.generate_key()

with open("cryptkey.key", "wb") as cryptkey:
    cryptkey.write(key)
    
for file in finalenc:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        