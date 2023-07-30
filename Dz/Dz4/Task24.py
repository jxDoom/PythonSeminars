# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод —на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint

count: int = int(input('Enter number of bushes: '))
sum3 = 0
max_sum3 = 0
index = 0
n = [randint(0, 15) for i in range(count)]
i = 1 - count
print(n)

while i < 1:
    sum3 = n[i-1] + n[i] + n[i+1]
    if sum3 > max_sum3:
        max_sum3 = sum3
        index = i
    i += 1

print(f'Maximum number of berries = {max_sum3}', end = ' ')
if index+count+1 == count:
    # index = count
    print(f'in the bushes: {count-1}, {count}, {1}')
elif index+count+1 == count+1:
    # index = 0
    print(f'in the bushes: {count}, {1}, {2}')
else:
    index = index+count+1
    print(f'in the bushes: {index-1}, {index}, {index+1}')
