from views import view
from tkinter import ttk, colorchooser, filedialog as fd
import tkinter as tk
from managers.image_manager import ImageManager
from PIL import ImageTk

from typing import Dict, Any


# class MainView(view):
#     def __init__(self, parent: tk.Tk, callbacks: Dict[str, Any]):
#         super().__init__(parent, callbacks)
#
#         # Create Frames


class SettingsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_widgets()

    def create_widgets(self):
        # Row 0: Text Setting
        tk.Label(self, text="Text: ", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.text_entry = tk.Entry(self, width=30)
        self.text_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        self.text_entry.insert(0, "Watermark")

        # Row 1: Font Size Setting
        tk.Label(self, text="Font Size: ", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.font_size = tk.Spinbox(self, from_=1, to=200, width=5)
        self.font_size.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.font_size.delete(0, tk.END)
        self.font_size.insert(0, "12")

        # Row 2: Color setting
        tk.Label(self, text="Colour:", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.color_frame = tk.Frame(self, bg="#000000", width=30, height=20)
        self.color_frame.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        self.color_button = tk.Button(self, text="Choose Colour", command=self.choose_color)
        self.color_button.grid(row=2, column=1, sticky="e", padx=5, pady=5)
        self.color_value = "#000000"  # Default color is black

        # Row 3: Opacity setting
        tk.Label(self, text="Opacity:", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.opacity_slider = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL)
        self.opacity_slider.set(100)
        self.opacity_slider.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # Row 4: Angle setting
        tk.Label(self, text="Angle:", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.angle_slider = tk.Scale(self, from_=0, to=360, orient=tk.HORIZONTAL)
        self.angle_slider.grid(row=4, column=1, sticky="ew", padx=5, pady=5)

        # Row 5: Apply button
        # self.apply_button = tk.Button(self, text="Apply Settings", command=self.apply_settings)
        # self.apply_button.grid(row=5, column=0, columnspan=2, pady=10)

        # # Configure the grid to expand properly
        # self.columnconfigure(1, weight=1)

    def choose_color(self):
        color = colorchooser.askcolor(initialcolor=self.color_value)
        if color[1]:  # If a color was chosen (not canceled)
            self.color_value = color[1]
            self.color_frame.config(bg=self.color_value)


class ImagePreviewFrame(tk.Frame):
    def __init__(self, parent):
        self.width = 700
        self.height = 700
        self.border_width = 2
        self.border_color = "black"

        self.image_manager = ImageManager()

        super().__init__(parent,
                         width=self.width,
                         height=self.height,
                         bd=self.border_width,
                         relief=tk.SOLID,
                         bg=self.border_color)


        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_widgets()

        # Make the frame non-resizable
        self.pack_propagate(False)

    def create_widgets(self):
        self.image_label = tk.Label(
            self,
            width=self.width - 2 * self.border_width,
            height=self.height - 2 * self.border_width,
            bg="white")

        self.image_label.pack(padx=0, pady=0)


    def display_image(self):

        watermarked_image = self.image_manager.get_watermarked()
        preview_image = watermarked_image.reduce(max(int(watermarked_image.size[0] / self.width), int(watermarked_image.size[1] / self.height)))  # Reduce image to fit label
        photo = ImageTk.PhotoImage(preview_image)  # Convert to Tkinter-compatible format
        self.image_label.config(image=photo)
        self.image_label.image = photo


class Menubar(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_filemenu()

    def create_filemenu(self):
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="Open Images", command=ImageManager.select_files)
        filemenu.add_command(label="Export", command=ImageManager.export_watermarked)
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
    app = ImagePreviewFrame(root)
    app.image_manager.select_files()
    app.image_manager.display_watermarked()
    app.display_image()
    root.focus_force()
    root.mainloop()


if __name__ == "__main__":
    # test_SettingsFrame()
    # test_Menubar()
    test_ImagePreview()

class Settings():
    pass


class ImagePreview():
    pass
