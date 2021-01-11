continuar = 'true'
c1 = 0
c2 = 0
c3 = 0
c4 = 0
branco = 0
nulo = 0
while continuar == 'true':
    print 'Digite o numero do seu candidato: 1,2,3,4; Para voto em branco: 5; Para voto nulo: 6; Sair:0'
    a = input()
    if a == 1:
        c1 = c1 + 1
    if a == 2:
        c2 = c2 + 1
    if a == 3:
        c3 = c3 + 1
    if a == 4:
        c4 = c4 + 1
    if a == 5:
        branco = branco + 1
    if a == 6:
        nulo = nulo + 1
    if a == 0:
        continuar = 'false'
t = c1 + c2 + c3 + c4 + nulo + branco
print 'candidato 1 Votos: ', c1, (c1 * 100.0) / t, '%'
print 'candidato 2 Votos: ', c2, (c2 * 100.0) / t, '%'
print 'candidato 3 Votos: ', c3, (c3 * 100.0) / t, '%'
print 'candidato 4 Votos: ', c4, (c4 * 100.0) / t, '%'
print 'Em Branco Votos: ', branco, (branco * 100.0) / t, '%'
print 'Nulos Votos: ', nulo, (nulo * 100.0) / t, '%'