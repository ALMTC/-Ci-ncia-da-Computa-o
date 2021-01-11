print 'Valor do produlto'
a = input()
print 'Condicao de pagamento: 1, 2, 3 ou 4 '
b = input()
if b == 1:
    print 'Valor final: ' + str(a - a * 10 / 100.0) + 'R$'
elif b == 2:
    print 'Valor final: ' + str(a - a * 5 / 100.0) + 'R$'
elif b == 3:
    print str(a) + 'R$'
elif b == 4:
    print 'Valor final: ' + str(a + a * 10 / 100.0) + 'R$'
else:
    print 'Opcao invalida'