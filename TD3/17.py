l = []
a = input('Digite a quantidade de elementos da lista:')
for i in range(a):
    print 'Digite o elemento', i, 'da lista'
    l.append(input())
e = input('Digite o elemento a ser verificado:')
for i in range(a):
    if l[i]==e:
        e='ACHADO'
if e=='ACHADO':
    print 'ACHADO'
else:
    print "NAO ACHADO"