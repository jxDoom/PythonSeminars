# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Теперь надо проверить ее практически, в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением и засекаем общее время выполнения программы.
# Юзаем библиотеки random и time.
# Предикаты НЕ ЗАДАЕМ как целое число!

from random import choice
from time import time
start = time()
#sp = ['X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
for _ in range(100):
    x = choice([True, False])
    y = choice([True, False])
    z = choice([True, False])
    #print(('X = {}, Y = {}, Z = {}').format(x, y, z))

    if not(x or y or z) == (not x and not y and not z):
        print(' ', end = '')
    else:
        print('false')
print()
print(time()-start)