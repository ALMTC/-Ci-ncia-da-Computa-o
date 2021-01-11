print 'Digite o valor do salario'
a = input()
print 'Digite o valor da prestacao'
b = input()
c = a - a * 70 / 100
if b <= c:
    print 'O emprestimo pode ser concedido'
else:
    print 'O emprestimo nao pode ser concedido'