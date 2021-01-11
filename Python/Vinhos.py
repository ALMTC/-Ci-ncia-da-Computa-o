a = 'n'
t = 0
b = 0
r = 0
while a != 's':
    print 'Digite qual o Vinho: (T) (B) (R) Para sair digite (S)'
    x=raw_input()
    if x == 'T' or x == 't':
    	t = t + 1
    elif x == 'B' or x == 'b':
    	b = b + 1
    elif x == 'R' or x == 'r':
    	r = r + 1
    else:
    	a='s'
w = (t * 100.0) / (t + b + r)
e = (b * 100.0) / (t + b + r)
s = (r * 100.0) / (t + b + r)
print 'Porcentagem dos vinhos: Tinto=',w,'% Branco=',e,'% Rose=',s,'%'
