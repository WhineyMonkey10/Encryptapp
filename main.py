x = input("Folder Path Here \n")

filez = open("usrinput.txt","w")
filez.truncate(0)
filez.close()

with open("usrinput.txt", "w") as f:
    f.write(x)


print("Type 1 in order to Encrypt, 2 in order to Decrypt, 3 to change Path, 4 in order to close")



def dore():
    print("1 to set/change Path (you need to do this first), 2 in order to Encrypt, Type 3 in order to Decrypt, 4 in order to close and clear saved path")
    x = input("1/2/3/4 \n")
   
    if x == "2":
        exec(open("Encrypt.py").read())
        dore()
    if x == "3":
        exec(open("Decrypt.py").read())
        dore()
    if x == "1":
        file = open("usrinput.txt","r+")
        file.truncate(0)
        file.close()
        y = input("Enter Path here")
        dore()
    if x == "4":
        filez = open("usrinput.txt","w")
        filez.truncate(0)
        filez.close()
        exit()
    else:
        print("unvalid input try again")
        dore()

dore()

