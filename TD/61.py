print 'Nome do livro'
a = raw_input()
print 'Aluno ou Professor'
b = raw_input()
if b == 'Aluno' or b == 'Professor':
    print 'Recibo:'
    print 'Nome do livro: ' + str(a)
    print 'Tipo de usuario: ' + str(b)
    if b == 'Aluno':
        print 'Total de dias: 3'
    else:
        print 'Total de dias: 10'
else:
    print 'Opcao invalida'