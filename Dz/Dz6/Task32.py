# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
# На входе: [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

ListGenerate = lambda size: [randint(-100, 100) for i in range(size)]

def FindIndex(spisok, min_num, max_num):
    index = []
    for item, element in enumerate(spisok):
        if element > min_num and element < max_num:    #min_num < element < max_num
            index.append(item)
    return index

def Start():
    size: int = int(input('Определите размер массива: '))
    if size > 0:
        sp = ListGenerate(size)
        print(sp)
        #minimum: int = int(input('Заданный минимум = '))
        #maximum: int = int(input('Заданный максимум = '))
        minimum = -25
        maximum = 40
        if maximum > minimum and maximum - minimum > 1:
            print(FindIndex(sp, minimum, maximum))
        else: print(-1)
    else: print(0)

Start()