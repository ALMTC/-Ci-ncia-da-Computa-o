print 'Digite a quantidade de numeros a serem somados'
x = input()
k = 1
b = 0.0
while k <= x:
    print 'Digite o numero par a ser somado'
    a = input()
    k = k + 1
    b = b + a
print 'A media dos numeres: ', (b / x)
