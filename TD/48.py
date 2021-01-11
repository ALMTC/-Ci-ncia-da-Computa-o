print 'Digite o primeiro numero:'
a = input()
print 'Digite o segundo numero:'
b = input()
print 'Digite a operacao: + - * /'
c = raw_input()
if c == '+':
    print a + b
elif c == '-':
    print a - b
elif c == '*':
    print a * b
elif c == '/':
    print a / (b + 0.0)