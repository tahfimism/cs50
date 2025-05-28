from PIL inport Image
from PIL import ImageFilter

with image.open("wave.jpeg") as img:
    img = img.rotate(180)
    img = img.filter(ImageFilter.BLUR)
    img.save("wave_rotated.jpeg")

