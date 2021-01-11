m=[[],[],[]]
for linha in range (3):
	print 'Digite os elementos da linha',linha
	for coluna in range(2):
		m[linha].append(input())
print 'Digite o numero real'
r=input()
for linha in range (3):
	for coluna in range(2):
		m[linha][coluna]=m[linha][coluna]*r
print m[0]
print m[1]
print m[2]
