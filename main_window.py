import zip_window
import unzip_window
from tkinter import *
from tkinter import font as tkf
from functools import partial


# main window
def create_main_window():
    window = Tk()
    window.title("AutoZipper")
    window.geometry("605x405+300+200")
    window.resizable(width = False, height = False)
    window['background'] = '#f6f6ba'           

    ONE_PIXEL = PhotoImage(width=1, height=1)

    # title frame
    title_frame = Label(window, width=540, height=170, image=ONE_PIXEL)
    title_frame.configure(background='#ffb86c')
    title_frame.place(x=30, y=20)

    # icon image
    global icon_image
    icon_image = PhotoImage(file='potato.png')
    icon_label = Label(window, width=150, height=150, image=icon_image)
    icon_label.configure(bd=0)
    icon_label.place(x=40, y=30)

    # title
    title_label = Label(window, width=310, height=150, image=ONE_PIXEL)
    title_label['text'] = 'AutoZipper'
    title_label['font'] = tkf.Font(family='Ubuntu Mono', size=48, weight='bold')
    title_label.configure(compound=CENTER, background='#ffb86c')
    title_label.place(x=225, y=30)

    # signature
    signature_label = Label(window, image=ONE_PIXEL)
    signature_label['text'] = 'Created by Dannyyang0329'
    signature_label['font'] = tkf.Font(family='Ubuntu Mono', size=12, slant='italic')
    signature_label.configure(compound=CENTER, background='#ffb86c')
    signature_label.place(x=355, y=150)

    # zip frame
    zip_frame = Label(window, width=264, height=180, image=ONE_PIXEL)
    zip_frame['background'] = '#ffb86c'
    zip_frame.place(x=30, y=200)

    # zip button
    zip_btn = Button(window, width=244, height=160, image=ONE_PIXEL, command=partial(zip_window.create_zip_window, window))
    zip_btn['text'] = '🔐 Zip'
    zip_btn['font'] = tkf.Font(family='Ubuntu Mono', size=36, weight='bold')
    zip_btn.configure(bd=0, compound=CENTER, background='#efd130', activebackground='#35fbbf')
    zip_btn.place(x=40, y=210)

    # unzip frame
    unzip_frame = Label(window, width=264, height=180, image=ONE_PIXEL)
    unzip_frame['background'] = '#ffb86c'
    unzip_frame.place(x=306, y=200)

    # unzip button
    unzip_btn = Button(window, width=244, height=160, image=ONE_PIXEL, command=partial(unzip_window.create_unzip_window, window))
    unzip_btn['text'] = '🔓 Unzip'
    unzip_btn['font'] = tkf.Font(family='Ubuntu Mono', size=36, weight='bold')
    unzip_btn.configure(bd=0, compound=CENTER, background='#efd130', activebackground='#35fbbf')
    unzip_btn.place(x=316, y=210)

    window.mainloop()


# execute the program
create_main_window()