JV=[['v','v','v'],['v','v','v'],['v','v','v']]
for i in range (9):
	print JV[0]
	print JV[1]
	print JV[2]
	print 'digite a primeira jogada. Jogador 1=x; Jogador 2=o'
	a=raw_input()
	print 'digite a linha'
	l=input()
	print 'digite a coluna'
	c=input()
	if a=='x' or a=='X':
		JV[l][c]='x'
	elif a=='o' or a=='O':
		JV[l][c]='o'
