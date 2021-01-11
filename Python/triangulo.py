print 'Digite o valor 1'
a=input()
print 'Digite o valor 2'
b=input()
print 'Digite o valor 3'
c=input()
if a<b+c and b<a+c and c<a+b:
	if a==b and b==c and c==a:
		print 'Forma um triangulo Equilatero'
	if a!=b and	b!=c and c!=a:
		print 'Forma um triangulo Escaleno'
	if a==b!=c or a==c!=b or b==c!=a:
		print 'Forma um trangulo Isoceles'
else:
	print 'Nao e possivel formar um triangulo'
