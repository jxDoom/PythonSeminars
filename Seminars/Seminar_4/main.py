# x: int = "Hello"    #Аннотация
# # y: int = " World"
# # print(x + y)

# def summa(x1, x2):
#     print(x1 + x2)

# def summa2(x1: int, x2: int) -> int:    #Функция возвращает значение int
#     global x
#     res: int = x1 + x2
#     return res

# summa(8,12)
# print(summa2(7,13))
# print(summa2("Hello ", "World "))

# Задача 25
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# sp = 'a a a b c a a d c d d'.split()
# new_sp = ''
# dictionary = {}
# for i in sp:
#     if i not in dictionary:
#         dictionary[i] = 1
#         new_sp += f'{i} '
#     else:
#         dictionary[i] += 1
#         new_sp += f'{i}_{dictionary[i] - 1} '
# print(new_sp)

# -----------------------------------------------------------------
# Другое решение
# sp = "a a a b c a a d c d d"
# new_list = sp.split()
# # print(new_list)
# new_ar = {}
# result = ""
# for i in new_list:
#     if i not in new_ar:
#         new_ar[i] = 0
#         result +=f"{i} "
#     else:
#         new_ar[i] += 1
#         result +=f"{i}_{new_ar[i]} "
# print(result)

# Задача 27
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# s = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# s = s.replace(".", " ").lower().split()
# print(len(set(s)))

# ---------------------------------------------------------------------------------------------

# Задача 29
# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить значение наибольшего элемента
# последовательности, которая завершается первым встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня
# n = int(input())
# max_number = 1000
# while n != 0:
#     n = int(input())
#     if max_number > n:
#         max_number = n
# print(max_number)

# Петя
# n = int(input())
# max_number = -1
# while n < 0:
#     n = int(input())
#     if max_number < n:
#         n = max_number
# print(n)

# def Max_Number() -> int:
#     flag = True
#     max_number: int = 0
#     while flag:
#         n: int = int(input())
#         if n == 0:
#             break
#         if max_number < n:
#             max_number = n
#     return max_number
# print('Max value =', Max_Number())

# ---------------------------------------------------------------------------------------\

# ДОП задача - Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать как многочлен степени k.
#     *Пример:* 
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введите натуральную максимальную степень "))
# sp = [randint(-100, 100) for _ in range(k + 1)]
sp = [randint(0, 100) for _ in range(k + 1)]
print(sp)
res = ''
for i in range((len(sp)-1), -1, -1):    
    if sp[i] == 0:
        res += ''
    elif sp[i] == 1 and i == 0:
        res += '1 + '
    elif sp[i] == 1 and i == 1:
        res += 'x + '
    elif sp[i] == 1:
        res += f'x^{i} + '
    elif i == 0:
        res += f'{sp[i]} + '
    elif i == 1:
        res += f'{sp[i]}x + '
    else:    
        res += f'{sp[i]}x^{i} + '
print(res[:-3], '= 0')
#print(res[:-3].replace('+ -', '- '), '= 0')