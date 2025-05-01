class SettingsManager:
    def __init__(self):
        self.text = "Watermark"
        self.opacity = 1.0
        self.font_size = 120
        self.color = "red"
        self.angle = 45
        self.observers = []

    def get_settings(self):
        pass

    def update_settings(self, settings):
        pass

    def register_observer(self, callback):
        pass

    def notify_observers(self):
        pass