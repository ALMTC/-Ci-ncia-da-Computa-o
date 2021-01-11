def potencia(a,b):
	resultado=1
	for i in range(b):
		resultado=resultado*a
	return resultado
juros=input('Digite os juros')
valordep=input('Digite o valor do deposito')
vfin=valordep*potencia(1+juros, tempo)
