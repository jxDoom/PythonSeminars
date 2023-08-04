# def create_phrase(func, word):
#     print(func(word))

# def hello(s):
#     return f"Hello {s}"

# def bye(s):
#     return f"{s} bye-bye"

# create_phrase(hello, " world")
# create_phrase(hello, " Timur")
# create_phrase(bye, " world")
# create_phrase(bye, " Timur")

# def calc_power(degree):
#     def power(number):
#         return number ** degree
#     return power

# print(calc_power(2)(3))
# square = calc_power(2)
# print(type(square))
# cube = calc_power(3)

# print(square(8))
# print(cube(3))
# print((lambda x,y: x+y) (5,8))
# calc = {"+": lambda x,y: x+y,
#         "-": lambda x,y: x-y,
#         "*": lambda x,y: x*y,
#         "/": lambda x,y: x/y
#         }
# print(calc[input("Введите операцию")](5,15))
# print(calc["*"](5,300))
# names=["Петя", "Ваня"]
# sp = [5, 8, 1, 11, 3, 2]
# print(*map(lambda item: item**2,sp))
# print(list(map(lambda item: item**2,sp)))
# print(list(map(lambda item: item**2 if item>5 else 0,sp)))
# print(*filter(lambda item: True if item>5 else False,sp))
# print(list(filter(lambda item:  item>5 ,sp)))
# print(*sp)
# for i,v in enumerate(sp):
#     print(i,v)

# for x1,x2 in zip(names, sp):
#     print(x1,x2)

# --------------------------------------------------------------------------------------------------
# Задача 47
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# values = [1, 23, 42, 'asdfg']
# transformed_values = list(map(lambda n: n, values))
# print(transformed_values)
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')

# ------------------------------------------------------------------------------------
# Задача 49
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# def find_farthest_orbit(orbits):
#     S = list(map(lambda item: 3.14*item[0]*item[1] if item[0] != item[1] else 0, orbits))
#     return f"Самая далекая планета имеет индекс {S.index(max(S))}"

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))

# --------------------------------------------------------------------------------
# Задача 51
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by(characteristic, objects):
   
#     el = len(list(filter(characteristic,objects)))
#     print(el)
#     return not el or el == len(objects)

# values = [0, 2, 10, 6]
# values2 = [1, 3, 5, 7]

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')
# ----------------------------------------------------------------------------------
# Доп задача
# Необходимо написать программу для автоматического перевода различных валютных счетов в рублевые.
# Начальные данные программы это три различных списка - Фамилии владельцев банковских счетов,
# указание валют счетов, соответствующее состояние счетов.
# То есть у Иголкина счет в евро и там лежит 50000, и так далее.
# Также вначале заданы отношения курса рубля к доллару и евро.

# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99

# Вам необходимо написать функцию calc, которая на входе принимает только один аргумент,
# далее надо применить ее в комбинациях с map и zip.

# На выходе программы должны быть три пары значений - фамилии владельцев счетов и состояние рублевого счета.

# def calc(currency, balance):
#     result = balance
#     if currency == "доллар":
#         result *= dollar
#     elif currency == "евро":
#         result *= euro
#     return result
    
# surnames = ["Иванов", "Карпов", "Иголкин"]
# currency_name = ["рубль", "доллар", "евро"]
# balances = [30000, 40000, 50000]
# dollar = 90
# euro = 99

# new_ballances = list(map(calc, currency_name, balances))
# print(*zip(surnames, new_ballances))