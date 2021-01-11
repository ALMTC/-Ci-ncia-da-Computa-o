produtos = ['tipo1','tipo2','tipo3','tipo3','tipo4','tipo5']
precos = []
total = 0
ProdVendidos=0
tipo1=0
tipo2=0
tipo3=0
tipo4=0
tipo5=0
continuar='true'
for i in range (5):
	print 'Digite o valor do produto Tipo',i+1
	precos.append(input())
while continuar=='true':
	print 'digite o tipo do produto: tipo1,tipo2,tipo3,tipo4,tipo5'
	tipo=raw_input()
	print 'Digite a quantidade vendida do produto'
	qnt=input()
	ProdVendidos=ProdVendidos+qnt
	if tipo=='tipo1':
		total=total + precos[0]*float(qnt)
		tipo1=tipo1+qnt
	if tipo=='tipo2':
		total=total + precos[1]*float(qnt)
		tipo2=tipo2+qnt
	if tipo=='tipo3':
		total=total + precos[2]*float(qnt)
		tipo3=tipo3+qnt
	if tipo=='tipo4':
		total=total + precos[3]*float(qnt)
		tipo4=tipo4+qnt
	if tipo=='tipo5':
		total=total + precos[4]*float(qnt)
		tipo5=tipo5+qnt
	print 'Para terminar digite (n), para entrar com outra compra digite (s)'
	sair=raw_input()
	if sair=='n' or sair=='N':
		continuar='false'
print 'Total de produtos vendidos:',ProdVendidos
print 'Vendas do produto:'
print 'tipo1:',tipo1
print 'tipo2:',tipo2
print 'tipo3:',tipo3
print 'tipo4:',tipo4
print 'tipo5:',tipo5
print 'Total vendido:',total,'R$'
