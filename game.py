import random

# создаёт список всех возможных ответов
def get_all_answer():
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
def del_bad_answers():
    pass

#answers = get_all_answer()
#player = input_number()
#enemy = get_one_answer(answers)

a, b = check([1 ,2 ,3, 4], [2, 4, 6, 8])
print(a, b)
