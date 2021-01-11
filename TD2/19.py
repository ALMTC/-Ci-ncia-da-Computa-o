print 'Valor da divida'
d = input()
print 'Numero de parcelas'
P = input()
sj = d / float(P)
total = 0
for i in range (1, P+1):
    parcela = sj + (sj * (2 * P)) / 100.0
    total = total + parcela
    print 'parcela ',i,':',parcela
print 'Valor total:',total
