# Посчитать сумму цифр любого целого или вещественного числа. Через строку решать нельзя.

from decimal import *

number = input('Enter any number: ')
num = Decimal(str(number))
getcontext().prec = len(str(number))

while num % 1 != 0:
    num *= 10
num = int(num)    
result = 0

while num > 0:
    result += num % 10
    num //= 10
print(f'The sum of the digits in a number {number} equals {result}')











# symbol = '.'

# if symbol in num:
#     num = float(num)
#     num.pop()
#     print(num)
# else:
#     num = int(num)
#     result = 0

#     while num > 0:
#         result += num % 10
#         num //= 10
#     print(result)
