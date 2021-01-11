QtdVendida=[]
Valor=[]
QtdTotal=0
for i in range(3):
    print 'Digite a quantidade de produtos vendidos polo vendedor',i+1
    QtdVendida.append(input())
    print 'Digite o valor da unidade do produto do vendendor',i+1
    Valor.append(input()*QtdVendida[i])
    QtdTotal=QtdTotal+QtdVendida[i]
print 'Quantidade de pecas vendidas:',QtdTotal
print 'Valor total da venda de cada vendedor respectivamente:',Valor