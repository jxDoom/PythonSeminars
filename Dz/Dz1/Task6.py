# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

num = input('Enter ticket number (6 digits): ')
sum1 = sum2 = 0

try:
    tmp = int(num)
    
    if len(num) != 6:
        print('Error: This ticket does not exist! Enter again.')
    else:
        for i in range(3):
            sum1 += int(num[i])

        for i in range(3,len(num)):
            sum2 += int(num[i])

        print(f'The sum of the first three: {sum1} \t The sum of the second three: {sum2}')

        if sum1 == sum2:
            print('Hooray! Happy ticket!')
        else:
            print('Better luck next time :(')
except:
    print('Error. Enter only numbers.')
