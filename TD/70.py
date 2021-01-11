print 'Nome do produto'
a = raw_input()
print 'Valor do produto'
b = input()
if b < 10:
    print 'Produto: ' + str(a)
    print 'Valor de venda: ' + str(b + b * 70 / 100.0) + 'R$'
elif 10 <= b < 30:
    print 'Produto: ' + str(a)
    print 'Valor de venda: ' + str(b + b * 50 / 100.0) + 'R$'
elif 30 <= b < 50:
    print 'Produto: ' + str(a)
    print 'Valor de venda: ' + str(b + b * 40 / 100.0) + 'R$'
elif b > 50:
    print 'Produto: ' + str(a)
    print 'Valor de venda: ' + str(b + b * 30 / 100.0) + 'R$'