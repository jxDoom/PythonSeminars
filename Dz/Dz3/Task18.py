# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

lst = list()
size = int(input('Enter list size = '))
n = int(input('Enter max number in the array = '))
index = 0

try:
    n > 1
    num = int(input('Enter some number: '))

    for i in range(size):
        lst.append(random.randint(1, n))
    print(lst)
    dif = abs(num - lst[0])

    for i in range(1, len(lst)):
        differance = abs(num - lst[i])
        if differance < dif:
            dif = differance
            index = i
    print(f'Index of close element = {index + 1} => value = {lst[index]}')
except:
    exit('ValueError')