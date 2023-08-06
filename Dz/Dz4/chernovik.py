# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# Например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# Можно использовать модуль re

import re

def elem(spisok):
    for i in range(len(spisok)):
        ch = '^'
        if ch in spisok[i]:
            spisok[i] = spisok[i-1] + spisok[i]
            spisok[i-1] = 0
    return spisok

plm1 = '2x^2 + 4x + 5 = 0'
plm2 = '5x^3 - *x^2 + 5x - 12 = 0'
plm1 = plm1.replace('*', '')
plm2 = plm2.replace('*', '')
plm1 = re.sub(r'\s+', '', plm1)    #убрали все пробелы в строке
plm2 = re.sub(r'\s+', '', plm2)

regex = r'[+-^]?\w+(?:\.\w+)?'
reg = r'/(?!^)(?=.)/u'

sp_s1 = re.findall(regex, plm1)
sp_s2 = re.findall(regex, plm2)
print(sp_s1)
print(sp_s2)

sp_s1 = elem(sp_s1)[:-1]
sp_s2 = elem(sp_s2)[:-1]

while 0 in sp_s1:
    sp_s1.remove(0)
while 0 in sp_s2:
    sp_s2.remove(0)

sp_s1 = [re.findall(regex, sp_s1[i]) for i in range(len(sp_s1))]
sp_s2 = [re.findall(regex, sp_s2[i]) for i in range(len(sp_s2))]
print(sp_s1)
print(sp_s2)

# for i in range(len(sp_s1)):
#     for j in range(len(sp_s2)):
#         if len(sp_s1[i]) == 2 and len(sp_s2[j]) == 2 and sp_s1[i][1] == sp_s2[j][1]:
#             tmp1 = int(sp_s1[i][0].replace('x', ''))
#             tmp2 = int(sp_s2[j][0].replace('x', ''))
#             tmp = tmp1 + tmp2
#             print(tmp)









    # if len(sp[i]) == 2:
    #     if sp[i][1] == [sp[i][1] for j in range(i+1, len(sp[i]))]:
    #         sp[i][0] += 1
    #         print(sp[i][0])
    # print(sp[i][0])
    #     # for j in range(len(sp[i])):
            