print 'Numero de criancas mortas no periodo'
m = input()
continuar = 'true'
sexoM = 0
sexoF = 0
doisanos = 0
for i in range (1, m+1):
    print 'Sexo da crianca: M ou F'
    s = raw_input()
    if s=='M' or s=='m':
        sexoM = sexoM + 1
    if s=='F' or s=='f':
        sexoF = sexoF + 1
    print 'Tempo de vida em meses'
    t = input()
    if t<=24 and (s=='M' or s=='m' or s=='F' or s=='f'):
        doisanos = doisanos + 1
print 'porcentagem de criancas do sexo feminino mortas no periodo'
print sexoF * 100.0/m,'%'
print 'percentagem de criancas do sexo masculino mortas no periodo'
print sexoM * 100.0/m,'%'
print 'percentagem de criancas que viveram 24 meses ou menos'
print doisanos * 100.0/m,'%'

