def modulo(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    return x
a=input('Digite o KM da cidade 1:')
b=input('Digite o KM da cidade 2:')
print 'Distancia entre as cidades:',modulo(a-b)