import tkinter as tk
from views.main_view import MainView

# This file is redundant as there is only one view but provides
# a proof of concept as a Model-View-Controller (MVC) design pattern
class ViewManager:
    def __init__(self, parent, callbacks):
        self.parent = parent
        self.views = {}
        self.current_view = None
        self.callbacks = callbacks

    def register_view(self, ):
    def switch_to_view(self, view_name):
            pass

    def update_image(self, image):
        pass

    def update_settings_display(self, settings):
        pass

    def register_callbacks(self, callbacks):
        pass

