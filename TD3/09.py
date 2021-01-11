l=[]
for i in range(10):
	print 'Digite o elemento',i,'do vetor'
	l.append(input())
	max=l[0]
print 'Os valores impares sao:'
for i in range(10):
	if l[i]%2!=0:
		print l[i]
