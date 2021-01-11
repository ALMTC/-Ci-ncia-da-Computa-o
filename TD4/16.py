import math 
def valor(x):
	if x<=180:
		return 4
	else:
		return 4+math.ceil((x-180)/60.0)


k=0
total=0
for i in range(input('Digite a quantidade de clientes:')):
	a=input('Digite o tempo que o cliente utilizou o estacionamento em minutos:')
	print 'Valor a pagar:', valor(a),'R$'
	k=k+valor(a)
print 'Volor total arrecadado:',k,'R$'
