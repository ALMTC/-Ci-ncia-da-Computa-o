idadetime1 = 0
idadetime2 = 0
idadetime3 = 0
idadetime4 = 0
idadetime5 = 0
idademenor18 = 0
alturat = 0
pesot = 0
peso80 = 0
for i in range (1, 56):
    print 'Digite a Idade do jogador',i
    idade = input()
    if idade<18:
        idademenor18 = idademenor18 + 1
    if 1<=i<=11:
        idadetime1 = idadetime1 + idade
    if 12<=i<=22:
        idadetime2 = idadetime2 + idade
    if 23<=i<=33:
        idadetime3 = idadetime3 + idade
    if 34<=i<=44:
        idadetime4 = idadetime4 + idade
    if 45<=i<=55:
        idadetime5 = idadetime5 + idade
    print 'Digite a altura do jogador',i
    altura = input()
    alturat = alturat + altura
    print 'Digite o peso do jogador',i
    peso = input()
    pesot = pesot + peso
    if peso > 80:
        peso80 = peso80 + 1

print 'Jogadores com menos de 18 anos:',idademenor18
print 'Media de idade dos jogadores de cada time:'
print 'Time 1:',idadetime1/11
print 'Time 2:',idadetime2/11
print 'Time 3:',idadetime3/11
print 'Time 4:',idadetime4/11
print 'Time 5:',idadetime5/11
print 'Media das alturas de todos os jogadores do campeonato:', alturat/55.0
print 'Porcentagem de jogadores com mais de 80 Kg entre todos os jogadores do campeonato:',(peso80*100)/pesot
