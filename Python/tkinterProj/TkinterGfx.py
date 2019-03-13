from tkinter import *

# draw a flag
def draw_flag(flagcanvas):
    flagcanvas.create_rectangle(40, 40, 100, 100, fill="red", outline="red")
    flagcanvas.create_rectangle(100, 40, 120, 100, fill="white", outline="white")
    flagcanvas.create_rectangle(120, 40, 240, 100, fill="red", outline="red")
    flagcanvas.create_rectangle(40, 100, 240, 120, fill="white", outline="white")
    flagcanvas.create_rectangle(40, 120, 100, 180, fill="red", outline="red")
    flagcanvas.create_rectangle(100, 120, 120, 180, fill="white", outline="white")
    flagcanvas.create_rectangle(120, 120, 240, 180, fill="red", outline="red")

def draw_chess(chesscanvas, b, w):
    x = 40
    y = 220
    for i in range(0, 8):
        for j in range(0, 8):
            if (i + j) % 2 == 1:
                chesscanvas.create_rectangle(x + j * 20, y + i * 20, 20 + x + j * 20, 20 + y + i * 20, fill=b, outline=b)
            else:
                chesscanvas.create_rectangle(x + j * 20, y + i * 20, 20 + x + j * 20, 20 + y + i * 20, fill=w, outline=w)

def closeclick(e):
    tk.destroy()

def mouseclick(self, param):
    my_canvas.delete(param)
    draw_chess(my_canvas, "black", "white")
    my_canvas.create_text(250, 10, font=("Arial", 12), text="Click again to close it")
    my_canvas.bind('<Button-1>', closeclick)

tk = Tk()
tk.title("Experiment")

my_canvas = Canvas(tk, width=450, height=700, bg="lightblue")
my_canvas.bind('<Button-1>', lambda event : mouseclick(event, param=temporarytext))

my_canvas.pack()

temporarytext = my_canvas.create_text(70, 10, font=("Arial", 12), text="Click in window")

draw_flag(my_canvas)


tk.mainloop()