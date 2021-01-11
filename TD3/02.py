l1=[]
l2=[]
for i in range(20):
    print 'Digite a posicao',i+1,'do vetor 1'
    l1.append(input())
for i in range(20):
    print 'Digite a posicao',i+1,'do vetor 2'
    l2.append(input())
for i in range(20):
    l1[i]=l1[i]+l2[i]
print 'Soma das posicoes dos vetores:',l1