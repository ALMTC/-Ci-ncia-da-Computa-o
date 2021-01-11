funcionario=[]
gerente=[]
print 'Digite a quantidade de funcionarios:'
f=input()
print 'Digote a quantidade de gerentes:'
g=input()
for i in range (f):
	print 'Digite o salario do funcionario',i
	funcionario.append(input())
for i in range(g):
	print 'Digite as horas de trabalho do gerente',i
	gerente.append(input())
men=funcionario[0]
min=gerente[0]
for i in range (f):
	if funcionario[i]<men:
		men=funcionario[i]
for i in range (g):
	if gerente[i]<min:
		min=gerente[i]
print 'Menor salario:',men,'R$'
print 'Menor quantidade de horas trabalhadas pelos gerentes:',min,'h'
