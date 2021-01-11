print 'Digite os dois valores a serem tirados o MMC'
a = input()
b = input()
k=1.0
continuar = 'true'
while continuar=='true':
    if k%a==0 and k%b==0:
        continuar = 'false'
    else:
        k=k+1
print 'MMC=',k
