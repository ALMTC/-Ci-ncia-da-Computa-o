import math 
print 'Calcule ax^2+bx+c=0'
print 'Digite o valor de ax^2'
a = input()
print 'Digite o valor do bx'
b = input()
print 'Digite o valor de c'
c = input()
k = b ** 2 - 4 * a * c
x1 = (-b+math.sqrt(k))/(2.0*a)
x2 = (-b-math.sqrt(k))/(2.0*a)
if k < 0:
    print 'Nao possui raizes naturais'
if k == 0:
    print 'Possui apenas uma raiz'
    print x1
if k > 0:
    print 'Possui duas raizes'
    print x1
    print x2
