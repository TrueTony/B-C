from tkinter import *
import logic_for_gui

root = Tk()
root.title('Игра')
# root.minsize(800,600)

fram = Frame(root, width=800, height=600)
fram.pack()


def secondscreen():
    btn_quit.place_forget()
    btn_start.place_forget()

    entry.place(x=275, y=260)
    bnt_input.place(x=270, y=400)


def thirdscreen():


    trig = 0
    # запрашивает упольщователя неповторяющиеся цифры
    

    nums = entry.get()
    if len(set(nums)) == 4 and nums.isdigit():

        trig = 1
        print('right')
    else:
        print('wrong')
    
    if trig == 1:
        entry.place_forget()
        bnt_input.place_forget()

        turn.place(x=330, y=170)
        output_user.place(x=140, y=230)
        output_comp.place(x=420, y=230)
        try_entry.place(x=140, y=540)
        btn_ok.place(x=325, y=540)
        btn_sur.place(x=420, y=540)

        nums = list(map(int, nums))
        return nums

def foruthscreen():
    pass

def limit_sym(e):
    entry.delete('3', END)

#logic
answers = logic_for_gui.get_all_answers()
enemy = logic_for_gui.get_one_answer(answers)

# first screen
title = Label(fram, font=('Cambria', 50), text='Быки и коровы')
title.place(x=190, y=70)

btn_start = Button(fram, width=10, text='Начать', font=('Cambria, 30'), command=secondscreen)
btn_start.place(x=270, y=260)

btn_quit = Button(fram, width=10, text='Выход', font=('Cambria, 30'), command=quit)
btn_quit.place(x=270, y=400)

# second screen
entry = Entry(fram, width=10, font=('Cambria, 30'))
entry.bind('<KeyPress>', limit_sym)
bnt_input = Button(fram, width=10, text='Ввести', font=('Cambria, 30'), command=thirdscreen)
turn = Label(fram, text='Ход NN', font=('Carambia, 20'))

# third screen
output_user = Text(fram, width=27, height=18)
output_comp = Text(fram, width=27, height=18)
try_entry = Entry(fram, font=('Cambria, 15'), width=10)
btn_ok = Button(fram, text='ОК', font=('Cambria, 10'))
btn_sur = Button(fram, text='Сдаться', font=('Cambria, 10'), width=25)

root.mainloop()