m=[[],[],[],[]]
for i in range(4):
    for j in range(7):
        print 'Digite o elemento',i,j,'da matriz'
        m[i].append(input())
        menor=m[0][0]
        maior=m[0][0]
for i in range(4):
    for j in range(7):
        if menor>m[i][j]:
            menor=m[i][j]
            linha=i
for i in range(7):
    if maior<m[linha][i]:
        maior=m[linha][i]
print 'Maior elemento da linha onde esta o menor elemento da matriz:',maior