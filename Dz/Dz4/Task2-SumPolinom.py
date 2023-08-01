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

def priorityDict(dict_max, dictionary):
    for key, value in dictionary.items():
        if key in dict_max:
            dict_max[key] += value
        else:
            dict_max = value
    return dict_max

def equationPrint(dictionary):
    res = ''
    for key, value in dictionary.items():    
        if value == 0:
            res += ''
        elif value == -1 and key == 'x^0':
            res += '-1 + '
        elif value == 1 and key == 'x^0':
            res += '1 + '
        elif value == -1 and key == 'x^1':
            res += '-x + '
        elif value == 1 and key == 'x^1':
            res += 'x + '
        elif value == -1:
            res += f'-{key} + '
        elif value == 1:
            res += f'{key} + '
        elif key == 'x^0':
            res += f'{value} + '
        elif key == 'x^1':
            res += f'{value}x + '
        else:
            res += f'{value}{key} + '
    
    res = res[:-3].replace('+ -', '- ')
    return res

exp_max1: int = int(input('Введите максимальную натуральную степень первого многочлена: '))
dict_plm1 = completingDict(exp_max1)
print('Первый многочлен:\n', equationPrint(dict_plm1), '= 0')
print()
exp_max2: int = int(input('Введите максимальную натуральную степень второго многочлена: '))
dict_plm2 = completingDict(exp_max2)
print('Второй многочлен:\n', equationPrint(dict_plm2), '= 0')
print()

if len(dict_plm2) > len(dict_plm1):
    print('Результирующий многочлен:\n', equationPrint(priorityDict(dict_plm2, dict_plm1)), '= 0')
else:
    print('Результирующий многочлен:\n', equationPrint(priorityDict(dict_plm1, dict_plm2)), '= 0')