#запилит ьчперез tkinter!!!

import random

# создаёт список всех возможных ответов
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # print(tmp)
        #if len(set(map(int, tmp))) == 4:
        #    ans.append(list(map(int, tmp)))
    #print(ans)
        lst = ['x' for num in tmp if tmp.count(num) == 1]
        if len(lst) == 4:
            ans.append(list(map(int, tmp)))
    return ans

# выбирает один ответ из списка возможных
def get_one_answer(ans):
    num = random.choice(ans)
    return num

# запрашивает упольщователя неповторяющиеся цифры
def input_number():
    while True:
        nums = input('Введите 4 неповторяемые цифры: ')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums

# сравнивает два сисла и сообщает кол-во быков и коров
def check(nums, true_num):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_num:
            if nums[i] == true_num[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

# удаляет неподходящие варианты из списка возможных
def del_bad_answers(ans, enemy_try, bull, cow):
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull and temp_bull != cow:
            ans.remove(num)
    return ans


if __name__ == '__main__':
    print('Игры Быки и Коровы')
    answers = get_all_answers()
    player = input_number()
    enemy = get_one_answer(answers)

    while True:
        print('=' * 15, 'Ход игрока', '=' * 15)
        print('Угадайте число компьютера')
        number = input_number()
        bulls, cows = check(number, enemy)
        print('Быки {}, Коровы {}'.format(bulls, cows))
        if bulls == 4:
            print('Победил игрок!')
            print('Компьютер загадал {}'.format(enemy))
            break

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

