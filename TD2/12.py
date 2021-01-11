maior=0
menor=1000
for i in range (1, 31):
	print 'digite a altura do aluno ', i, ' em centimetros'
	a=input()
	if maior<a:
		maior=a
		NumeroMaior=i
	if menor>a:
		menor=a
		NumeroMenor=i
print 'Maior aluno: numero ',NumeroMaior, maior, 'cm'
print 'Menor aluno: numero ',NumeroMenor, menor, 'cm'
