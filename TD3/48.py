l=[]
QtdTotal=[]
VendasVendedor=[]
print 'Digite a quantidade de vendedores'
vendedor=input()
print 'Digite a quantidade de produtos'
prod=input()
for i in range(vendedor):
    l.append([])
    for j in range(prod):
        print 'Digite a qunatidade de produtos do tipo',j,'vendidos pelo vendedor',i
        l[i].append(input())
for j in range(prod):
    qtdtotal=0
    for i in range(vendedor):
        a=l[i][j]
        qtdtotal=qtdtotal+a
    QtdTotal.append(qtdtotal)
for i in range(vendedor):
    qtdtotal=0
    for j in range(prod):
        qtdtotal=qtdtotal+l[i][j]
    VendasVendedor.append(qtdtotal)
qtdtotal=0
for i in range(vendedor):
    qtdtotal=qtdtotal+VendasVendedor[i]
print 'Quantidade de produtos vendidos por tipo respectivamente:',QtdTotal
print 'Quantidade de produtos vendidos por vendedor respectivamente:',VendasVendedor
print 'Total de produtos vendidos:',qtdtotal