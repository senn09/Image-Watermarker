from tkinter import ttk, colorchooser, filedialog as fd, image_names
import tkinter as tk
from managers.image_manager import ImageManager
from PIL import ImageTk
from typing import Dict, Any
import logging

class MainView():
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Image Watermarker")
        self.root.geometry("900x600")  # Set initial window size

        self.image_manager = ImageManager()

        # create menubar
        self.menubar_callbacks = [self.import_images, self.export_images]
        menubar = Menubar(self.root, self.menubar_callbacks)
        self.root.config(menu=menubar)

        # create callbacks and ui components
        self.settings_callbacks = [self.update_watermark]
        self.image_preview_callbacks = [self.image_manager.get_watermarked]

        self.settings_frame = SettingsFrame(self.root, self.settings_callbacks)
        self.image_preview_label = ImagePreviewLabel(self.root, self.image_preview_callbacks)

        # pack frames
        self.settings_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        self.image_preview_label.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    def import_images(self):
        filepath = self.image_manager.select_files()
        self.image_manager.load_images(filepath)
        self.image_manager.watermark_image(self.settings_frame.settings)
        self.image_preview_label.cache_image()
        self.image_preview_label.scale_image(self.image_preview_label.watermarked_image.size[0],
                                             self.image_preview_label.watermarked_image.size[1])
        self.image_preview_label.display_image()

    def update_watermark(self):
        new_settings = self.settings_frame.settings
        self.image_manager.watermark_image(new_settings)
        self.image_preview_label.cache_image()
        self.image_preview_label.scale_image(self.image_preview_label.watermarked_image.size[0],
                                             self.image_preview_label.watermarked_image.size[1])
        self.image_preview_label.display_image()


    def export_images(self):
        self.image_manager.export_watermarked()

    def run(self):
        self.root.focus_force()
        self.root.mainloop()




class SettingsFrame(tk.Frame):
    def __init__(self, parent, callbacks):
        self.settings = {
            "text": tk.StringVar(value="watermark"),
            "font_size": tk.IntVar(value=120),
            "color": tk.StringVar(value="#FF0000"),
            "opacity": tk.IntVar(value=100),
            "angle": tk.IntVar(value=45),
        }


        super().__init__(parent)
        self.callbacks = callbacks
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):

        # Row 0: Text Setting
        tk.Label(self, text="Text: ", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.text_entry = tk.Entry(self, textvariable=self.settings["text"], width=30)
        self.text_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # Row 1: Font Size Setting
        tk.Label(self, text="Font Size: ", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.font_size = tk.Spinbox(self, textvariable=self.settings["font_size"] ,from_=1, to=200, width=5)
        self.font_size.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        # self.font_size.delete(0, tk.END)
        # self.font_size.insert(0, self.settings["font_size"].get())


        # Row 2: Color setting
        tk.Label(self, text="Colour:", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.color_frame = tk.Frame(self, bg=self.settings['color'].get(), width=30, height=20)
        self.color_frame.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        self.color_button = tk.Button(self, text="Choose Colour", command=self.choose_color)
        self.color_button.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.color_value = "#FF0000"  # Default color is black

        # Row 3: Opacity setting
        tk.Label(self, text="Opacity:", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.opacity_slider = tk.Scale(self, variable=self.settings["opacity"], from_=0, to=255, orient=tk.HORIZONTAL)
        self.opacity_slider.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # Row 4: Angle setting
        tk.Label(self, text="Angle:", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.angle_slider = tk.Scale(self, variable=self.settings["angle"], from_=0, to=90, orient=tk.HORIZONTAL)
        self.angle_slider.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        # Row 5: Update button
        self.apply_button = tk.Button(self, text="Update Preview", command=self.callbacks[0])
        self.apply_button.grid(row=5, column=0, columnspan=2, pady=10)


    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.color_value)
        if color[1]:  # If a color was chosen (not canceled)
            self.settings['color'].set(color[1])
            self.color_frame.config(bg=self.settings['color'].get())

class ImagePreviewLabel(tk.Label):
    def __init__(self, parent, callbacks):
        self.parent = parent
        self.callbacks = callbacks
        self.watermarked_image = None
        self.preview_image = None

        super().__init__(self.parent,
                         width=700,
                         height=700,
                         bd=2,
                         relief=tk.SOLID,
                         bg="white")

        self.bind("<Configure>", self.on_label_resize)
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


    def on_label_resize(self, event):
        width = event.width
        height = event.height

        logging.debug(f"new resize: width={width} height={height}")

        # self.scale_image(width, height)
        # self.display_image()


    def cache_image(self):
        self.watermarked_image = self.callbacks[0]()

    def scale_image(self, width, height):
        if self.watermarked_image is None:
            logging.error("watermarked_image is none")
        else:
            self.preview_image = self.watermarked_image.reduce(
                max(int(width / self.winfo_width()), int(
                    height / self.winfo_height())))  # Reduce image to fit label

    def display_image(self):
        if self.preview_image is None:
            logging.error("preview_image is none")
        else:
            tk_photo = ImageTk.PhotoImage(self.preview_image)  # Convert to Tkinter-compatible format
            self.config(image=tk_photo)
            self.image = tk_photo


class Menubar(tk.Menu):
    def __init__(self, parent, callbacks):
        self.parent = parent
        self.callbacks = callbacks
        super().__init__(self.parent)
        self.create_filemenu()

    def create_filemenu(self):
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="Open Images", command=self.callbacks[0])
        filemenu.add_command(label="Export", command=self.callbacks[1])
        self.add_cascade(label="File", menu=filemenu)

def test_SettingsFrame():
    root = tk.Tk()
    root.title("Program Settings")
    root.geometry("400x300")
    app = SettingsFrame(root)

    root.focus_force()
    root.mainloop()

def test_Menubar():
    root = tk.Tk()
    root.title("Menubar")
    root.geometry("400x300")

    menu = Menubar(root)
    root.config(menu=menu)
    root.focus_force()
    root.mainloop()

def test_ImagePreview():
    root = tk.Tk()
    root.title("Image Preview")
    root.geometry("400x300")
    app = ImagePreviewLabel(root)
    app.image_manager.select_files()
    app.image_manager.display_watermarked()
    app.display_image()
    root.focus_force()
    root.mainloop()

def test_MainView():
    app = MainView()
    app.run()


if __name__ == "__main__":
    # test_SettingsFrame()
    # test_Menubar()
    # test_ImagePreview()

    test_MainView()
