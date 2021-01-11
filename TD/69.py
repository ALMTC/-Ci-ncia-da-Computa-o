print 'Destino da vaigem: NorteNordeste(n); Sudeste(d); CentroOeste(c); Sul(s)'
a = raw_input()
print 'Ida(1) ou Ida e volta(2)'
b = input()
c = a + str(b)
if c == 'n1':
    print 'Valor da viagem: 500R$'
elif c == 'n2':
    print 'Valor da viagem: 900R$'
elif c == 'd1':
    print 'Valor da viagem: 350R$'
elif c == 'd2':
    print 'Valor da viagem: 650R$'
elif c == 's1':
    print 'Valor da viagem: 300R$'
elif c == 's2':
    print 'Valor da viagem: 550R$'
