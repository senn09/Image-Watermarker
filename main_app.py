import tkinter as tk

from managers.image_manager import ImageManager
from managers.settings_manager import SettingsManager
from managers.view_manager import ViewManager
from views import *
from tkinter import ttk
from tkinter import filedialog as fd
from PIL import Image, ImageTk

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.image_manager = ImageManager()
        self.settings_manager = SettingsManager()
        self.view_manager = ViewManager()

    def run(self):
        pass

    def handle_settings_change(self):
        pass

    def handle_image_selection(self):
        pass

    def handle_save_request(self):
        pass
