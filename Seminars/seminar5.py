# def Summ_rec(N):
#     if N == 0:
#         return 0
#     return N + Summ_rec(N-1)

# #(4  + (3 + (2 + (1 + 0) ) ) )
# #(4 + ( 3 + 3))
# #10

# print(Summ_rec(4))

# Задача 31
# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def Fibo_find(n):
#     # if n == 0:
#     #     return 0
#     # if n == 1:
#     #     return 1
#     if n == 0 or n == 1:
#         return n
#     return Fibo_find(n-2) + Fibo_find(n-1)

# print(Fibo_find(10))

# ---------------------------------------------------------------------------------------------
# Задача 33
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# def Rating(num, i = 0):
#     if i == len(num):
#         return num
#     if num[i] == max(num):
#         num[i] = min(num)
#     Rating(num, i + 1)

# str1 = [1, 3, 4, 3, 4]
# Rating(str1)
# print(str1)

# ---------------------------------------------------------------------------------------
# Задача на рекурсию (хард)

def Staff(count_all):
    summ = 0
    for i in count_all:
        if type(i) == int:
            summ += 1
        else:
            Staff(count_all)
        return summ


count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]

print(Staff(count_all))

# Решеная задача
"""
count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york, count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)


def count(element):
    if type(element) == int:
        return element

    summa = 0
    for elem in element:
        if type(element) == list:
            summa += count(elem)
        else:
            summa += elem
    return summa
"""

# Другое решение
"""
count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york, count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)


def count(element):
    if type(element) == int:
        return element

    summa = 0
    for elem in element:
        summa += count(elem)
    return summa
"""

# ----------------------------------------------------------------------------------------
# Задача 35
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

# def primeNum(num, i = 2):
#     if i == num:
#         return True
#     if num % i == 0:
#         return False
#     return primeNum(num, i + 1)


# n: int = int(input('Enter number: '))
# print(primeNum(n))