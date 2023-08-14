# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,

# |     |  Х | 
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход

from random import randint

# field = [None, None, None,
#          None, None, None,
#          None, None, None]

# "Рабочие" клавиши (какая клавиша обозначает ячейку поля)
def Standart(message = ''):
    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    FieldInit(sample)
    print()

# Визуалиация игрового поля
def FieldInit(arr):    
    print(arr[0], end = '|')
    print(arr[1], end = '|')
    print(arr[2])
        
    print(arr[3], end = '|')
    print(arr[4], end = '|')
    print(arr[5])
        
    print(arr[6], end = '|')
    print(arr[7], end = '|')
    print(arr[8])

# Поиск победителя после каждого хода
def Winner(win_arr):
    message = ''
    for i in win_arr:
        if win_arr[i[0]] == 'X' and win_arr[i[1]] == 'X' and win_arr[i[2]] == 'X':
            message = 'Победили крестики'
        elif win_arr[i[0]] == 'O' and win_arr[i[1]] == 'O' and win_arr[i[2]] == 'O':
            message = 'Победили нолики'
    return message

# Ход игрока
def StepPlayer(arr, symbol):
    tmp = int(input('Ваш ход: ')) - 1
    if arr[tmp] != 'X' and arr[tmp] != 'O':
        arr[tmp] = symbol
    else:    
        print('Эта клетка занята, выберите другую клетку')
        StepPlayer(arr, symbol)
    return arr

# Псевдоинтеллект: поиск победных линий
def AI(win_arr, arr, sum_x, sum_o):
    step = ''
    for line in win_arr:
        count_x = count_o = 0

        for i in range(3):
            if arr[line[i]] == 'X':
                count_x += 1
            elif arr[line[i]] == 'O':
                count_o += 1

        if count_x == sum_x and count_o == sum_o:
            for j in range(3):
                if arr[line[j]] == ' ':
                    step = arr[line[j]]
    return step

# Ход псевдоинтеллекта
def StepAI(arr):
    step = ''
    step = AI(field, sym1, sym2)

# Пустые ячейки
field = ['O', ' ', ' ', 'X', ' ', 'O', ' ', ' ', ' ']

# Победные комбинации
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]

#Standart(print('"Рабочие" клавиши:'))
#FieldInit(field)
#Winner(victory)
#print(StepPlayer(field, 'X'))
#AI(victory, field,,)


# def Ranking(arr):
#     for i in arr:



