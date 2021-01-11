m1=[[],[],[]]
m2=[[],[],[]]
for i in range(3):
    for j in range(3):
        print 'Digite o elemento',i,j,'da matriz 1'
        m1[i].append(input())
for i in range(3):
    for j in range(3):
        print 'Digite o elemento',i,j,'da matriz 2'
        m2[i].append(input())
for i in range(3):
    for j in range(3):
        m1[i][j]=m1[i][j]*m2[i][j]
print 'O produto das duas matrizes:'
print m1[0]
print m1[1]
print m1[2]
