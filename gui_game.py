# сложность
# время хода компьютера 1 сек.
from tkinter import *


root = Tk()

top_frame = Frame()
top_frame.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=BOTTOM)

button1 = Button(top_frame, text="Первая", fg="red")
button2 = Button(top_frame, text="Вторая", fg="blue")
button3 = Button(top_frame, text="Третья", fg="green")
button4 = Button(bottom_frame, text="Четвёртая", fg="gray")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()