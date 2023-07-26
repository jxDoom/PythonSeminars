# Задача
# Необходимо создать функцию sumNumbers(), которая будет считать сумму всех элементов от 1 до n

# def sumNumbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sumNumbers(5, 'qwerty'))

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# print(sum_str('H', 'e', 'l', 'l', 'o'))

# import modul1
# print(modul1.max1(5, 9))

# from modul1 import max1
# print(max1(5, 3))

# import modul1 as m1
# print(m1.max1(5, 9))

# Задача
# Пользователь вводит число n. Необходимо вывести n-первых членов последовательности Фибоначчи

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))

# print(list_1)

# Быстрая сортировка ("Разделяй и влавствуй")
"""
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([321, 6, 88, 651, 86, 6, 2, 8, 3, 4]))
"""

# Сортировка слиянием

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list_1 = [321, 6, 88, 651, 86, 6, 2, 8, 3, 4]
merge_sort(list_1)
print(list_1)