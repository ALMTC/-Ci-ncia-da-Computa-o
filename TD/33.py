print 'Digite os 4 valores'
a = input()
b = input()
c = input()
d = input()
print 'Em ordem crescente'
if a < b and a < c and a < d:
    print a
if b < a and b < c and b < d:
    print b
if c < a and c < b and c < d:
    print c
if d < a and d < b and d < c:
    print d
if b < a < c < d or b < a < d < c or c < a < b < d or c < a < d < b or d < a < b < c or d < a < c < b:
    print a
if a < b < c < d or a < b < d < c or c < b < a < d or c < b < d < a or d < b < a < c or d < b < c < a:
    print b
if a < c < b < d or a < c < d < b or b < c < a < d or b < c < d < a or d < c < a < b or d < c < b < a:
    print c
if a < d < b < c or a < d < c < b or b < d < a < c or b < d < c < a or c < d < a < b or c < d < b < a:
    print d
if b > a > c > d or b > a > d > c or c > a > b > d or c > a > d > b or d > a > b > c or d > a > c > b:
    print a
if a > b > c > d or a > b > d > c or c > b > a > d or c > b > d > a or d > b > a > c or d > b > c > a:
    print b
if a > c > b > d or a > c > d > b or b > c > a > d or b > c > d > a or d > c > a > b or d > c > b > a:
    print c
if a > d > b > c or a > d > c > b or b > d > a > c or b > d > c > a or c > d > a > b or c > d > b > a:
    print d
if a > b and a > c and a > d:
    print a
if b > a and b > c and b > d:
    print b
if c > a and c > b and c > d:
    print c
if d > a and d > b and d > c:
    print d
