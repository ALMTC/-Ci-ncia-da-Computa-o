continuar='true'
while continuar=='true':
	print 'Digite o numero numero numero a ser feita a tabuada; Para sair digite (00)'
	a=input()
	if a==00:
		continuar='false'
	else:
		for i in range(0, 11):
			print a*i
