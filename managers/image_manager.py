import logging

import math
from tkinter import ttk, colorchooser, filedialog as fd, StringVar, IntVar
from PIL import Image, ImageDraw, ImageFont

class ImageManager:
    def __init__(self):
        self.original_images: list[tuple[Image, str]] = []
        self.watermarked_image: Image = None
        self.current_index = 0


    def select_files(self):
        filetypes = (
            ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp *.tiff *.tif'),
            ('All files', '*.*')
        )

        filepaths = fd.askopenfilenames(
            title='Open files',
            initialdir='/Users/stevenhan/PycharmProjects/watermarker/images',
            filetypes=filetypes)

        if filepaths:
            return filepaths
            logging.debug("sucessfully loaded filepaths")
        else:
            logging.debug("failed loaded filepaths")



    def load_images(self, paths):
        for path in paths:
            self.original_images.append((Image.open(path), path))


    def watermark_image(self, settings):
            base_im = self.original_images[self.current_index][0]

            # Create Watermark ---------------------------------------------------------------------
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100, encoding="unic")
            text = settings["text"].get()
            bbox = font.getbbox(text)
            text_w = int(bbox[2] - bbox[0])
            text_h = int(bbox[3] - bbox[1])
            wm_img_size = (text_w, text_h)
            wm_angle = settings["angle"].get()
            wm_img = Image.new("RGBA", wm_img_size, (255, 255, 255, 0))

            d = ImageDraw.Draw(wm_img)
            d.text((text_w / 2, text_h), text, fill=(255, 0, 0, 255), anchor="ms", font=font)
            wm_img = wm_img.rotate(wm_angle, expand=True)

            # Create Tiled Watermark ---------------------------------------------------------------------
            tiled_wm_img = Image.new("RGBA", base_im.size, (255, 255, 255, 255))
            wm_img_size = wm_img.size

            x_ratio = base_im.size[0] / wm_img_size[0]
            y_ratio = base_im.size[1] / wm_img_size[1]

            # could be better optimized
            for i in range(math.ceil(x_ratio)):
                for j in range(math.ceil(y_ratio)):
                    tiled_wm_img.paste(wm_img, (wm_img_size[0] * i, wm_img_size[1] * j))

            # Paste watermark over base image ---------------------------------------------------------------------
            self.watermarked_image = Image.alpha_composite(base_im, tiled_wm_img)


    def display_watermarked(self):
        self.watermarked_image.show()

    def get_watermarked(self):
        return self.watermarked_image

    def export_watermarked(self):
        pass

if __name__ == "__main__":
    manager = ImageManager()
    filepaths = manager.select_files()
    manager.load_images(filepaths)

    settings = {
        "text": "watermark",
        "font_size": 120,
        # "color": self.color_frame.get(),
        "opacity": 100,
        "angle": 45,
    }

    manager.watermark_image(settings)
    manager.display_watermarked()
