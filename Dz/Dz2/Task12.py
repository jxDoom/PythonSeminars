# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('First hint: Enter the sum of two numbers = '))
p = int(input('Second hint: Enter the product of two numbers = '))

# x + y = S and x * y = P
# y = S - x => x * (S - x) = P => x^2 - Sx + P = 0
# According to the Vieta theorem (x^2 + bx + c = 0):
# x1 + x2 = -b and x1 * x2 = c
# x^2 - Sx + P = 0
# d = (-s)^2 - 4 * 1 * p => a = (d)^0.5
# x = (s + a)/(2 * 1)
# y = (s - a)/(2 * 1)

d = (-s) ** 2 - 4 * p
if d > 0:
    a = d ** 0.5
    x = int((s + a)/2)
    y = int((s - a)/2)
    if 0 <= x < 1001 and 0 <= y < 1001:
        print(f'These numbers are equal: X = {x} and Y = {y}')
    else:
        print('According to the condition of the problem,', end = " ")
        print('we have only natural numbers from 0 to 1000')
elif d == 0:
    x = y = s/2
    if 0 <= x < 1001 and 0 <= y < 1001:
        print(f'These numbers are equal: X = Y = {x}')
    else:
        print('According to the condition of the problem,', end = " ")
        print('we have only natural numbers from 0 to 1000')
else:
    print('Error: Task solution does not exist')

# Verification

if x + y == s and x * y == p:
    print('Success')
else:
    print('Error: There is a fractional part in the discriminant,', end = " ")
    print('according to the condition of the problem, we have natural numbers')

