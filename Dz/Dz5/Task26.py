# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# Моё решение
a: int = int(input('Enter number: '))
b: int = int(input('Enter exponent: '))
def expo(num, exponent):
    if exponent < 2:
        return num
    return num * expo(num, exponent-1)
    
print(expo(a, b))

# Решение из автотеста
# a: int = int(input('Enter number: '))
# b: int = int(input('Enter exponent: '))
# def expo(num, exponent):
#     if exponent == 0:
#         return 1
#     return num * expo(num, exponent-1)
    
# print(expo(a, b))