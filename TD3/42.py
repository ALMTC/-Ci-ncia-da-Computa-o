m1=[]
m2=[]
m3=[]
print 'Digite a quantidade de linhas e colunas da primeira matriz respectivamente'
linha=input()
coluna=input()
print 'Digite a quantidade de linhas e colunas da primeira matriz respectivamente'
linha1=input()
coluna1=input()
if coluna!=coluna1 or linha!=linha1:
    print 'As duas matrizes devem ter o mesmo numero de colunas'
else:
    for i in range(linha):
        m1.append([])
        for j in range(coluna):
            print 'Digite o elemento',i,j,'da matriz 1'
            m1[i].append(input())
    for i in range(linha):
        m2.append([])
        for j in range(coluna):
            print 'Digite o elemento',i,j,'da matriz 2'
            m2[i].append(input())
    for i in range(linha):
        for j in range(coluna):
            m1[i][j]=m1[i][j]+m2[i][j]
    print 'Soma das matrizes:'
    for i in range(linha):
        print m1[i]