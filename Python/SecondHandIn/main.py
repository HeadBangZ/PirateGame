from tkinter import *
import math

root = Tk()
root.title("Population Graph")

my_canvas = Canvas(width=800, height=800, bg="white")
my_canvas.create_text(200, 20, anchor=NW, font=("Arial", 24), text="Fox and Rabbit Population")
my_canvas.create_text(15, 75, anchor=NW, font=("Arial", 24), text="1400")
my_canvas.create_text(15, 425, anchor=NW, font=("Arial", 24), text="500")
my_canvas.create_text(15, 575, anchor=NW, font=("Arial", 24), text="10")

x_axes = my_canvas.create_line(100, 700, 700, 700, fill="blue")
y_axes = my_canvas.create_line(100, 700, 100, 100, fill="blue")

# initial values
a = 0.1 
b = 0.00002
c = 0.01
d = 0.01
e = 0.00002
f = 0.0001

rabbits = int(input("Enter number of rabbits: "))
foxes = int(input("Enter number of foxes: "))

xy_fox = []
xy_rabbit = []

for i in range(600):
    # append values to array
    xy_rabbit.append(100 + i)
    xy_rabbit.append(700 - rabbits / 2)
    xy_fox.append(100 + i)
    xy_fox.append(700 - foxes * 10)
    # calculate population
    rabbit_population = rabbits * (1 + a - b * rabbits - c * foxes)
    fox_population = foxes * (1 - d + e * rabbits - f * foxes)
    # set population value
    rabbits = rabbit_population
    foxes = fox_population
    # print if exstinct
    print("Rabbits: " + str(rabbits) + " and Foxes: " + str(foxes))
    if rabbits < 1:
        print("Rabbits are exstinct")
    elif foxes < 1:
        print("Foxes are exstinct")


rabbit_curve = my_canvas.create_line(xy_rabbit, fill="green")
fox_curve = my_canvas.create_line(xy_fox, fill="red")

my_canvas.pack()

root.mainloop()