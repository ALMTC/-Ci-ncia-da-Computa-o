def media(x1, x2, x3):
    if x3 == 'a' or x3 == 'A':
        resultado = (x1 + x2) / 2.0
    if x3 == 'p' or x3 == 'P':
        resultado = ((x1 * 2) + (x2 * 3)) / 5.0
    return resultado
for i in range(20):
    print 'Digite a primeira nota'
    a = input()
    print 'Digite a segunda nota'
    b = input()
    print 'Digite o tipo de media: Aritimetica(A) ou Ponderada(P)'
    c = raw_input()
    d = media(a, b, c)
    print d
