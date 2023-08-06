# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def ArithProg(first_num, diff, count):    #Первый элемент, разность и кол-во элементов соответственно
#     sp = [first_num + (i - 1) * diff for i in range(1, count + 1)]
#     return sp

def Start():
    ArithProg = lambda first_num, diff, count: [first_num + (i - 1) * diff for i in range(1, count + 1)]
    a1: int = int(input('Введите первый элемент арифметической прогрессии: '))
    d: int = int(input('Разность элементов: '))
    n: int = int(input('Количество элементов: '))
    if d > 0 and n > 1:
        print(ArithProg(a1, d, n))
    else:
        print(0)
    
Start()
