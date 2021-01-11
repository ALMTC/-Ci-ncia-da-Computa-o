print 'Digite seu peso'
a = input()
print 'Digite sua altura em metros'
b = input()
imc = a / b ** 2.0
print 'imc: ' + str(imc)
if imc < 17:
    print 'Muito abaixo do peso'
elif 17 <= imc <= 18.49:
    print 'Abaixo do peso'
elif 18.49 <= imc <= 24.99:
    print 'Peso normal'
elif 25 <= imc <= 29.99:
    print 'Acima do peso'
elif 30 <= imc <= 34.99:
    print 'Obesidade I'
elif 35 <= imc <= 39.99:
    print 'Obesidade II (severa)'
elif imc >= 40:
    print 'Obesidade III (morbida)'