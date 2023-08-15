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
#"""
# Выбор символа: крестик 'X' или нолик 'O' (выбирает игрок)
def PickSymbol(message = ''):
    try:
        pick: int = int(input())
        if pick == 1:
            symbol = 'X'
        elif pick == 0:
            symbol = 'O'
        return symbol
    except:
        print('Ошибка: Вы нажали не ту кнопку')

#"""
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

# # Ход псевдоинтеллекта
# def StepAI(arr):
#     step = ''
#     step = AI(field, sym1, sym2)

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
#"""
#Standart(print('"Рабочие" клавиши:'))
#FieldInit(field)
#Winner(victory)
#print(PickSymbol(print('Нажмите 1, чтобы выбрать крестики или 0, чтобы выбрать нолики')))
#print(StepPlayer(field, PickSymbol(print('Нажмите 1, чтобы выбрать крестики или 0, чтобы выбрать нолики'))))
#AI(victory, field,,)


# def Ranking(arr):
#     for i in arr:










# # Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# # Инициализация победных линий
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])
     
# # Сделать ход в ячейку
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# # Получить текущий результат игры
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# #Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
# def check_line(sum_O,sum_X):
 
#     step = ""
#     for line in victories:
#         o = 0
#         x = 0
 
#         for j in range(0,3):
#             if maps[line[j]] == "O":
#                 o = o + 1
#             if maps[line[j]] == "X":
#                 x = x + 1
 
#         if o == sum_O and x == sum_X:
#             for j in range(0,3):
#                 if maps[line[j]] != "O" and maps[line[j]] != "X":
#                     step = maps[line[j]]
                 
#     return step
 
# #Искусственный интеллект: выбор хода
# def AI():        
 
#     step = ""
 
#     # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
#     step = check_line(2,0)
 
#     # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
#     if step == "":
#         step = check_line(0,2)        
 
#     # 3) если 1 фигура своя и 0 чужих - ставим
#     if step == "":
#         step = check_line(1,0)           
 
#     # 4) центр пуст, то занимаем центр
#     if step == "":
#         if maps[4] != "X" and maps[4] != "O":
#             step = 5           
 
#     # 5) если центр занят, то занимаем первую ячейку
#     if step == "":
#         if maps[0] != "X" and maps[0] != "O":
#             step = 1           
   
#     return step
 
# # Основная программа
# game_over = False
# human = True
 
# while game_over == False:
 
#     # 1. Показываем карту
#     print_maps()
 
#     # 2. Спросим у играющего куда делать ход
#     if human == True:
#         symbol = "X"
#         step = int(input("Человек, ваш ход: "))
#     else:
#         print("Компьютер делает ход: ")
#         symbol = "O"
#         step = AI()
 
#     # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
#     if step != "":
#         step_maps(step,symbol) # делаем ход в указанную ячейку
#         win = get_result() # определим победителя
#         if win != "":
#             game_over = True
#         else:
#             game_over = False
#     else:
#         print("Ничья!")
#         game_over = True
#         win = "дружба"
 
#     human = not(human)        
 
# # Игра окончена. Покажем карту. Объявим победителя.        
# print_maps()
# print("Победил", win)