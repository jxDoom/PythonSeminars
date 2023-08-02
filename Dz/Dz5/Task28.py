# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Моё решение
a: int = int(input('Enter number 1: '))
b: int = int(input('Enter number 2: '))
def sumNumbers(num_1, num_2):
    if num_2 == 0:
        return num_1
    return sumNumbers(num_1+1, num_2-1)
    
print(sumNumbers(a, b))

# Решение из автотеста (странное, решает не ту задачу и вообще можно заменить на return b)
def sum(a, b):
  if b == 0:
    return 0
  return sum(a, b - 1) + 1
