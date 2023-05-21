# Найдите сумму цифр трехзначного числа.

num = int(input('Enter a three-digit number: '))
sum = 0
if num < 100 or num > 999:
    print('Error: Enter a three-digit number')
else:
    while num != 0:
        mod = num % 10
        sum += mod
        num //= 10
    print(sum)
