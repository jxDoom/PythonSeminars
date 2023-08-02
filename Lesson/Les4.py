# def funct(x):
#     return x*x

# a = funct
# print(a(5))
# print(funct(5))

# def calc1(a):
#     return a + a

# def math(op, x):
#     print(op(x))

# math(calc1, 5)


# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# math(calc2, 5, 25)

# Применение лямбда-функции (аналог генератора списков list comprehension)
# def math(op, x, y):
#     print(op(x, y))

# # calc1 = lambda a, b: a + b

# # math(calc1, 5, 45)
#math(lambda a, b: a + b, 5, 45)

# Задача 1
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# print(list((i, i**2) for i in sp if i % 2 == 0))    #List Comprehension

# Через лямбда-функции
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# sp = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, sp)
# print(res)
# res = where(lambda x: x % 2 == 0, sp)
# print(res)
# res = select(lambda x: (x, x**2), res)
# print(res)