from abc import ABC, abstractmethod
import tkinter as tk
from typing import Dict, Any

class View(ABC):
    def __init__(self, parent: tk.Tk, callbacks: Dict[str, Any]):
        self.parent = parent
        self.frames =  {}
        self.callbacks = callbacks

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def hide(self):
        pass

    @abstractmethod
    def update_content(self, data):
        pass


