n=[]
total=0
acimaM=[]
for i in range(30):
	print 'Digite a nota do aluno',i+1
	n.append(input())
	total=total+n[i]
media=total/30.0
print 'Alunos acima da media:'
for i in range(30):
	if n[i]>media:
		acimaM.append(n[i])
print acimaM
