print 'Digite o primeiro numero'
a = input()
print 'digite o segundo numero'
b = input()
print 'Digite o terceiro numero'
c = input()
print 'Maior valor:'
if a > b and a > c:
    print a
elif b > c and b > a:
    print b
elif c > a and c > b:
    print c
elif a == b > c or a == c > b:
    print a
elif b == c > a:
    print b
elif a == b == c:
    print a