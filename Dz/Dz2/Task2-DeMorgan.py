# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Теперь надо проверить ее практически, в цикле 100 раз прогоняем
# каждый раз генерируем случайное количество предикат от 3 до 15
# и конечно со случайным булевым значением и засекаем общее время выполнения программы.
# Юзаем библиотеки random и time.
# Предикаты НЕ ЗАДАЕМ как целое число!

from random import choice, randint
from time import time
start = time()
k = 0

while(k < 100):
    sp = [choice([True, False]) for i in range(randint(3, 15))]
    # print(sp)
    left_side = False
    right_side = True
    
    for i in range(len(sp)):
        tmp_left = sp[i]
        left_side = left_side or tmp_left
        tmp_right = sp[i]
        right_side = right_side and not tmp_right

    if not left_side == right_side:
        print('Statement is true')
    else:
        print('Statement is false')
    k += 1

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

# ------------------------------------------------------------------------------------------------------------
"""
from random import *
# x = choice([True,False])
# y = choice([True,False])
# z = choice([True,False])

def predicate_generator(predicate_count):
    predicates = []
    for i in range(predicate_count):
        predicates.append(choice([True,False]))
    return predicates



def de_morgan(predicates):
    left_side = predicates[0]
    right_side = not predicates[0]
    for i in range(1,len(predicates)):
        left_side = left_side or predicates[i]
        right_side = right_side and not predicates[i]
    return not left_side == right_side       
        

j = 0
while(j < 100):
    count_predicate = randint(3,15)
    print(de_morgan(predicate_generator(count_predicate)))
    j += 1
"""
