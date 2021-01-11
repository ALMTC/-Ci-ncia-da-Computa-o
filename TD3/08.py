alturas = []
somaaltura = 0
repeticao = 0
for i in range(50):
    print 'Digite a altura', i + 1
    alturas.append(input())
    somaaltura = somaaltura + alturas[i]
print 'Media das alturas:', somaaltura / 50.0
for i in range(50):
    a = alturas.count(alturas[i])
    if repeticao < a:
        repeticao = a
        maiorRepeticao = alturas[i]
print 'Numero com maior repeticao:', maiorRepeticao
print 'Repete', repeticao, 'vezes'