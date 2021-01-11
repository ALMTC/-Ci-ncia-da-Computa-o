l=[]
a=input('Digite o tamanho da lista:')
for i in range (a):
	print 'Digite o valor',i,'da lista'
	l.append(input())
print 'Os valores impares sao:'
for i in range(a):
	if l[i]%2!=0:
		print 'Numero:',l[i],'Posicao:',i
