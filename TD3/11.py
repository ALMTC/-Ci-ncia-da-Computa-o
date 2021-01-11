modelo=[]
consumo=[]
for i in range(5):
	print 'Digite o modelo do corro',i
	modelo.append(raw_input())
	print 'Digite o consumo em km/l do carro'
	consumo.append(input())
menorC=consumo[0]
for i in range(5):
	if consumo[i]>menorC:
		consumoM=modelo[i]
for j in range(5):
	consumo[j]=round(1000.0/consumo[j],3)
print 'Modelo mais economico:',consumoM
print 'Consumo de cada modelo respectivamente:',consumo
