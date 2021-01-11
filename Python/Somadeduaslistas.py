l1=[]
l2=[]
l3=[]
for i in range(10):
	print 'Digie o valor',i+1,'da lista 1'
	l1.append(input())
	print 'Digie o valor',i+1,'da lista 2'
	l2.append(input())
	l3.append(l1[i]+l2[i])
print 'soma das duas listas',l3
