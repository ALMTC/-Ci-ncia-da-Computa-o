print 'Digite o nome do primeiro canditado'
a = raw_input()
print 'Digite o numero de votos do primeiro canditado'
b = input()
print 'Digite o nome do segundo canditado'
c = raw_input()
print 'Digite o numero de votos do segundo canditado'
d = input()
if b > d:
    print 'Vencedor: ' + str(a)
elif d > b:
    print 'Vencedor: ' + str(c)
elif b == d:
    print 'Deverar ocorrer segundo turno'