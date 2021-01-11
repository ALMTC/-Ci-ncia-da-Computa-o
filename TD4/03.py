def somatoria(x1,x2):
    k=0
    for i in range(x1+1,x2):
        k=k+i
    return k
for i in range(2):
    a=input('Digite o primeiro valor :')
    b=input('Digite o segundo valor:')
    print 'Soma dos inteiros entre os valores:',somatoria(a,b)