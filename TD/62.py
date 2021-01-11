print 'Tipo do carro: a ou b ou c'
a = raw_input()
print 'Percurso em Km:'
b = input()
if a == 'a':
    print 'Consumo de conbustivel: ' + str(b / 8.0) + 'L'
elif a == 'b':
    print 'Consumo de conbustivel: ' + str(b / 9.0) + 'L'
elif a == 'c':
    print 'Consumo de conbustivel: ' + str(b / 12.0) + 'L'