l=[]
PosicoesdoMenor=[]
print 'Digite a quantidade de elementos da lista. Maximo 20'
n=input()
for i in range(n):
    print 'Digite o elemento',i
    l.append(input())
    menor=l[0]
for i in range(1,n):
    if menor>l[i]:
        menor=l[i]
for i in range(n):
    if menor==l[i]:
        PosicoesdoMenor.append(i)
print 'Menor numero:',menor
print 'Se repete nas posicoes:',PosicoesdoMenor