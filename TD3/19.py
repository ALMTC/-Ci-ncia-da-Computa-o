l = []
total = 0
k = 0
a = input('Digite a quantidade de funcionarios:')
maior = 0
for i in range(a):
    l.append(input('Digite o salario do funcionario:'))
    total = total + l[i]
    if l[i] > maior:
        maior = l[i]
media = total / float(a)
for i in range(a):
    if l[i] < media:
        k = k + 1
print 'Maior salario:', maior
print 'Gasto da empresa com os salarios:', total
print 'Media dos salarios:', round(media,2)
print 'Quantidade de funcionarios com salario menor que a media:', k