matriz=[]
soma=0
print 'Digite a quantiade de linhas da matriz'
linhas=input()
print 'Digite a quantidade de colunas da matriz'
colunas=input()
for i in range(linhas):
    matriz.append([])
    for j in range(colunas):
        print 'Digite o elemento',i+1,j+1,'da matriz'
        matriz[i].append(input())
        if matriz[i][j]%2!=0:
            soma=soma+matriz[i][j]
print 'Soma dos elementos impares da matriz:',soma