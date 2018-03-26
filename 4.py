from tkinter import Frame, Label, Entry, Tk, Text, Button, END
import logic_for_gui

root = Tk()
root.title('Игра')
# root.minsize(800,600)

fram = Frame(root, width=800, height=600)
fram.pack()


def firscreen():
    btn_quit.place_forget()
    btn_start.place_forget()

    entry.place(x=275, y=260)
    bnt_input.place(x=270, y=400)


def secondscreen():
    # запрашивает у пользователя неповторяющиеся цифры
    get_nums()
    if nums != 0:
        num_err.place_forget()
        entry.place_forget()
        bnt_input.place_forget()

        turn.place(x=330, y=170)
        output_user.place(x=140, y=230)
        output_comp.place(x=420, y=230)
        try_entry.place(x=140, y=540)
        btn_ok.place(x=325, y=540)
        btn_sur.place(x=420, y=540)

        thirdscreen()



def thirdscreen():
    # while True:   #убрал цикл пока что
    if True:
        output_user.insert(1.0, ('=' * 5, 'Ход игрока', '=' * 5))
        output_user.insert(END, '\nУгадайте число компьютера')

        
            # break
        '''
        
        '''


def limit_sym(e):
    entry.delete('3', END)
    try_entry.delete('3', END)


def get_nums():
    global nums
    while True:
        nums = entry.get()
        if len(set(nums)) == 4 and nums.isdigit():
            nums = list(map(int, nums))
            print('nums before return', nums)
            return nums
        else:
            num_err.place(x=190, y=170)
            nums = 0
            return nums

def player_turn():
    print('start get numb2')
    nums = try_entry.get()
    print('nums', nums)
    if len(set(nums)) == 4 and nums.isdigit():
        num_err.place_forget()
        nums = list(map(int, nums))
        print('nums before bulls, cows', nums)

        bulls, cows = logic_for_gui.check(nums, enemy)
        txt = '\nБыки {}, Коровы {}'.format(bulls, cows)
        output_user.insert(END, txt)
        if bulls == 4:
            print('Победил игрок!')
        else:
            return
        print('Компьютер загадал {}'.format(enemy))

    else:
        turn.place_forget()
        num_err.place(x=190, y=170)

    print(nums)

def enemy_turn():
    print('=' * 15, 'Ход комьютера', '=' * 15)
    enemy_try = get_one_answer(answers)
    print('Компьютер считает, что вы загадали {}'.format(enemy_try))
    bulls, cows = check(enemy_try, player)
    print('Быки {}, Коровы {}'.format(bulls, cows))
    if bulls == 4:
        print('Победил компьютер!')
        print('Компьютер загадал {}'.format(enemy))
        break
    else:
        answers = del_bad_answers(answers, enemy_try, bulls, cows)



# logic
answers = logic_for_gui.get_all_answers()
enemy = logic_for_gui.get_one_answer(answers)

print(enemy)

# начальный nums, числа загаданное пользователем
nums = 0

# first screen
title = Label(fram, font=('Cambria', 50), text='Быки и коровы')
title.place(x=190, y=70)

btn_start = Button(fram, width=10, text='Начать', font=('Cambria, 30'), command=firscreen)
btn_start.place(x=270, y=260)

btn_quit = Button(fram, width=10, text='Выход', font=('Cambria, 30'), command=quit)
btn_quit.place(x=270, y=400)

# second screen
num_err = Label(fram, text='Введите 4 неповторяющиеся цифры', font=('Carambia, 20'))
entry = Entry(fram, width=10, font=('Cambria, 30'))
entry.bind('<KeyPress>', limit_sym)
bnt_input = Button(fram, width=10, text='Ввести', font=('Cambria, 30'), command=secondscreen)


# third screen
turn = Label(fram, text='Ход NN', font=('Carambia, 20'))
output_user = Text(fram, width=27, height=18)
output_comp = Text(fram, width=27, height=18)
try_entry = Entry(fram, font=('Cambria, 15'), width=10)
try_entry.bind('<KeyPress>', limit_sym)
btn_ok = Button(fram, text='ОК', font=('Cambria, 10'), command=player_turn)
btn_sur = Button(fram, text='Сдаться', font=('Cambria, 10'), width=25)

root.mainloop()