# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('Enter the total number of coins: '))
orel = reshka = 0

for _ in range(n):
    tmp = random.randint(0, 1)
    if tmp == 0:
        orel += 1
    else:
        reshka += 1
print(f'Up is "orel": {orel} coins and "reshka": {reshka} coins')

if orel == n or reshka == n:
    print('All coins lie on the table with one side')
elif orel > reshka:
    print(f'The number of coins to be flipped to the side "orel" is {reshka}')
elif orel < reshka:
    print(f'The number of coins to be flipped to the side "reshka" is {orel}')
else:
    print('The number of coins "orel" and "reshka" is the same,', end = " ")
    print('let the user choose which way to flip\n')
    print('Press "-1" - if you don\'t change anything,', end = " ")
    print('press "0" if you want to flip the coins to the side "orel",', end = " ")
    print('press "1" if you want to flip the coins to the side "reshka."')
    
    but = int(input('Enter number = '))
    if but == 0:
        print(f'{reshka} coins need to be flipped to the side "orel"')
    elif but == 1:
        print(f'{orel} coins need to be flipped to the side "reshka"')
    elif but == -1:
        print('We leave everything as it is')
    else:
        print('Error: there is no such number')

