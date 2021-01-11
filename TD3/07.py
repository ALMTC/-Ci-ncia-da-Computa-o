l=[]
l2=[]
for i in range (5):
	print 'Digite o valor',i,'da lista'
	l.append(input())
for i in range (4,-1,-1):
	l2.append(l[i])
print l2
