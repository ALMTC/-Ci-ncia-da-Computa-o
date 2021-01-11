l=[]
c=[]
MinimoLinha=[]
MaximoLinha=[]
MinimoColuna=[]
MaximoColuna=[]
print 'Digite a qunatidade de linhas da matriz'
linha=input()
print 'Digite a quantidade de colunas da matriz'
coluna=input()
for i in range(linha):
	l.append([])
	for j in range(coluna):
		print 'Digite o eleento',i,j,'da matriz'
		l[i].append(input())
for i in range(linha):
	menor=l[i][0]
	maior=l[i][0]
	for j in range(1,coluna):
		if menor>l[i][j]:
			menor=l[i][j]
		if maior<l[i][j]:
			maior=l[i][j]
	MinimoLinha.append(menor)
	MaximoLinha.append(maior)
for i in range(coluna):
	c.append([])
	for j in range(linha):
		c[i].append(l[j][i])
for i in range(coluna):
	menor=c[i][0]
	maior=c[i][0]
	for j in range(linha):
		if menor>c[i][j]:
			menor=c[i][j]
		if maior<c[i][j]:
			maior=c[i][j]
	MinimoColuna.append(menor)
	MaximoColuna.append(maior)
print 'Matriz original:'
for i in range(linha):
	print l[i]
for i in range(linha):
	print 'Maior elemeto da linha',i,':',MaximoLinha[i]
for i in range(linha):
	print 'Menor elemeto da linha',i,':',MinimoLinha[i]
for i in range(coluna):
	print 'Maior elemeto da coluna',i,':',MaximoColuna[i]
for i in range(coluna):
	print 'Menor elemeto da coluna',i,':',MinimoColuna[i]
