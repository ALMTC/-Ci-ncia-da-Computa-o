k = 0
j = 's'
m = 0
while j == 's':
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
    print 'Existe mais algum aluno? se sim, digite (s), se n digite (n)'
    j = raw_input()  
    m = m + c
    k = k + 1
print 'Media da turma: ' + str(m / k)
