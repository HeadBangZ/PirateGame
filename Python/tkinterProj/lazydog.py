from tkinter import *
import math

root = Tk()
root.title("Some stuff")

my_canvas = Canvas(width=500, height=300, bg="white")
my_canvas.create_text(150, 20, anchor=NW, font=("Arial", 24), text="Lazy dog curve")

my_canvas.pack()

x_axes = my_canvas.create_line(50, 250, 450, 250, fill="green")
y_axes = my_canvas.create_line(50, 250, 50, 50, fill="green")

xy = []

for y in range(100, 1, -1):
    y_val = y / 100
    x_val = math.log((1 + math.sqrt(1 - y_val*y_val)) / y) - math.sqrt(1 - y_val*y_val)
    xy.append(50 + x_val * 100)
    xy.append(250 - y_val * 100)

dogcurve = my_canvas.create_line(xy, fill="blue")

root.mainloop()