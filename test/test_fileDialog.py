import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the root window
root = tk.Tk()
root.title('Tkinter File Dialog')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.tif'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/Users/stevenhan/PycharmProjects/watermarker/images',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )


# open button
open_button = ttk.Button(
    root,
    text='Open Files',
    command=select_files
)

open_button.pack(expand=True)

root.mainloop()