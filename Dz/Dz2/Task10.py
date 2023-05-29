# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Enter the total number of coins: '))
o = r = 0   #o = orel   r = reshka

for i in range(n):
    tmp = random.randint(0, 1)
    if tmp == 0:
        o += 1
    else:
        r += 1
print(f'Up is "orel": {o} coins and "reshka": {r} coins')

if o == n or r == n:
    print('All coins lie on the table with one side')
elif o > r:
    print(f'The number of coins to be flipped to the side "orel" is {r}')
elif o < r:
    print(f'The number of coins to be flipped to the side "reshka" is {o}')
else:
    print('The number of coins "orel" and "reshka" is the same,', end = " ")
    print('let the user choose which way to flip')
    print('Press "-1" - if you don\'t change anything,', end = " ")
    print('press "0" if you want to flip the coins to the side "orel",', end = " ")
    print('press "1" if you want to flip the coins to the side "reshka."')
    but = int(input('Enter number = '))
    if but == 0:
        print(f'{r} coins need to be flipped to the side "orel"')
    elif but == 1:
        print(f'{o} coins need to be flipped to the side "reshka"')
    elif but == -1:
        print('We leave everything as it is')
    else:
        print('Error: there is no such number')

