print 'Digite os 5 numeros'
a = input()
b = input()
c = input()
d = input()
e = input()
print 'Maior valor: '
if a > b and a > c and a > d and a > e:
    print a
elif b > a and b > c and b > d and b > e:
    print b
elif c > a and c > b and c > d and c > e:
    print c
elif d > a and d > b and d > c and d > e:
    print d
elif e > a and e > b and e > c and e > d:
    print e
print 'Menor valor: '
if a < b and a < c and a < d and a < e:
    print a
elif b < a and b < c and b < d and b < e:
    print b
elif c < a and c < b and c < d and c < e:
    print c
elif d < a and d < b and d < c and d < e:
    print d
elif a < e and e < b and e < c and e < d:
    print e
