from tkinter import *


root = Tk()
#root.title = 'Игра'
root.geometry('800x600')


title = Label(root, font=('Cambria', 50), text='Быки и коровы', bg='red')
title.place(x=190, y=70)

btn_start = Button(root, width=10, text='Начать', font=('Cambria, 30'), bg='red')
btn_start.place(x=270, y=260)

btn_quit = Button(root, width=10, text='Выход', font=('Cambria, 30'))
btn_quit.place(x=270, y=400)

root.mainloop()