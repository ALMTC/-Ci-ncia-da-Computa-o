m=[[],[],[]]
somalinha=[]
somacoluna=[]
for i in range(3):
    for j in range(3):
        print 'Digite o elemento',i,j,'da matriz'
        m[i].append(input())
    somalinha.append(m[i][0]+m[i][1]+m[i][2])
for i in range(3):
    somacoluna.append(m[0][j]+m[1][j]+m[2][j])
somaDP=m[0][0]+m[1][1]+m[2][2]
somaDS=m[0][2]+m[1][1]+m[2][0]
if somaDP==somaDS==somalinha[0]==somalinha[1]==somalinha[2]==somacoluna[0]==somacoluna[1]==somacoluna[2]:
    print 'E um quadrado magico'
else:
    print 'Nao e um quadrado magico'