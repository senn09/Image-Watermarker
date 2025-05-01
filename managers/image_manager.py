from PIL import Image, ImageTk

class ImageManager:
    def __init__(self):
        self.original_images: list[Image]
        self.watermarked_images: list[Image]
        self.current_index = 0

    def load_images(self, path):
        pass

    def get_current_original(self):
        pass

    def get_current_watermarked(self):
        pass

    def generate_watermark(self, settings):
        pass

    def save_current_watermarked(self, path):
        pass

