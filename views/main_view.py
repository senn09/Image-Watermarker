from tkinter import filedialog as fd

class MainView():
    def __init__(self):
        pass

class Menubar():
    def __init__(self):
        pass

    def select_files(self):
        filetypes = (
            ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.tif'),
            ('All files', '*.*')
        )

        filenames = fd.askopenfilenames(
            title='Open files',
            initialdir='/Users/stevenhan/PycharmProjects/watermarker/images',
            filetypes=filetypes)

        if filenames:
            # pass image file paths onto show_watermark_image_view
            self.on_sucess(filenames)

class Settings():
    pass

class ImagePreview():
    pass