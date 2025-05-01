import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

class MainApp(tk.Tk):
    # View Controller

    def __init__(self):
        super().__init__()
        self.title("Image Watermarker")
        self.geometry("900x600")
        self.image_paths = None

        # Watermark settings
        self.watermark_text = tk.StringVar()
        self.watermark_text.set("Watermark")  # Default value
        self.watermark_opacity = tk.DoubleVar()
        self.watermark_opacity.set(0.5)
        self.watermark_font_size = tk.IntVar()
        self.watermark_font_size.set(120)
        self.watermark_color = tk.StringVar()
        self.watermark_color.set("red")

        self.show_file_select_view()

    def show_file_select_view(self):
        if hasattr(self, "current_view"):
            self.current_view.destroy()
        self.current_view = FileSelectFrame(self, self.on_file_selected)
        self.current_view.pack()
        self.focus_force()

    def show_watermark_image_view(self):
        if hasattr(self, "current_view"):
            self.current_view.destroy()
        self.current_view = WatermarkImageFrame(self, self.image_paths, self.show_file_select_view)
        self.current_view.pack()

    def on_file_selected(self, filepaths):
        # Callback function for show_file_select_view that connects to show_watermark_image_view
        for path in filepaths:
            print(path)
        self.image_paths = filepaths
        self.show_watermark_image_view()


class MenuBar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

    def create_filemenu(self):
        self.filemenu = tk.Menu(self, tearoff=0)
        # self.filemenu.add_command(label="Open", command=donothing)
        # self.filemenu.add_command(label="Save", command=donothing)


class MainView():
    def __init__(self):
        pass


# View 1: Image Selection
class FileSelectFrame(ttk.Frame):
    def __init__(self, parent, on_success_callback):
        super().__init__(parent)
        self.on_sucess = on_success_callback
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(self, text='Open Files', command=self.select_files).pack()

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

# View 2: Watermark Image Viewer
class WatermarkImageFrame(ttk.Frame):
    def __init__(self, parent, image_paths, on_success_callback):
        super().__init__(parent)
        self.image_paths = image_paths
        self.on_sucess = on_success_callback
        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        # I have organized the view by having the settings in one frame and the image in another
        self.settings_frame = ttk.Frame()
        self

    def create_watermark_settings_widget(self):
        watermark_text_label = ttk.Label(self, text="Watermark Text")
        watermark_text_label.grid(row=0, column=0)

        watermark_entry = ttk.Entry(self)
        watermark_entry.grid(row=0, column=1)

    def create_widgets(self):
        ttk.Label(self, text=self.image_paths).pack(side=tk.TOP)

        for path in self.image_paths:
            image = Image.open(path) # Load Image with PIL
            preview_image = image.reduce(int(image.size[0]/700)) # Reduce image to ~700 pixels
            photo = ImageTk.PhotoImage(preview_image) # Convert to Tkinter-compatible format
            label = ttk.Label(image=photo) # Create a label to display the image
            label.image = photo  # strong reference to prevent garbage collection
            label.pack(side=tk.RIGHT)

# todo create one view
# todo create a menubar



if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

