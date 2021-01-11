print 'Digite valor 1'
a=input()
print 'Digite valor 2'
c=input()
print 'Digite valor 3'
b=input()
print 'Em ordem crescente:'
if a<b and a<c:
	print a
if b<a and b<c:
	print b
if c<a and c<b:
	print c
if b<a<c or c<a<b:
	print a
if a<b<c or c<b<a:
	print b
if a<c<b or b<c<a:
	print c
if a>b and a>c:
	print a
if b>a and b>c:
	print b
if c>a and c>b:
	print c
