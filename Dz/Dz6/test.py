from random import sample
#field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
field = ['X', 'O', 'X', 'X', 'O', ' ', 'O', 'X', 'O']
#field = [' ', ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ']

# Победные комбинации
victory = [[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8],
           [0, 3, 6],
           [1, 4, 7],
           [2, 5, 8],
           [0, 4, 8],
           [2, 4, 6]]


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
    
    count = index = 0
    for i, el in enumerate(arr):
        if ' ' == el:
            count += 1
            index = i
    if count == 1:
        step = index


    return step
    
print(ConditionAI(field))