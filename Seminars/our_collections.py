first_list = [9, 'rus', True, [1, 2, 3]]

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