print 'Digite o primeiro numero'
a = input()
print 'Digite o segundo numero'
b = input()
if a > b:
    print 'Valor da diferenca: ' + str(a - b)
elif b > a:
    print 'Valor da diferenca: ' + str(b - a)
elif a == b:
    print 'Valor da diferenca: 0'