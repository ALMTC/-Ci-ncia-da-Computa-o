print 'Digite os dois valores a serem tirados o MDC'
a = input()
b = input()
continuar = 'true'
while continuar == 'true':
    c = a % b
    if c==0:
        continuar = 'false'
    else:
        a=b
        b=c
print 'MDC=', b
