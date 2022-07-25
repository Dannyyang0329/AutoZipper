import os
import pyzipper
from tkinter import *
from tkinter import messagebox


def zip_open(src_file, des_folder):
    if not os.path.exists(src_file) or src_file[-4:] != '.zip':
        messagebox.showinfo("Error", "Please select correct zip file")
    elif not os.path.isdir(des_folder):
        messagebox.showinfo("Error", "Please select correct folder")
    else:
        while src_file[-4:] == '.zip':
            remove_file = ""
            with pyzipper.AESZipFile(src_file) as zf:
                fileName = zf.namelist()[0]
                password = fileName[:-4]

                zf.extractall(path=des_folder, pwd = bytes(password, 'utf-8'))
                remove_file = zf.filename

                src_file = des_folder + '/' + fileName
            os.remove(remove_file)
        messagebox.showinfo("Success", "Processing successfully")
        