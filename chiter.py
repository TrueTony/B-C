import game

answers = game.get_all_answers
counter = 0
while len(answers) != 1:
    counter += 1
    print('Ход номер {}'.format(counter))
    print('Возможных вариантов ответа: {}'.format(len(answers)))
    ans = game.get_one_answer(answers)
    print('Назови комбинаци: {}'.format(ans))
    bulls = int(input('Сколько быков?'))
    cows = int(input('Сколько коров?'))
    answers = game.del_bad_answers(answers, ans, bulls, cows)
print('Ответ: {}'.format(answers))