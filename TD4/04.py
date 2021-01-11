def verifica(a,b,c):
    k=0
    for i in range(b+1,c):
        if i%a==0:
            k=k+i
    return k
for i in range(10):
    a=input('Digite o valor de a:')
    if a<=1:
        a=input('Digite o valor de a(a deve ser maior que 1):')
    b=input('Digite o valor de b:')
    c=input('Digite o valor de c:')
    print verifica(a,b,c)