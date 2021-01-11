l1=[]
for i in range(30):
    print 'Diigite o valor',i,'do vetor'
    l1.append(input())
for i in range(0,30,2):
    l1[i]=l1[i]*2
for i in range(1,30,2):
    l1[i]=l1[i]*3
print l1