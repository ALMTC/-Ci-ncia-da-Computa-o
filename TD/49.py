print 'Digite as 4 notas'
a = input()
b = input()
c = input()
d = input()
e = (a + b + c + d) / 4
print e
if e >= 5:
    print 'Aprovado'
elif e < 3:
    print 'Reprovado'
elif 3 <= e < 5:
    print 'Digite a nota da avaliacao final'
    f = input()
    if (e + f) / 2 >= 5:
        print 'Aprovado'
    else:
        print 'Reprovado'