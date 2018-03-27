from tkinter import Frame, Label, Entry, Tk, Text, Button, END, Toplevel, Message
import logic_for_gui

root = Tk()
root.title('Игра')
# root.minsize(800,600)

fram = Frame(root, width=800, height=600)
fram.pack()


def firscreen():
    logic()
    btn_quit.place_forget()
    btn_start.place_forget()

    entry.delete(0, END)
    entry.place(x=275, y=260)
    bnt_input.place(x=270, y=400)


def secondscreen():
    # запрашивает у пользователя неповторяющиеся цифры
    get_player()
    if player != 0:
        num_err.place_forget()
        entry.place_forget()
        bnt_input.place_forget()

        turn.place(x=330, y=170)
        output_user.delete(1.0, END)
        output_comp.delete(1.0, END)
        output_user.place(x=140, y=230)
        output_comp.place(x=420, y=230)
        try_entry.place(x=140, y=540)
        btn_ok.place(x=325, y=540)
        btn_sur.place(x=420, y=540)

        # thirdscreen()



def thirdscreen():
    pass


def fourscreen():
    def retry():
        turn.place_forget()
        output_user.place_forget()
        output_comp.place_forget()
        try_entry.place_forget()
        btn_ok.place_forget()
        btn_sur.place_forget()
        firscreen()
        top.destroy()


    top = Toplevel(width=300, height=200)
    msg = Message(top, text='Бла-ба-бла!')
    msg.pack()

    top.focus_force()
    top.grab_set()

    btn_retry = Button(top, text='Повторить', command=retry)
    btn_retry.pack()
    btn_quit = Button(top, text='Выход', command=quit)
    btn_quit.pack()

    


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
            fourscreen()
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
        fourscreen()
    else:
        answers = logic_for_gui.del_bad_answers(answers, enemy_try, bulls, cows)
        return

def main():
    player_turn()

# logic
def logic():
    global answers, enemy
    answers = logic_for_gui.get_all_answers()
    enemy = logic_for_gui.get_one_answer(answers)
    print('enemy', enemy)

# начальный player, числа загаданное пользователем
player = 0

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
output_user = Text(fram, width=30, height=18)
output_comp = Text(fram, width=30, height=18)
try_entry = Entry(fram, font=('Cambria, 15'), width=10)
try_entry.bind('<KeyPress>', limit_sym)
btn_ok = Button(fram, text='ОК', font=('Cambria, 10'), command=main)
btn_sur = Button(fram, text='Сдаться', font=('Cambria, 10'), width=25)

# fourth screen



root.mainloop()