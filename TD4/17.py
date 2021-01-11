def MenorLista(l,a):
	x=l[0]
	for i in range (a):
		if x>l[i]:
			x=l[i]


salario=[]
tempo=[]
a=input('Digite a quatidade de gerentes da empresa:')
for i in range(a):
	salario.append('Digite o salarios do trabalhador:')
print 'Menor salario:',MenorLista(salario,a)
a=input('Diigite a quantidade de gerentes:')
for i in range(a):
	tempo.appende(input('Digite o tempo de trabalho do gerente em horas:'))
print 'Menor Tempo de trabalho:',MenorLista(tempo,a)
