def retorno(x):
    if x%2==0:
        a=1
    else:
        a=0
    return a
for i in range(4):
    x=input('Digite o falor a ser verificado:')
    if retorno(x)==1:
        print 'Par'
    if retorno(x)==0:
        print 'Impar'