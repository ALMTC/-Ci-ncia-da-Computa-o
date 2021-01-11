l1=[0,1]
print 'Digite a qunatidade de valores da lista'
a=input()
for i in range (2,a):
	if i%2==0:
		l1.append(0)
	else:
		l1.append(1)
print l1
