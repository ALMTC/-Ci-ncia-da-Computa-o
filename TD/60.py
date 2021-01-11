print 'Nome'
n=raw_input()
print 'Idade'
a=input()
if a<=10:
    print str(n) + ': 30.00R$'
elif 10<a<=29:
    print str(n) + ': 60.00R$'
elif 29<a<=45:
    print str(n) + ': 120.00R$'
elif 45<a<=59:
    print str(n) + ': 150.00R$'
elif 59<a<=65:
    print str(n) + ': 250.00R$'
elif a>65:
    print str(n) + ': 400.00R$'