# Валентина прогуляла лекцию по математике.
# Преподаватель решил подшутить над нерадивой студенткой и
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел.
# Для несложных примеров студентка быстро нашла решения
# (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось.
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232.

# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью.
# Помогите ей (при помощи функции all_divisors(number), которую напишете сами).
# Постарайтесь найти самое оптимальное решение.
# Результат представьте в виде списка (не забудьте отсортировать по возрастанию).

# Самым оптимальным решением будет перебрать делители до квадратного корня от искомого числа,
# найти делители перебором до квадратного корня, а все что остается после делаем поиск,
# разделив искомое число на найденный перебором делитель

num = int(input('Enter number: '))
sp = [1, num]

for i in range(2, 1 + int(num ** 0.5)):
    if num % i == 0:
        sp.extend([num // i, i])
print(sorted(sp))