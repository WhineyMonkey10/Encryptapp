print("Type a d in order to Decrypt, Type e in order to encrypt")

def dore():
    x = input("D/E")
    x = x.upper
   
    if x == E:
        exec(open("Encrypt.py").read())
    if x == D:
        exec(open("Encrypt.py").read())
    else:
        print("unvalid input try again")
        dore()
