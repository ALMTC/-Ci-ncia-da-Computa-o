print 'Digite a quantidade de traabalhadores'
trab = input()
total = 0.0
for i in range(1, trab+1) :
	print 'Digite as vendas do trabalhador ', i
	venda = input()
	total = total + venda
print 'Total de vendas da loja: ', total,'R$'
print 'Media de venda dos vendedores: ', total / trab,'R$'
