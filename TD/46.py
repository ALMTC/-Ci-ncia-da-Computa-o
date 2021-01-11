print 'Digite o nome do primeiro canditado'
n1 = raw_input()
print 'Digite o numero de votos do primeiro canditado'
a = input()
print 'Digite o nome do segundo canditado'
n2 = raw_input()
print 'Digite o numero de votos do segundo canditado'
b = input()
print 'Digite o nome do terceiro canditado'
n3 = raw_input()
print 'Digite o numero de votos do terceiro canditado'
c = input()
d = a + b + c
e = d / 2
if a >= e:
    print 'Vencedor: ' + str(n1)
elif b >= e:
    print 'Vencedor: ' + str(n2)
elif c >= e:
    print 'Vencedor: ' + str(n3)
elif a < e and b < e and c < e:
    print 'Devera ter um segundo turno com os 2 mais votados'