import os
from cryptography.fernet import Fernet

finalenc = []
#creates list that will be used to know what to encrypt

folder = str(input("enter path for your folder here"))
#defining the directory we want

direc = os.listdir(folder)
#sets the list of files as a varialbe

os.chdir(folder)

for file in direc:
    if file == "Encrypt.py":
        direc.remove("Encrypt.py")
    if file == "README.md":
        direc.remove("README.md")     
    if file == "Decrypt.py":
        direc.remove("Decrypt.py")  
    if file == "cryptkey.key":
        direc.remove("cryptkey.key")     
    if file == "gitignore":
        direc.remove("gitignore") 



key = Fernet.generate_key()

with open("cryptkey.key", "wb") as cryptkey:
    cryptkey.write(key)
    
    
for file in direc:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("succusfully encrypted", direc)
