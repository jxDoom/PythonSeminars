# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

a: int = int(input('Initial value number: '))
b: int = int(input('Final value number: '))

size_n: int = int(input('Enter size first set = '))
size_m: int = int(input('Enter size second set = '))

n = [randint(a, b) for i in range(size_n)]
print(n)
n = set(n)

m = [randint(a, b) for i in range(size_m)]
print(m)
m = set(m)

u = list(n.union(m))
u.sort()
print(*u)
