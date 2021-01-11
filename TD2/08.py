continuar = 'true'
H1835 = 0
Mverdeloiro = 0
total = 1
MaiorIdade = 0
while continuar == 'true':
    print 'Digite o seu sexo: M ou F'
    sexo = input()
    print 'Digite a cor dos olhos: A, V ou C'
    olho = input()
    print 'Digite a cor do cabelo: L, C, P ou P'
    cabelo = input()
    print 'Digite a sua idade'
    idade = input()
    print 'Se quiser sair, digite -1, para continuar aperte outra tecla'
    sair = input()
    tatal = total + 1
    if sexo == 'h' or sexo == 'H' and 18 <= idade <= 35:
        H1835 = H1835 + 1
    if sexo == 'm' or sexo == 'M' and olho == 'v' or olho == 'V' and cabelo == 'l' or cabelo == 'L':
        Mverdeloiro = Mverdeloiro + 1
    if idade > MaiorIdade:
        MaiorIdade = idade
    if sair == '-1':
        continuar = 'false'
print 'Maior Idade: ', MaiorIdade
print 'Pessoas de sexo masculino que tem idade entre 18 e 35: ', (H1835 * 100) / total
print 'Mulheres com olhos verdes e cabelos loiros: ', (Mverdeloiro * 100) / total