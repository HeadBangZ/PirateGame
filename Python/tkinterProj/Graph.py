from tkinter import *
import math

root = Tk()
root.title("Curved Graph")

data = []

c = Canvas(width=600, height=300, bg="white")
c.pack()

axes = c.create_line(50, 150, 550, 150, fill="green")

for x in range(550):
    data.append(50 + x)
    data.append(150 - math.sin(x/20) * 100)

sincurve = c.create_line(data, fill="red")

c.mainloop()