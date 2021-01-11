print 'Entre com o codigo do Prato: Vegetariano(p1); Peixe(p2); Frango(p3); Carne(p4)'
a = raw_input()
print 'Entre com o codigo da Sobremesa: Abacaxi(s1); Sorvetediet(s2); Moussediet(s3); Moussechocolate(s4)'
b = raw_input()
print 'Entre com o codigo da Bebida: Cha(b1); Sucodelaranja(b2); Sucodemelao(b3); Refrigeranteb(b4)'
c = raw_input()
if a == a:
    if a == 'p1':
        a = 180
    elif a == 'p2':
        a = 230
    elif a == 'p3':
        a = 250
    elif a == 'p4':
        a = 350
    else:
        print 'O nome do prato esta errado'
if b == b:
    if b == 's1':
        b = 75
    elif b == 's2':
        b = 110
    elif b == 's3':
        b = 170
    elif b == 's4':
        b = 200
    else:
        print 'O nome da sobremesa esta errado'
if c == c:
    if c == 'b1':
        c = 20
    if c == 'b2':
        c = 70
    if c == 'b3' or c == 'b4':
        c = 100
    else:
        print 'O nome da bebida esta errado'
print 'Total de calorias: ' + str(a+b+c) + 'cal'