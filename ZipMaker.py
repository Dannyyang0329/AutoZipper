import os
import pyzipper
from tkinter import *
from tkinter import messagebox
from random import randrange

def zip_make(src_files, des_folder, layers):
    for src_file in src_files:
        if not os.path.exists(src_file):
            messagebox.showinfo("Error", "Please select correct files")
            return 
    if not os.path.isdir(des_folder):
        messagebox.showinfo("Error", "Please select correct folder")
        return
    if layers == '' or not str.isdigit(layers):
        messagebox.showinfo("Error", "Please key in number")
        return
    else :
        layers_n = int(layers)
        if layers_n < 1 or layers_n > 1000:
            messagebox.showinfo("Error", "Please select correct layer")
            return

    password = []
    for x in range(int(layers)+1):
        tmp = str(randrange(100000, 100000000))
        while os.path.exists(tmp + '.zip'):
            tmp = str(randrange(100000, 100000000))
        password.append(tmp)

    for n in range(int(layers)+1):
        newfile = des_folder + '/' + password[n] + '.zip'
        if n == 0:
            zip_file = pyzipper.ZipFile(newfile, 'w', compression=pyzipper.ZIP_DEFLATED)
            for src_file in src_files:
                index = src_file.rfind('/', 0)
                relative_path =  src_file[index+1:]
                zip_file.write(src_file, relative_path)
        else:
            if n == int(layers):
                newfile = des_folder + '/' + 'AutoZipper_of_layer' + layers + '.zip'
            zip_file = pyzipper.AESZipFile(newfile, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES)
            zip_file.pwd = bytes(password[n-1], encoding='utf-8')

            absolute_path = des_folder + '/' + password[n-1] + '.zip'
            relative_path = password[n-1] + '.zip'
            zip_file.write(absolute_path, relative_path)

            os.remove(absolute_path)

    messagebox.showinfo("Success", "Processing successfully")
