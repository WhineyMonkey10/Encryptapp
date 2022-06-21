x = input("Folder Path Here \n")

with open("usrinput.txt", "r") as f:
    f.write(x)


print("Type 1 in order to Encrypt, 2 in order to Decrypt, 3 to change Path, 4 in order to close")



def dore():
    print("1 to set/change Path (you need to do this first), 2 in order to Decrypt, Type 3 in order to Encrypt, 4 in order to close and clear saved path")
    x = input("1/2/3/4 \n")
   
    if x == "2":
        exec(open("Encrypt.py").read())
        dore()
    if x == "3":
        exec(open("Decrypt.py").read())
        dore()
    if x == "1 ":
        y = input("Enter Path here")
        dore()
    if x == "4":
        with open("usrinput.txt", "w") as q:
            q.write(x)
    else:
        print("unvalid input try again")
        dore()

dore()