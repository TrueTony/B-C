from tkinter import *


root = Tk()
root.title('Игра')
#root.minsize(800,600)

fram = Frame(root, width=800, height=600)
fram.pack()

def secondscreen():
    btn_quit.place_forget()
    btn_start.place_forget()

    entry.place(x=275, y=260)
    bnt_input.place(x=270, y=400)



def thirdscreen():
    entry.place_forget()
    bnt_input.place_forget()

# first screen
title= Label(fram, font=('Cambria', 50), text='Быки и коровы')
title.place(x=190, y=70)

btn_start = Button(fram, width=10, text='Начать', font=('Cambria, 30'), command=secondscreen)
btn_start.place(x=270, y=260)

btn_quit = Button(fram, width=10, text='Выход', font=('Cambria, 30'), command=quit)
btn_quit.place(x=270, y=400)

# second screen
entry = Entry(fram, width=10, font=('Cambria, 30'))
bnt_input = Button(fram, width=10, text='Ввести', font=('Cambria, 30'), command=thirdscreen)





root.mainloop()