from tkinter import Frame, Label, Entry, Tk, Text, Button, END, Toplevel
import logic_for_gui


def firtscreen():
    title.place(x=190, y=70)
    btn_start.place(x=270, y=260)
    btn_quit.place(x=270, y=400)

def firstcreen_logic():
    def trigger():
        global trigger
        trigger = 1
    btn_start.config(command=trigger)
    btn_quit.config(command=quit)


def secondscreen():
    btn_quit.place_forget()
    btn_start.place_forget()

    entry.place(x=275, y=260)
    bnt_input.place(x=270, y=400)


def thirdscreen():
    # запрашивает у пользователя неповторяющиеся цифры
    get_player()
    if player != 0:
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

def fourscreen():
    pass

def fifhscreen():
    win = Toplevel()
    win = Label(text='the End')
    win.pack
    if True:
        win.focus_force()
        win.grab_set()

def limit_sym(e):
    entry.delete('3', END)
    try_entry.delete('3', END)


def get_player():
    global player
    while True:
        player = entry.get()
        if len(set(player)) == 4 and player.isdigit():
            player = list(map(int, player))
            return player
        else:
            num_err.place(x=190, y=170)
            player = 0
            return player

def player_turn():

    number = try_entry.get()
    if len(set(number)) == 4 and number.isdigit():
        number = list(map(int, number))
        num_err.place_forget()
        turn.place(x=330, y=170)
        output_user.insert(END, '\n===== Ход игрока =====')
        output_user.insert(END, '\nУгадайте число компьютера')
        txt = '\nИгрок предположил {}'.format(number)
        output_user.insert(END, txt)
        bulls, cows = logic_for_gui.check(number, enemy)
        txt = '\nБыки {}, Коровы {}'.format(bulls, cows)
        output_user.insert(END, txt)
        if bulls == 4:
            output_user.insert(END, '\nПобедил игрок!')
            global a
            a = 1
            return a
        else:
            enemy_turn()

    else:
        turn.place_forget()
        num_err.place(x=190, y=170)

    print(number)

def enemy_turn():
    global answers
    print(len(answers))
    output_comp.insert(END, '\n===== Ход комьютера =====')
    enemy_try = logic_for_gui.get_one_answer(answers)
    txt = '\nКомпьютер считает, что вы загадали {}'.format(enemy_try)
    output_comp.insert(END, txt)
    bulls, cows = logic_for_gui.check(enemy_try, player)
    txt = '\nБыки {}, Коровы {}'.format(bulls, cows)
    output_comp.insert(END, txt)
    if bulls == 4:
        output_comp.insert(END, '\nПобедил копьютер!')
        txt = '\nКомпьютер загадал {}'.format(enemy)
        global a
        a = 1
        return a
    else:
        answers = logic_for_gui.del_bad_answers(answers, enemy_try, bulls, cows)
        return

def main():
    firtscreen()
    while trigger == 0:
        # firstcreen_logic()
        print('a')
    #secondscreen()

root = Tk()
root.title('Игра')

fram = Frame(root, width=800, height=600)
fram.pack()

# logic
answers = logic_for_gui.get_all_answers()
enemy = logic_for_gui.get_one_answer(answers)
a = 0
print('enemy', enemy)

# начальный player, число загаданное пользователем
player = 0

trigger = 0

# first screen
title = Label(fram, font=('Cambria', 50), text='Быки и коровы')
btn_start = Button(fram, width=10, text='Начать', font=('Cambria, 30'))
btn_quit = Button(fram, width=10, text='Выход', font=('Cambria, 30'))

# second screen
num_err = Label(fram, text='Введите 4 неповторяющиеся цифры', font=('Carambia, 20'))
entry = Entry(fram, width=10, font=('Cambria, 30'))
entry.bind('<KeyPress>', limit_sym)
bnt_input = Button(fram, width=10, text='Ввести', font=('Cambria, 30'), command=secondscreen)

# third screen
turn = Label(fram, text='Ход NN', font=('Carambia, 20'))
output_user = Text(fram, width=30, height=18)
output_comp = Text(fram, width=30, height=18)
try_entry = Entry(fram, font=('Cambria, 15'), width=10)
try_entry.bind('<KeyPress>', limit_sym)
btn_ok = Button(fram, text='ОК', font=('Cambria, 10'), command=None)
btn_sur = Button(fram, text='Сдаться', font=('Cambria, 10'), width=25)




main()

root.mainloop()
