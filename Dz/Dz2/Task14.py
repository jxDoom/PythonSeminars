# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

k = int(input('Enter the power of a number: '))

for i in range(k + 1):
    print(f'2^{i} =  {2 ** i}')