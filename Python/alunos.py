print 'Digite a a quantidade de alunos'
x = input()
k = 1
while k <= x:
    k = k + 1
    print 'Digite a primeira nota'
    a = input()
    print 'Digite a segunda nota'
    b = input()
    c = (a + b) / 2.0
    print 'Media final: ', c
    if  c < 3:
        print 'Reprovado'
    else:
        if  3 <= c < 7:
            print 'Avaliacao Final'
        else: 
            print 'Aprovado'
