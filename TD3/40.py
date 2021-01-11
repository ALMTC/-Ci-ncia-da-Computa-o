m=[]
soma=[]
print 'Digite o numero de linhas'
linha=input()
print 'Digite o numero de colunas'
coluna=input()
for i in range(linha):
    m.append([])
    for j in range(coluna):
        print 'Digite o elemento',i,j,'da matriz'
        m[i].append(input())
for j in range(coluna):
    soma.append([0])
    for i in range(linha):
        soma[j][0]=soma[j][0]+m[i][j]
for j in range(coluna):
    print 'Soma da coluna',i,':',soma[j]