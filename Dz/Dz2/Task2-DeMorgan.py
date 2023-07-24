# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Теперь надо проверить ее практически, в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением и засекаем общее время выполнения программы.
# Юзаем библиотеки random и time.
# Предикаты НЕ ЗАДАЕМ как целое число!

from random import choice, randint
from time import time
start = time()

for _ in range(100):
    sp = ['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    new_sp = list()
    for i in range(randint(3, 15)):
        sp[i] = choice([True, False])
        new_sp.append(sp[i])
    
    #print(new_sp)
    left_side = False
    right_side = True
    
    for i in range(len(new_sp)):
        tmp_left = new_sp[i]
        left_side = left_side or tmp_left
        tmp_right = new_sp[i]
        right_side = right_side and not tmp_right

    if not left_side == right_side:
        print('Statement is true')
    else:
        print('Statement is false')

end = time()-start
print(end)


# ------------------------------------------------------------------------------------------------------------
# x = choice([True, False])
# y = choice([True, False])
# z = choice([True, False])
# #print(('X = {}, Y = {}, Z = {}').format(x, y, z))

# if not(x or y or z) == (not x and not y and not z):
#     print('true')
# else:
#     print('false')

# ------------------------------------------------------------------------------------------------------------
# from random import choice, randint
# from time import time

# def func(*arguments):
#     for item in arguments:
#         print(f'{item} = {choice([True, False])}')
        
# func('x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
