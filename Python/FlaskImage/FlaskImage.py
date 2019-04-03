from tkinter import *
from PIL import Image, ImageDraw, ImageFont
import math
import os

root = Tk()
root.tite("Random Image")

c = Canvas(width = 500, height = 300, bg = 'white')
c.pack()

my_text = "Random Image Stuff"
c.create_text(50, 20, anchor = NW, text = my_text)

axes = c.create_line(50, 150, 450, 150, fill = 'green')

xy = []
for x in range(400):
    xy.append(50 + x)
    xy.append(150 - math.sin(x/40) * 100)

sinekurve = c.create_line(xy, fill = 'red')

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

my_image = Image.new("RGB", (500, 300), white)
draw = ImageDraw.Draw(my_image)

my_font = ImageFont.truetype("arial.ttf", 15)

draw.text((50, 20), my_text, font = my_font, fill = black)
draw.line([50, 150, 450, 150], green)
draw.line(xy, red)

my_file_path = os.path.join('static', 'image', 'mytest.jpg')
my_image.save(my_file_path)

os.startfile(my_file_path)

root.mainloop()
