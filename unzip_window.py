import ZipOpener
from tkinter import *
from tkinter import font as tkf
from tkinter import filedialog


def open_source_file():
    filepath = filedialog.askopenfilename(title="Select a zip file", filetypes=[('zip file', '*.zip')])
    src_text.delete("1.0","end")
    src_text.insert("1.0", filepath)


def open_destination_folder():
    folderpath = filedialog.askdirectory(title="Select a folder")
    des_text.delete("1.0","end")
    des_text.insert("1.0", folderpath)


def zip_open():
    src = src_text.get("1.0", "end-1c")
    des = des_text.get("1.0", "end-1c")
    ZipOpener.zip_open(src, des)
    unzip_window.destroy()


def create_unzip_window(window):
    global unzip_window
    unzip_window = Toplevel()
    unzip_window.title('Zip Opener')
    unzip_window.geometry('620x260+600+400')
    unzip_window.resizable(width=False, height=False)
    unzip_window['background'] = '#f6f6ba'           

    ONE_PIXEL = PhotoImage(width=1, height=1)

    # source label
    src_label = Label(unzip_window, width=40, height=20, image=ONE_PIXEL)
    src_label['text'] = 'Src'
    src_label['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    src_label.configure(bd=0, compound=CENTER, background='#ffb86c')
    src_label.place(x=25, y=30)

    # source text
    global src_text
    src_text = Text(unzip_window, width=52, height=1)
    src_text['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    src_text.place(x=80, y=30)

    # select source file
    src_btn = Button(unzip_window, width=20, height=20, image=ONE_PIXEL, command=open_source_file)
    src_btn['text'] = '📁'
    src_btn['font'] = tkf.Font(size = 17)
    src_btn.configure(bd=0, compound=CENTER, background='#ffb86c', activebackground='#35fbbf')
    src_btn.place(x=565, y=30)


    # destination label
    des_label = Label(unzip_window, width=40, height=20, image=ONE_PIXEL)
    des_label['text'] = 'Des'
    des_label['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    des_label.configure(bd=0, compound=CENTER, background='#ffb86c')
    des_label.place(x=25, y=70)

    # destination text
    global des_text
    des_text = Text(unzip_window, width=52, height=1)
    des_text['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    des_text.place(x=80, y=70)

    # select destination file
    src_btn = Button(unzip_window, width=20, height=20, image=ONE_PIXEL, command=open_destination_folder)
    src_btn['text'] = '📁'
    src_btn['font'] = tkf.Font(size=17)
    src_btn.configure(bd=0, compound=CENTER, background='#ffb86c', activebackground='#35fbbf')
    src_btn.place(x=565, y=70)


    # start unzip button
    start_unzip_btn = Button(unzip_window, width=260, height=100, image=ONE_PIXEL, command=zip_open)
    start_unzip_btn['text'] = '🔓 Unzip'
    start_unzip_btn['font'] = tkf.Font(family='Ubuntu Mono', size=36, weight='bold')
    start_unzip_btn.configure(bd=0, compound=CENTER, background='#efd130', activebackground='#35fbbf')
    start_unzip_btn.place(x=180, y=125)

    unzip_window.transient(window)
    unzip_window.grab_set()
    window.wait_window(unzip_window)
