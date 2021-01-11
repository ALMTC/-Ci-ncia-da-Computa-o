print 'Digite sua idade'
a = input()
if a < 16:
    print 'Nao-eleitor'
elif 18 <= a <= 65:
    print 'Eleitor obrigatorio'
elif 16 < a < 18 or a > 65:
    print 'Eleitor facutativo'
