import sys
import os
from PIL import Image, ImageOps

if(len(sys.argv) < 3):
    sys.exit("Too few command-line arguments")

if(len(sys.argv) > 3):
    sys.exit("Too many command-line arguments")

input_image = sys.argv[1]
output_image = sys.argv[2]

input_image_ext = os.path.splitext(input_image)[1].casefold()
if(input_image_ext not in ('.jpg', '.jpeg', '.png')):
    sys.exit("Invalid input")

output_image_ext = os.path.splitext(output_image)[1].casefold()
if(output_image_ext not in ('.jpg', '.jpeg', '.png')):
    sys.exit("Invalid output")

if(input_image_ext != output_image_ext):
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    shirt_size = shirt.size

    before_image = Image.open(input_image)
    before_image = ImageOps.fit(before_image, shirt_size)
    before_image.paste(shirt, shirt)
    before_image.save(output_image)
except FileNotFoundError:
    sys.exit("Input does not exist")
