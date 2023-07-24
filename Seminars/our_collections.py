# first_list = [9, 'rus', True, [1, 2, 3]]

# for i, element  in enumerate(first_list):
#     if element == 9:
#         first_list[i] = 'nine'

# print(first_list.index(1))

# first_list.remove(9)
# first_list.sort и sorted(first_list) - вопрос на собесах (None и отсортированный массив по возрастанию)
# print(first_list.sort)

# first_set = set([1,1,1,2,3,4])
# # print(first_set)
# second_set = set([2, 3])
# print(second_set.issubset(first_set))

# first_tuple = (1, 'eru', True)

# a = (1,1,1,5,65,1,2,684,8,1,2,24)
# print(list(set(a)))

# first_dict = {'Mother':23816546, 'Father':56746568, 'Friend':56841689}

# for key in first_dict:
#     print(first_dict[key])

# print(first_dict.)

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# a = [1,2,5,4,1,2,4,1,4]
# print(len(set(a)))
# ---------------------------------------------------------
# import random

# list_1 = list()

# for i in range(0, 10):
#     n = random.randint(-1, 10)
#     list_1.append(n)
# print(list_1)
# print(set(list_1))
# result = len(set(list_1))
# print(result)

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
"""
list_1 = []
length = int(input('Enter length of list > '))
k = int(input('k = '))
for i in  range(length):
    list_1.append(int(input()))

print(list_1)

for i in range(k):
    tmp = list_1[-1]
    list_1.insert(0, tmp)
    list_1.pop()

print(list_1)

---------------------------------------------
print("Enter num")
num=int(input())
arr.clear()
for i in range(num):
    arr.append(rand.randint(0,10))

print("Enter k")
k=int(input())
print(arr)
arr2=arr[:len(arr)-k]
arr3=arr[len(arr)-k:]
arr3.append(arr2)
print(arr3)
----------------------------------------"""
# list = [1, 2, 3, 4, 5]
# k = int(input('k = '))

# for i in range(k - 1):
#     list.insert(0, list.pop())
# print(list)

# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# data = [{"V": "S001"},
#         {"V": "S002"},
#         {"VI": "S001"},
#         {"VI": "S005"},
#         {"VII": " S005 "},
#         {" V ":" S009 "},
#         {" VIII ":" S007 "}]

# print(set(data.values())) #если бы бы просто список, решалось бы так, у нас список словарей!

# data = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005"},
#     {"V": "S009"},
#     {"VIII": "S007"}
# ]

# unique_values = set()

# for item in data:
#     for value in item.values():
#         unique_values.add(value.strip())  # Добавляем уникальные значения в множество

# print(list(unique_values))

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# list = [0,-1,5,2,3]
# count = 0
# for i in range(len(list)-1):
#     if list[i]<list[i+1]:
#         count+=1    
# print(count)


#[a for a in input().split()]

# a = [int(a) for a in input().split() if int(a)>0]
# print(a)

# -----------------------------------------------------------------------------------------------------------

# sp = []
# sp.append(5)
# sp.expend(7,8,True)
# sp.insert(0,5.7)
# sp = sp + [1,2,True,44]   # конкатенация
# print(sp)
# print(sp[3::])
# print(sp[2:5])
# print(sp[-5])
# a = sp.pop()
# print(a)
# sp.remove(True)
# del sp[0]

# for i,k in enumerate(sp):
#     print(i,k)
# print(sp)
# t = [4,8,9]
# print(t[0])

# d = {}
# d["дядя Ваня"] = "+78465564"
# d["дядя Вова"] = "+12312131"
# print(d)
# for key, value in d.items():
#     print(key, value)

# print(d.keys())
# print(d.values())

# s = set()
# s.add(5)
# s.add(7)
# print(s)
# print(5 in s)
# # list tuple dict set

# Задача 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
"""
import random
size = int(input('Enter size: '))
sp = []
for i in range(size):
    sp.append(random.randint(-5, 5))
print(sp)

s = []  #новый список из неповторяющихся чисел
for i in sp:
    if i not in s:
        s.append(i)
print(s)
print(len(s))
"""
# -------------------------------
# list = set(sp)
# print(list)
# print(len(list))

# Задача 19
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 2
# Output: [4, 5, 1, 2, 3]

# sp = [1, 2, 3, 4, 5]
# k = int(input('Enter number: '))

# for _ in range(k):
#     sp.insert(0, sp.pop())
# print(sp)

# ---------------------------------------
# sp1 = sp[:len(sp) - k]
# sp2 = sp[len(sp) - k:]
# sp2.append(sp1)
# print(sp2)

# Задача 21
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
dictionary = []
sp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
for i in sp:
    for key, values in i.items():
        if values.strip() not in dictionary:
            dictionary.append(values.strip())
print(dictionary)
"""
# ---------------------------------------
# dictionary = {"V": "S001", "V": "S002", "VI": "S001","VI": "S005", "VII": " S005 ", " V ":" S009 "," VIII":" S007 "}

# print(dictionary)
# sp = []



# for values in dictionary.values():
#     temp = values.strip()
#     if temp not in sp:
#         sp.append(temp)
        
# print(sp)

# Задача 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
"""
sp = [0, -1, 5, 2, 3]
count = 0
i = 1
while i < len(sp):
    if sp[i] > sp[i-1]:
        count += 1
    i += 1
print(count)
"""

# Дополнительная задача
# Дан некоторый список чисел, задача - найти сколько раз встречается введенная пользователем цифра
# например был список [1,15,55,7.58,0,99]
# и пользователь ввел 5
# ответ будет 4

# n = [1, 15, 55, 7.58, 0, 99]
# count = 0
# i = 0
# while i < len(n):
#     if n[i]//10 or n[i]%10 or n[i]%0.6 == 5:
#         count += 1
#     i += 1
# print(count)

"""
from decimal import *

def numbers_after_dot_converter(number):
    numbers_after_dot = (Decimal (str(number)).as_tuple().exponent*(-1))
    while numbers_after_dot > 0:
        number *= 10
        numbers_after_dot -= 1
    return round(number)

def calc(list):
    count = 0
    for i in range(len(list)):
        while list[i] != 0:
            if list[i] % 10 == 5:
                count += 1
            list[i] = list[i] // 10
    return count

sp = [1,15,55,7.58,0,99]

sp2 = []
for i in range(len(sp)):
    sp2.append(numbers_after_dot_converter(sp[i]))
    
print(sp)
print(sp2)
a = calc(sp2)
print(a)
"""