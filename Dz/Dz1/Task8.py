# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

n = int(input('Proportion of chocolate - length: '))
m = int(input('Proportion of chocolate - width: '))
k = int(input('Proportion of chocolate - after partition: '))

if k<n*m and k%n == 0 or k%m == 0:
    print('Yes, it is possible')
else:
    print('No it can\'t be done')
