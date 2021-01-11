l=[]
p=[]
n=[]
for i in range(8):
	print 'Digite o elemento',i,'da linta'
	l.append(input())
for i in range(8):
	if l[i]>=0:
		p.append(l[i])
	else:
		n.append(l[i])
print 'Posotivos:',p
print 'Negativos:',n
