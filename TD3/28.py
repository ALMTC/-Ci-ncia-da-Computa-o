matriz=[[],[],[]]
Soma=0
for i in range(3):
    for j in range(4):
        print 'Digite o elemente',i+1,j+1,'da matriz'
        matriz[i].append(input())
        Soma=Soma+matriz[i][j]
print 'Soma dos elementos da matriz:',Soma