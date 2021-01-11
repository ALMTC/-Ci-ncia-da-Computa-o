def menor(lista,tamanho):
	x=lista[0]
	for i in range(tamanho):
		if lista[i]<x:
			x=lista[i]
	return x
l=[]
a=input('Digite a quantidade de elementos da lista:')
for i in range(a):
	print 'Digite o elemento',i,'da lista'
	l.append(input())
print 'Menor elemento da lista:',menor(l,a)
