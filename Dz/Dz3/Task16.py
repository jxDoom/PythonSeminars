# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

lst = list()
size = int(input('Enter list size = '))
n = int(input('Enter max number in the array = '))
count = 0

try:
    n > 1
    find = int(input('What number are you looking for?\n'))

    for i in range(size):
        lst.append(random.randint(1, n))
        if lst[i] == find:
            count += 1
    print(lst)
    print(f'Number {find} appeared {count} times in the array')
except:
    exit('ValueError')
