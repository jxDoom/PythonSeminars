# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random

a = int(input('Initial value number: '))
b = int(input('Final value number: '))

if a >= 0 and b >= 0 or a < 0 and b < 0:
    size_n = int(input('Enter size first set = '))
    size_m = int(input('Enter size second set = '))

    n = [random.randint(a, b) for i in range(size_n)]
    print(n)
    n = set(n)

    m = [random.randint(a, b) for i in range(size_m)]
    print(m)
    m = set(m)

    print(n.union(m))
else:
    print('Error: re-enter numbers')