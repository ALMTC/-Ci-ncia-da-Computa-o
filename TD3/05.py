n=[]
menor=[]
maior=[]
total=0
for i in range(5):
	print 'Digite a nota do aluno',i
	n.append(input())
	total=total+n[i]
media=(total/50.0)*10/100
for i in range(5):
	if n[i]>media:
		maior.append(n[i])
	elif n[i]<media:
		menor.append(n[i])
print 'notas acima:',maior
print 'notas abaixo:',menor
