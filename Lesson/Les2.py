# Списки list()
# list_1 = []
# list_1 = list()
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(*list_1)

# for i in list_1:
#     print(i)

# print(len(list_1))

# print(list_1[3])
# print(list_1[-1])

# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)    #добавляем элемент к списку - метод append
# print(list_1)

# list_1 = []
# for i in range(5):
#     list_1.append(i)
# print(list_1)

# Удаление последнего элемента из списка - метод pop
# list_1 = [12, 7, -1, 21, 0]
# a = list_1.pop()  #также функция pop возвращает значение
# print(a) # 0   
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# Удаление конкретного элемента из списка
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию - функция insert
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.insert(2, 11))
# print(list_1) # [12, 7, 11, -1, 21, 0]

# Срез списка
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) # [9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# # Кортежи tuple()
# t = ()  #кортеж
# print(type(t))

# t = (1)   #int
# print(type(t))

# t = (1,)  #кортеж
# print(type(t))

# v = [1, 8, 9]   #список
# print(v)
# print(type(v))

# v = tuple(v)    #кортеж
# print(v)
# print(type(v))

# a, b = 1, 2
# print(a, b)

# v = tuple([1, 8, 9])
# a, b, c = v    #распаковка кортежа
# print(a, b, c)

# t = (1, 2, 3, 5,)

# # for i in t:
# #     print(i)

# for i in range(len(t)):
#     print(t[i])

# Словари dict()

# d = {}
# d = dict()

# d['q'] = 'qwerty'
# d['w'] = 'werty'
# d['e'] = 'erty'
# print(d)
# print(d['w'])
# del d['q']
# print(d)

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# print(dictionary)
# for item in dictionary:
#     print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# left: ←
# down: ↓
# right: →
# for (k, v) in dictionary.items():   #k - ключ, v - значение
#     print(f'{k}:', v)
# up: ↑
# left: ←
# down: ↓
# right: →

# Множества set()

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok

# Операции со множествами
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} - копирование множества
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} - объединение множеств
# i = a.intersection(b) # i = {8, 2, 5} - пересечения множеств
# dl = a.difference(b) # dl = {1, 3} - разности множеств
# dr = b.difference(a) # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} #сначала то что в скобках, дальше union и третье ищем разность между множествами

# Неизменяемое или замороженное множество frozenset()

# a = {1, 8, 6}
# b = frozenset(a)
# print(b)

#Задача: Создать список,состоящийиз четных чисел от 1 до 100:
# list_1 = [i for i in range(1, 101) if i%2 == 0]
# print(list_1)

#Добавим пару каждому из чисел (кортежи):
# print([(i, i) for i in range(1, 101) if i%2 == 0])

#Умножить значение на 2:
# print([i * 2 for i in range(10) if i%2 == 0])

#Возвести значение в 3 степень:
# print([i ** 3 for i in range(11) if i%2 == 0])
