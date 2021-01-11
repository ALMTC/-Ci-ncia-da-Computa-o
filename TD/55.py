print 'Entre com seu nome'
a = raw_input()
print 'Estado civil: c, s, d, v'
b = raw_input()
if b == 'c':
    print 'Casado'
elif b == 's':
    print 'Solteiro'
elif b == 'd':
    print 'Divorciado'
elif b == 'v':
    print 'Viuvo'
else:
    print 'Opcao invalida'