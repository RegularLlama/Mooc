import os

def rename_files():
    flist = os.listdir(r"C:\Users\neela\Pictures\prank")
    print flist
    print os.getcwd()
    os.chdir(r"C:\Users\neela\Pictures\prank")
    print os.getcwd()
    for name in flist:
        os.rename(name, name.translate(None, "0123456789"))

rename_files()