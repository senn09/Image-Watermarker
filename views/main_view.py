from views import  view
from tkinter import colorchooser, filedialog as fd
import tkinter as tk
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
        self.text_entry = tk.Entry(self, width= 30)
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

# class ImagePreviewFrame(tk.Frame):

def test_SettingsFrame():
    root = tk.Tk()
    root.title("Program Settings")
    root.geometry("400x300")
    app = SettingsFrame(root)
    root.mainloop()

if __name__ == "__main__":
    test_SettingsFrame()

# class Menubar():
#     def __init__(self):
#         pass
#
#     def select_files(self):
#         filetypes = (
#             ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.tif'),
#             ('All files', '*.*')
#         )
#
#         filenames = fd.askopenfilenames(
#             title='Open files',
#             initialdir='/Users/stevenhan/PycharmProjects/watermarker/images',
#             filetypes=filetypes)
#
#         if filenames:
#             # pass image file paths onto show_watermark_image_view
#             self.on_sucess(filenames)

class Settings():
    pass

class ImagePreview():
    pass