from math import *
def hipotenusa(b,c):
	return sqrt(b**2+c**2)
for i in range(3):
	b=input('Digite o lado 1 do triangulo:')
	c=input('Digite o lado 2 do triangulo:')
	print 'Hipotenusa:',hipotenusa(b,c)
