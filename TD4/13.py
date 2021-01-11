def peso(altura,sexo):
	if sexo=='m' or sexo=='M':
		p=72.7*altura-58
	if sexo=='f' or sexo=='F':
		p=62.1*altura - 44.7
	return p
sexo=raw_input('Digite o sexo do paciente:M ou F:')
altura=input('Digite a altura do paciente em metros:')
massa=input('Digite o peso atual do paciente:')
print 'Peso ideal:',peso(altura,sexo)
if peso(altura,sexo)<massa:
	print 'Precisa perder',massa-peso(altura,sexo),'quilos para o peso ideal'
if peso(altura,sexo)>massa:
	print 'Precisa ganhar',peso(altura,sexo)-massa,'quilos para o peso ideal'
