print 'Digite o numero inteiro maior que 1'
a = input()
primo='sim'
for i in range (2, a):
    d=a%i
    if d==0:
        primo='nao'
if primo=='nao':
    print 'Nao e um numero primo'
else:
    print 'E um numero primo'
