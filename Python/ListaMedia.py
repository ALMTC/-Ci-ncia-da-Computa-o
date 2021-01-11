medias = []
continuar = 'true'
k = 1
soma = 0
acimadamedia = 0
while continuar == 'true':
	print 'Digite as 2 notas do aluno',k
	a = input()
	b = input()
	medias.append((a+b)/2.0)
	soma = soma + medias[k-1]
	if medias[k-1] >= 7:
		acimadamedia = acimadamedia + 1
	print 'Para sair digite (s), para continuar (c)'
	c=raw_input()
	if c=='S' or c=='s':
		continuar='false'
	k=k+1
print 'Media da sala:', soma / float(k)
print 'Alunos acima da media:',acimadamedia
