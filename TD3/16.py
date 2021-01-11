l = []
print 'Digite a quantidade de elementos da lista'
a = input()
if a > 100:
    print 'Numero maximo de elementos: 100'
else:
    for i in range(a):
        print 'Digite o elemento', i
        l.append(input())
for i in range(a / 2):
    b = l[i]
    l[i] = l[a - 1 - i]
    l[a - 1 - i] = b
print 'Ordem inversa da lista', l