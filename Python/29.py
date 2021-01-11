print 'Digite a altura do cilindro em metros'
a=input()
print 'Digite  o raio de cilindro em metros'
r=input()
ab=3.14*r**2
al=2*3.14*r*a
at=ab+al
lt=at/15
p=lt*50.00
print 'Total de latas gastas: ' + str(lt)
print 'Custo total: ' + str(p)
