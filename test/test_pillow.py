import math
from PIL import Image, ImageDraw, ImageFont

# Read Image ---------------------------------------------------------------------
base_im = Image.open("images/ss.png")

# Create Watermark ---------------------------------------------------------------------
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 100, encoding="unic")
text = "Watermark"
bbox = font.getbbox(text)
text_w = bbox[2] - bbox[0]
text_h = bbox[3] - bbox[1]
wm_img_size = (text_w, text_h)
wm_angle = 45
wm_img = Image.new("RGBA", wm_img_size, (255, 255, 255, 0))

d = ImageDraw.Draw(wm_img)
d.text((text_w / 2, text_h), text, fill=(255, 0, 0, 255), anchor="ms", font=font)
wm_img = wm_img.rotate(wm_angle, expand=True)


# Create Tiled Watermark ---------------------------------------------------------------------
tiled_wm_img = Image.new("RGBA", base_im.size, (255, 255, 255, 255))
wm_img_size = wm_img.size

x_ratio = base_im.size[0]/wm_img_size[0]
y_ratio = base_im.size[1] / wm_img_size[1]

# could be better optimized
for i in range(math.ceil(x_ratio)):
    for j in range(math.ceil(y_ratio)):
        tiled_wm_img.paste(wm_img, (wm_img_size[0] * i , wm_img_size[1] * j))
# tiled_wm_img.show()

# Paste watermark over base image ---------------------------------------------------------------------
final_image = Image.alpha_composite(base_im, tiled_wm_img)
final_image.show()

