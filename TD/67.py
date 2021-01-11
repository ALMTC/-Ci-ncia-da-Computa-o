print 'Saldo medio do ultimo ano'
a=input()
if a<=500:
    print 'Nao recebera credito especial'
elif 500<a<=1000:
    print 'Saldo medio: ' + str(a) + 'R$'
    print 'Credito: ' + str(a-a*70/100.0) + 'R$'
elif 1000<a<=3000:
    print 'Saldo medio: ' + str(a) + 'R$'
    print 'Credito: ' + str(a-a*60/100.0) + 'R$'
elif a>3000:
    print 'Saldo medio: ' + str(a) + 'R$'
    print 'Credito: ' + str(a-a*50/100.0) + 'R$'