m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
continuar = 'true'
while continuar == 'true':
    print m[0]
    print m[1]
    print m[2]
    print 'digite a primeira jogada. Jogador 1=x; Jogador 2=o'
    a = raw_input()
    print 'digite a linha'
    l = input()
    print 'digite a coluna'
    c = input()
    m[l][c] = a
    if m[0] == ['x', 'x', 'x']:
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[1] == ['x', 'x', 'x']:
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[2] == ['x', 'x', 'x']:
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0][0] == 'x' and m[1][0] == 'x' and m[2][0] == 'x':
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0][1] == 'x' and m[1][1] == 'x' and m[2][1] == 'x':
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0][2] == 'x' and m[1][2] == 'x' and m[2][2] == 'x':
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0][0] == 'x' and m[1][1] == 'x' and m[2][2] == 'x':
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0][2] == 'x' and m[1][1] == 'x' and m[2][0] == 'x':
        print 'jogador 1 vencedor'
        continuar = 'false'
    if m[0] == ['o', 'o', 'o']:
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[1] == ['o', 'o', 'o']:
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[2] == ['o', 'o', 'o']:
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[0][0] == 'o' and m[1][0] == 'o' and m[2][0] == 'o':
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[0][1] == 'o' and m[1][1] == 'o' and m[2][1] == 'o':
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[0][2] == 'o' and m[1][2] == 'o' and m[2][2] == 'o':
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[0][0] == 'o' and m[1][1] == 'o' and m[2][2] == 'o':
        print 'jogador 2 vencedor'
        continuar = 'false'
    if m[0][2] == 'o' and m[1][1] == 'o' and m[2][0] == 'o':
        print 'jogador 2 vencedor'
        continuar = 'false'