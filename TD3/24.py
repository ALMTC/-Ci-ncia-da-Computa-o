l=[]
primos=[]
posicoes=[]
for i in range(5):
    print 'Digite o elemento',i
    l.append(input())
for i in range(5):
    primo='true'
    for k in range(2,l[i]):
        if l[i]%k==0:
            primo='false'
    if l[i]==1 or l[i]==0:
        primo='false'
    if primo=='true':
        primos.append(l[i])
        posicoes.append(i)
print 'Numeros primos:',primos
print 'Posicoes respectivamente:',posicoes