# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,

# |     |  Х | 
# |     |  O |
# |     |  O |
# При ходе пользователя у надо спрашивать номер строки и столбца, куда он хочет сделать ход
#"""
from random import sample
import time

# field = [None, None, None,
#          None, None, None,
#          None, None, None]

# Пустые ячейки
field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Победные комбинации
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]

# "Рабочие" клавиши (какая клавиша обозначает ячейку поля)
def Standart(message = ''):
    temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    FieldInit(temp)
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
def Winner(win_arr, arr):
    message = ''
    for i in win_arr:
        if arr[i[0]] == 'X' and arr[i[1]] == 'X' and arr[i[2]] == 'X':
            message = 'победили крестики'
        elif arr[i[0]] == 'O' and arr[i[1]] == 'O' and arr[i[2]] == 'O':
            message = 'победили нолики'
    return message
    
# Выбор символа: крестик 'X' или нолик 'O' (выбор игрока)
def PickPlayer(message = ''):
    # try:
    pick: int = int(input())
    if pick == 1:
        symbol = 'X'
    elif pick == 0:
        symbol = 'O'
    return symbol
    # except:
    #     print('Ошибка: Вы нажали не ту кнопку')

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
    step = -1
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
                    step = line[j]                

    return step

# Выбор хода псевдоинтеллекта (под цифрами будут описаны приоритеты выполнения кода)
def ConditionAI(arr):
    select = [0, 1, 2, 3, 5, 6, 7, 8]

    # 1. Если наша линия победная - добиваем её
    step = AI(victory, arr, 2, 0)
    
    # 2. Если чужая линия победная - защищаем её
    if step == -1:
        step = AI(victory, arr, 0, 2)

    # 3. Если центр пуст - занимаем его
    if step == -1:
        if arr[4] == ' ':
            step = 4

    # 4. Если один символ наш и нет чужих на линии - добавляем ещё
    if step == -1:
        step = AI(victory, arr, 1, 0)

    # 5. Если центр занят, выбираем любую клетку (когда игрок 'X' и он занял центр)
    if step == -1:
        if arr[4] != ' ':
            step = int(*sample(select, 1))

    # 6. Исправление бага с заполнением псевдоинтеллектом последнего символа в игровом поле
    count = index = 0
    for i, el in enumerate(arr):
        if ' ' == el:
            count += 1
            index = i
    if count == 1:
        step = index

    return step

def Start(arr):
    end = False
    Standart(print('"Рабочие" клавиши:'))
    sym_player = PickPlayer(print('Нажмите 1, чтобы выбрать крестики или 0, чтобы выбрать нолики'))
    if sym_player == 'X':
        sym_ai = 'O'
        player = True
    elif sym_player == 'O':
        sym_ai = 'X'
        player = False
    while end == False:
        FieldInit(arr)
        
        if player == True:
            StepPlayer(arr, sym_player)
        else:
            print('Ход компьютера')
            step = ConditionAI(arr)
            time.sleep(1.5)

            if step != -1:
                arr[step] = sym_ai
                win = Winner(victory, arr)
                if win:
                    end = True
                else:
                    end = False
            else:           #срабатывает, когда компьютер - нолик 'O'
                win = 'ничья'
                end = True
        
        if ' ' not in arr:  #срабатывает, когда компьютер - крестик 'X'
            win = 'ничья'
            end = True

        player = not player

    FieldInit(arr)
    print(f'Игра окончена, {win}')

Start(field)
