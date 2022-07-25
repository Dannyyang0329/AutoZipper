import ZipMaker
from tkinter import *
from tkinter import font as tkf
from tkinter import filedialog


def open_source_files():
    filepath = filedialog.askopenfilenames(title="Select files", filetypes=[('All file', '*.*')])
    src_text.delete("1.0","end")
    src_text.insert("1.0", filepath)


def open_destination_folder():
    folderpath = filedialog.askdirectory(title="Select a folder")
    des_text.delete("1.0","end")
    des_text.insert("1.0", folderpath)


def zip_make():
    src = src_text.get("1.0", "end-1c").split()
    des = des_text.get("1.0", "end-1c")
    layers = layer_text.get("1.0", "end-1c")
    ZipMaker.zip_make(src, des, layers)
    zip_window.destroy()


def create_zip_window(window):
    global zip_window
    zip_window = Toplevel()
    zip_window.title("Zip Opener")
    zip_window.geometry("620x300+600+400")
    zip_window.resizable(width=False, height=False)
    zip_window['background'] = '#f6f6ba'           

    ONE_PIXEL = PhotoImage(width=1, height=1)

    # source label
    src_label = Label(zip_window, width=40, height=20, image=ONE_PIXEL)
    src_label['text'] = 'Src'
    src_label['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    src_label.configure(bd=0, compound=CENTER, background='#ffb86c')
    src_label.place(x=25, y=30)

    # source text
    global src_text
    src_text = Text(zip_window, width=52, height=1)
    src_text['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    src_text.place(x=80, y=30)

    # select source file
    src_btn = Button(zip_window, width=20, height=20, image=ONE_PIXEL, command=open_source_files)
    src_btn['text'] = '📁'
    src_btn['font'] = tkf.Font(size=17)
    src_btn.configure(bd=0, compound=CENTER, background='#ffb86c', activebackground='#35fbbf')
    src_btn.place(x=565, y=30)


    # destination label
    des_label = Label(zip_window, width=40, height=20, image=ONE_PIXEL)
    des_label['text'] = 'Des'
    des_label['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    des_label.configure(bd=0, compound=CENTER, background='#ffb86c')
    des_label.place(x=25, y=70)

    # destination text
    global des_text
    des_text = Text(zip_window, width=52, height=1)
    des_text['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    des_text.place(x=80, y=70)

    # select destination file
    src_btn = Button(zip_window, width=20, height=20, image=ONE_PIXEL, command=open_destination_folder)
    src_btn['text'] = '📁'
    src_btn['font'] = tkf.Font(size = 17)
    src_btn.configure(bd=0, compound=CENTER, background='#ffb86c', activebackground='#35fbbf')
    src_btn.place(x=565, y=70)


    # layer label
    layer_label = Label(zip_window, width=170, height=20, image=ONE_PIXEL)
    layer_label['text'] = 'Layers (1~1000)'
    layer_label['font'] = tkf.Font(family='Ubuntu Mono', size=14)
    layer_label.configure(bd=0, compound=CENTER, background='#ffb86c')
    layer_label.place(x=25, y=110)

    # layer text
    global layer_text
    layer_text = Text(zip_window, width=8, height=1)
    layer_text['font'] = tkf.Font(family="Ubuntu Mono", size=14)
    layer_text.place(x=210, y=110)


    # start unzip button
    start_zip_btn = Button(zip_window, width=260, height=100, image=ONE_PIXEL, command=zip_make)
    start_zip_btn['text'] = '🔐 Zip'
    start_zip_btn['font'] = tkf.Font(family='Ubuntu Mono', size=36, weight='bold')
    start_zip_btn.configure(bd=0, compound=CENTER, background='#efd130', activebackground='#35fbbf')
    start_zip_btn.place(x=180, y=165)

    zip_window.transient(window)
    zip_window.grab_set()
    window.wait_window(zip_window)
