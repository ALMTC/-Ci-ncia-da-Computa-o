print 'Digite o falor de N'
n=input()
b=1
e=1
for i in range (0, n):
	print i
	b=b+b*i
	print b
	e=e+(1.0/b)
	print e
print 'e=', e
