# Напишите функцию вывода таблицы умножения
# print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

# Пример:

# Ввод: `print_operation_table(lambda x, y: x * y)` 
# Вывод:
# 1  2  3  4  5  6
# 2  4  6  8 10 12
# 3  6  9 12 15 18
# 4  8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

# Для прямоугольной (произвольной) матрицы
# def print_operation_table(num_rows, num_columns):
#     for i in range(1, num_rows + 1):
#         for j in range(1, num_columns + 1):
#             print(i * j, end = '\t')
#         print(sep = '\n')
#     return 0

# x: int = int(input('Enter quantity rows: '))
# y: int = int(input('Enter quantity columns: '))
# print_operation_table(x, y)


# Другое решение
print_operation_table = lambda x, y: (('\n'.join('\t'.join(f'{i * j}' for j in range(1, y + 1)) for i in range(1, x + 1))))

num_rows: int = int(input('Enter quantity rows: '))
num_columns: int = int(input('Enter quantity columns: '))
print(print_operation_table(num_rows, num_columns))

# ----------------------------------------------------------
# Для квадратной матрицы (частный случай)
# def print_operation_table(multi):
#     for num_columns in range(1, multi + 1):
#         for num_rows in range(1, multi):
#             print(num_rows * num_columns, end = '\t')
#         print(num_columns * multi)
#     return 0

# num: int = int(input('Enter the maximum multiplier: '))
# print_operation_table(num)


# Другое решение
# print(*(lambda x: ('\t'.join(f'{i * j}' for j in range(1, x)) for i in range(1, x)))(int(input('Enter the maximum multiplier: ')) + 1), sep = '\n')
