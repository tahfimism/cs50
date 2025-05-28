import sys
from PIL import Image, ImageOps


len = len(sys.argv)
if len < 3:
    sys.exit("Too few command-line arguments")
elif len > 3:
    sys.exit("Too many command-line arguments")

filetype1 = sys.argv[1].lower().split(".")
filetype2 = sys.argv[2].lower().split(".")




valid_extensions = ["jpg", "jpeg", "png"]



if filetype1[-1] not in valid_extensions:
    sys.exit("Input must be a PNG, JPEG, or JPG file")
if filetype2[-1] not in valid_extensions:
    sys.exit("Output must be a PNG, JPEG, or JPG file")
if filetype1[0] == filetype2[0]:
    sys.exit("Input and output have the same name")
if filetype1[-1] != filetype2[-1]:
    sys.exit("Input and output have different extensions")



shirt = Image.open("shirt.png")
size = shirt.size




with Image.open(sys.argv[1]) as img:
    cropped = ImageOps.fit(img, size)
    cropped.paste(shirt, shirt)
    cropped.save(sys.argv[2])




