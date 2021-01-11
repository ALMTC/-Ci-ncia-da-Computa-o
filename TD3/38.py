m=[]
soma=[]
print 'Digite o numero de linhas'
linha=input()
print 'Digite o numero de colunas'
coluna=input()
for i in range(linha):
    m.append([])
    soma.append([0])
    for j in range(coluna):
        print 'Digite o elemento',i,j,'da matriz'
        m[i].append(input())
        soma[i][0]=soma[i][0]+m[i][j]
for i in range(linha):
    print 'Soma da linha',i+1,':',soma[i]