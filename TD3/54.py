m1=[[],[]]
m2=[[],[]]
TotalMes=[]
TotalAutoFalante=0
TotalTeclas=0
print 'Digite a quantidade de auto-falantes dos modelos A B C respectivamente'
for i in range(3):
    m1[0].append(input())
print 'Digite a quantidade de teclas dos modelos A B C respectivamente'
for i in range(3):
    m1[1].append(input())
for i in range(2):
    print 'Quantidade de TVs do tipo A B C no mes',i+1,'respectivamente:'
    for j in range(3):
        m2[i].append(input())
for j in range(3):
    qtdtotal=0
    for i in range(2):
        qtdtotal=qtdtotal+m2[i][j]
    TotalMes.append(qtdtotal)
for i in range(2):
    for j in range(3):
        m1[i][j]=m1[i][j]*TotalMes[j]
    for i in range(3):
        TotalAutoFalante=TotalAutoFalante+m1[0][i]
        TotalTeclas=TotalTeclas+m1[1][i]
print 'Total de auto falantes:',TotalAutoFalante
print 'Total de teclas:',TotalTeclas
