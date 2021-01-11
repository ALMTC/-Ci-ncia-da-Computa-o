print 'Digite a base do triangulo'
b=input()
print 'Digite a altura do triangulo'
h=input()
while b<0:
	print 'Digite a base do triangulo; numero maior que 0'
	b=input()
while h<0:
	print 'Digite a altura do triangulo; numero maior que 0'
	h=input()
print 'Area do triangulo: ', (b*h)/2	
