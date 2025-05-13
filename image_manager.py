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
            initialdir='/images',
            filetypes=filetypes)

        if filepaths:
            return filepaths
            logging.debug("sucessfully loaded filepaths")
        else:
            logging.debug("failed loaded filepaths")



    def load_images(self, paths):
        for path in paths:
            self.original_images.append((Image.open(path, mode="r"), path))


    def watermark_image(self, settings):
            base_im = self.original_images[self.current_index][0]

            if base_im.mode != 'RGBA':
                base_im = base_im.convert('RGBA')

            # Create Watermark ---------------------------------------------------------------------
            font = ImageFont.truetype("/Library/Fonts/Arial.ttf", settings['font_size'].get(), encoding="unic")
            text = settings["text"].get()
            bbox = font.getbbox(text)
            text_w = int(bbox[2] - bbox[0])
            text_h = int(bbox[3] - bbox[1])
            wm_img_size = (text_w, text_h)
            wm_angle = settings["angle"].get()
            wm_img = Image.new("RGBA", wm_img_size, (255, 255, 255, 0))

            d = ImageDraw.Draw(wm_img)
            d.text((text_w / 2, text_h), text, fill=self.hex2rgb(settings['color'], settings['opacity']), anchor="ms", font=font)
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
            print(base_im, tiled_wm_img)
            self.watermarked_image = Image.alpha_composite(base_im, tiled_wm_img)


    def display_watermarked(self):
        self.watermarked_image.show()

    def get_watermarked(self):
        return self.watermarked_image

    def export_watermarked(self):
        print("image saved")

        filetypes = (
            ('Image files', '*.jpeg'),
            ('All files', '*.*')
        )

        filepath = fd.asksaveasfile(initialfile='watermarked_image.jpeg',
                                    initialdir='/saved_images',
                              defaultextension=".jpeg", filetypes=filetypes)


        export_image = self.watermarked_image.convert('RGB')
        export_image = export_image.save(filepath)

    def hex2rgb(self, hexcode, alpha_value):
        # Remove '#' if present
        hexcode = hexcode.get().lstrip('#')

        # Convert pairs of hex digits to integers
        rgb =  tuple(int(hexcode[i:i + 2], 16) for i in range(0, len(hexcode), 2))
        return rgb + (alpha_value.get(),)


if __name__ == "__main__":
    manager = ImageManager()
    filepaths = manager.select_files()
    manager.load_images(filepaths)

    settings = {
        "text": "watermark",
        "font_size": 120,
        "color": "#FF0000",
        "opacity": 100,
        "angle": 45,
    }

    manager.watermark_image(settings)
    manager.display_watermarked()
