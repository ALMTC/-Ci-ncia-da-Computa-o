print 'Digite o salario'
a = input()
if a <= 600:
    print 'insento de ddesconto: ' + str(a)
elif 600 < a <= 1200:
    print 'Desconto de 20%: ' + str(a-a*20/100.0)
elif 1200 < a <= 2000:
    print 'Desconto de 25%: ' + str(a-a*25/100.0)
elif a > 2000:
    print 'Desconto de 30%: ' + str(a-a*30/100.0)