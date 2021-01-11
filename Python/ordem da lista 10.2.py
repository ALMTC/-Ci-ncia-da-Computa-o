l1 = []
print 'Digite a quantidade de elementos da lisata'
a=input()
for u in range(a):
    print 'Digite o elemento', u, 'da lista'
    l1.append(input())
for i in range (a):
	for j in range (a):
		if l1[i]<=l1[j]:
			aux=l1[i]
			l1[i]=l1[j]
			l1[j]=aux
print l1
