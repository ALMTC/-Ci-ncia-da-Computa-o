print 'Codigo do produto'
a = input()
if a == 1:
    print 'Alimento nao-perecivel'
elif 2 <= a <= 4:
    print 'Alimento perecivel'
elif a == 5 or a == 6:
    print 'Vestuario'
elif a == 7:
    print 'Higiene pessoal'
elif 8 <= a <= 15:
    print 'Limpeza e utensilios domesticos'
else:
    print 'Invalido'