def primo(x1):
    x='true'
    for j in range (2,x1):
        if x1%float(j)==0:
            x='false'
    if x=='false':
        return 0
    else:
        return 1
print 'Digite o numero limite da  verificacao dos primos'
a=input()
print 'Os primos sao:'
for i in range(2,a+1):
    b=primo(i)
    if b==1:
        print i
