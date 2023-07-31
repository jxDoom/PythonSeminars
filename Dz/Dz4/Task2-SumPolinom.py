# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.

# Например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# Можно использовать модуль re

def completingDict(exponent):
    array = []
    dictionary = {}
    for i in range(exponent, -1, -1):
        tmp = [f'x^{i}', int(input(f'Введите коэффициент при x в степени {i} = '))]
        array.append(tmp)
    print()
    dictionary = dict(array)
    return dictionary

exp_max1: int = int(input('Введите максимальную натуральную степень первого многочлена: '))
exp_max2: int = int(input('Введите максимальную натуральную степень второго многочлена: '))

dict_plm1 = completingDict(exp_max1)
print('Первый многочлен:\n', dict_plm1)
print()
dict_plm2 = completingDict(exp_max2)
print('Второй многочлен:\n', dict_plm2)

# for key, value in dict_plm2.items():
#     if key in dict_plm1:
#         dict_plm1[key].extend(value)
#     else:
#         dict_plm1 = value

print(dict_plm1)