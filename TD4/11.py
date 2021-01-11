def farotial(x):
    k = 1
    for i in range(1,x+1):
        k = k * i
    return k
def E(a):
    y=1
    for i in range (1,a+1):
        y=y+1/float(farotial(i))
    return y
b=input('Digite o numero natural a ser usado na expressao:')
print 'Resultado:',E(b)