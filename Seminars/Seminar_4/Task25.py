# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# Решение с помощью срезов
# s = 'a a a b c a a d c d d'.split()
# final_string = ''
# print(s)

# for i in range(len(s)):
#     if s[0:i].count(s[i]) == 0:
#         final_string += f' {s[i]}'
#     else:
#         final_string += f' {s[i]}_{s[0:i].count(s[i])}'
# print(final_string)
# # Метод count() возвращает количество раз, когда указанный элемент появляется в списке

# Решение с помощью словаря
# el = {}

# for i in s:
#     if i not in el:
#         el[i] = 1
#         final_string += f'{i} '
#     else:
#         el[i] += 1
#         final_string += f'{i}_{el[i]-1} '
# print(final_string)

# Используя .get() - заменяет строки 29 и 32 прошлого решения

word = 'a a a b c a a d c d d'.split()
result = {}
for i in word:
    if i in result:
        print(f'{i}_{result[i]}', end = ' ')
    else:
        print(i, end = ' ')
    result[i] = result.get(i, 0) + 1
    print(i, result)