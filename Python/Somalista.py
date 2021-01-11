l1=[]
SomaLista = 0
for i in range(10):
	print 'Digite o valor',i+1,'da lista'
	l1.append(input())
	SomaLista = SomaLista + l1[i]
print 'soma da lista:', SomaLista
