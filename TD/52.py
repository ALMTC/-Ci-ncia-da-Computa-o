print 'Digite sua altura'
h = input()
print 'Digite seu sexo: M ou F'
b = raw_input()
print 'Peso ideal'
if b == 'M':
    print (72.7 * h) - 58
else:
    print (62.1 * h) - 44.7