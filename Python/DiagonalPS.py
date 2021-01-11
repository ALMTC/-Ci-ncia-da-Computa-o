m1=[]
DiagonalP=[]
DiagonalS=[]
print 'Digite a quantidade de linhas da matriz'
linhas=input()
print 'Digite a quantidade de colunas da matriz'
colunas=input()
if linhas!=colunas:
	print 'Nao existe diagonal principal nem secundaria, pois nao e uma matriz quadratica'
else:
	for i in range (linhas):
		m1.append([])
		for j in range(colunas):
			print 'Digite o elemento',i,'x',j
			m1[i].append(input())
			if i==j:
				DiagonalP.append(m1[i][j])
for i in range (linhas):
	DiagonalS.append(m1[i][colunas-1-i])
print 'Doagonal principal:',DiagonalP
print 'Diagonal secundaria:',DiagonalS
print m1
