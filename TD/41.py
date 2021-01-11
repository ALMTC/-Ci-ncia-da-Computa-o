print 'Digite o valor do salario'
a = input()
if a < 500:
    print 'Reajuste de 15%: ' + str(a + a * 15 / 100.0)
elif 500 <= a <= 1000:
    print 'Reajuste de 10%: ' + str(a + a * 10 / 100.0)
elif a > 1000:
    print 'Reajuste de 5%: ' + str(a + a * 5 / 100.0)