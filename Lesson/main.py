# print(5)
# n = None    #пустое значение, ставим тогда, когда знаем что нужна будет переменная, но не знаем какого она будет значения
# n = 1.23
# n = 'abcd'
# print(n)
"""
#n = 'ab\'cd'
n ='ab"cdef"gh'
print(n)
print(type(n))

a = 5
b = 1.234
c = 'hello'
print(a,b,c)
print(a,' - ',b,' - ',c)
print(f"{a} - {b} - {c}")   #шаблон f-строки
print("{} - {} - {}".format(a,b,c))    #шаблон-функция format
print(a,b,c,sep = ' - ')    #separator
"""

# print('Введите первую строку: ')
# a = input()
# print(a)

# a = input('Введите первое число: ')
"""
c = 3.64
print(c)
print(type(c))
c = str(c)
print(c + '64')
print(type(c))

c = 1
print(c)
print(type(c))
c = bool(c)
print(c)
print(type(c))
"""

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(f'{a} + {b} = {a+b}')

# a = 1.236845
# b = 5.43201
# print(round(a*b, 3))
"""
i = 0
while i < 5:
    if i == 3:
        break
    i = i + 1
else:
    print('Пожалуй')
    print('хватит)')
print(i)

n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0:   #если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2:    #делить числа не может превышать введеное число, деленное на 2
        print(n)
        flag = False
    i += 1
"""
# a = 'qwerty'
# #print(a[2])
# for i in a:
#     print(i)
"""
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)
"""
# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))
# print('ещё' in text)
# print(text.lower())   #все буквы текста в нижнем регистре
# print(text.upper())   #все буквы текста в верхнем регистре
# print(text.replace('ещё', 'ЕЩЁ'))
# print(text[0])
# print(text[1])
# print(text[len(text)-1])  #к
# print(text[-5])   #б
# print(text[:])  #СъЕШЬ ещё этих МяГкИх французских булок
# print(text[:2])   #Съ
# print(text[len(text)-2:])   #ок
# print(text[2:9])   #ЕШЬ ещё
# print(text[6:-18])  #ещё этих МяГкИх
# print(text[0:len(text):6])  #Сеикакл
# print(text[::6])    #Сеикакл

# text = text[2:9] + text[-5] + text[:2]
# print(text)   #ЕШЬ ещёбСъ