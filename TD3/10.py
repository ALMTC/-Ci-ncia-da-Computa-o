vendido = []
valor = []
QtdDeProdVendidos = 0
ValorTotal = 0
for i in range(10):
    print 'Digite a quantidade de produtos vendidos do tipo', i
    vendido.append(input())
    print 'Digite o valor da unidade do produto', i
    valor.append(input())
for i in range(10):
    valor[i] = valor[i] * vendido[i]
    QtdDeProdVendidos = QtdDeProdVendidos + vendido[i]
    ValorTotal = ValorTotal + valor[i]
print 'Itens vendidos por tipo de produto:',vendido
print 'Valor das vendas por produto:',valor
print 'Quantidade total de itens vendidos:',QtdDeProdVendidos
print 'Valor total das vendas:',ValorTotal