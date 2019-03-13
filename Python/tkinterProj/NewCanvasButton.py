from tkinter import *

def echo():
    my_label['text'] = textentry.get()
    btn_one.config(state=DISABLED)
    btn_two.config(state=NORMAL)

def reset_test():
    btn_one.config(state=NORMAL)
    btn_two.config(state=DISABLED)

tk = Tk()
tk.title("Canvas with buttons")

my_canvas = Canvas(tk, width=240, height=100, bg="lightblue")

textentry = Entry(my_canvas)
my_canvas.create_window(20, 60, anchor=NW, window=textentry, height=20, width=80)

btn_one = Button(my_canvas, text="Echo input", command=echo)
my_canvas.create_window(20, 20, anchor=NW, window=btn_one)
btn_two = Button(my_canvas, text="Echo reset", command=reset_test)
my_canvas.create_window(120, 20, anchor=NW, window=btn_two)
btn_two.config(state=DISABLED)

my_label = Label(my_canvas, text="Echo", anchor='w')
my_canvas.create_window(120, 60, anchor=NW, window=my_label, height=20, width=80)

my_canvas.pack()

tk.mainloop()