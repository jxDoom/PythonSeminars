# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Пример входа:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15

# Выход будет:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6
from random import randint

teams = ['Chelsea', 'Man City', 'Arsenal', 'Man United', 'Barcelona']#,
         #'Real Madrid', 'Liverpool', 'Bayern', 'PSJ', 'Newcastle']
#[Games, Result, Points]    #Result: return 0 0 0

def GenerateMatch(team):
    for i in range(len(team)):
        index = i - len(team)
        index1 = index2 = index
        team1 = team[index1]
        while index2 < i - 1:
            team2 = team[index2]
            index2 += 1
            left = randint(0, 5)
            right = randint(0, 5)
            print(f'{team[index1]} {left} : {right} {team[index2]}')

# def Games(team):
#     count = 0
#     if 
GenerateMatch(teams)

# for i in range(len(team)):
#     index1 = i - len(team)
#     team1 = team[index1]
#     index2 = i - len(team) + 1
#     team2 = team[index2]
#     print(f'{team[index1]} {randint(0, 5)} : {randint(0, 5)} {team[index2]}')