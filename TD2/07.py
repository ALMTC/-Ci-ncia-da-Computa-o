otimo = 0
bom = 0
regular = 0
ruim = 0
pessimo = 0
idadepessimo = 0
idadeotimo = 0
idaderuim = 0
k = 1
while k <= 5:
    print 'Digite sua idade'
    a = input()
    print 'Digite a sua nota: Bom; Otimo; Regular; Ruim; Pessimo;'
    b = raw_input()
    if b == 'otimo' or b == 'Otimo':
        otimo = otimo + 1
        if idadeotimo < a:
            idadeotimo = a
    if b == 'bom' or b == 'Bom':
        bom = bom + 1
    if b == 'regular' or b == 'Regular':
        regular = regular + 1
    if b == 'ruim' or b == 'Ruim':
        ruim = ruim + 1
        if idaderuim < a:
            idaderuim = a
    if b == 'pessimo' or b == 'Pessimo':
        pessimo = pessimo + 1
        if idadepessimo < a:
            idadepessimo = a
    k = k + 1
print 'Quantidade de Otimos: ', otimo
print 'Diferenca percentual entre Bom e Regular', ((bom * 100.0) / k) - ((regular * 100.0) / k), '%'
print 'Media de pessoas que votaram ruim de cada 100: ', ruim
print 'Percentagem de respostas Pessimo: ', (ruim * 100.0) / k
print 'Maior idade que respondeu Pessimo: ', idadepessimo
print 'Diferencca de idade entre a maior que respondeu Otimo e a maior que respondeu Ruim: ',
if idadeotimo < idaderuim:
    print idaderuim - idadeotimo
elif idadeotimo > idaderuim:
    print idadeotimo - idaderuim
else:
    print '0'