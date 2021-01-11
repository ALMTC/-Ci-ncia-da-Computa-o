l=[]
QtdTotal=[]
ValorProd=[]
ValorTotalVendedor=[]
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
for i in range(prod):
    print 'Digite o valor do produto',i
    ValorProd.append(input())
for j in range(prod):
    qtdtotal=0
    for i in range(vendedor):
        qtdtotal=qtdtotal+l[i][j]
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
max=VendasVendedor[0]
for i in range (prod):
    if VendasVendedor[i]>max:
        max=i
print 'Vendedor com mais vendas: Vendedor',max
a=max(QtdTotal)
max=QtdTotal[0]
for i in range(vendedor):
    if QtdTotal[i]>max:
    	max=i
print 'Produto mais vendido: Tipo',max
for i in range(vendedor):
    for j in range(prod):
        l[i][j]=l[i][j]*ValorProd[i]
for j in range(prod):
    qtdtotal=0
    for i in range(vendedor):
        qtdtotal=qtdtotal+l[i][j]
    ValorTotalVendedor.append(qtdtotal)
print 'Valor das vendas de cada vendedor respectivamente:',ValorTotalVendedor
a=max(ValorTotalVendedor)
max=ValorTotalVendedor[i]
for i in range(prod):
    if ValorTotalVendedor[i]>max:
    	max=i
print 'Vendendor com maior valor de reais em vendas: Vendedor',i
qtdtotal=0
for i in range(prod):
    qtdtotal=qtdtotal+ValorTotalVendedor[i]
print 'Valor total de reais da loja:',qtdtotal
