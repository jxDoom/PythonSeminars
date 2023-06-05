# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

# Решение с помощью срезов
s = 'a a a b c a a d c d d'.split()
final_string = ''
print(s)

for i in range(len(s)):
    if s[0:i].count(s[i]) == 0:
        final_string += f' {s[i]}'
    else:
        final_string += f' {s[i]}_{s[0:i].count(s[i])}'
print(final_string)

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

# Используя .get()

# s = 'aaabcaadcdd'
# s = list(s)
# print(s)
# m = {}
# str = ''

# for i in range(len(s)):
#     if m.get(s[i]) != None:
#         m[s[i]] = int(m[s[i]]) + 1
#     else:
#         m[s[i]] = 1
#     str += f'{s[i]}_{m[s[i]]} '
# print(str)