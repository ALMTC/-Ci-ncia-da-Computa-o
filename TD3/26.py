n=[]
QtdNotaMenor=0
QtdNotaMaior=0
print 'Digite a quantidade de alunos'
a=input()
for i in range(a):
    print 'Digite a nota do aluno',i+1
    n.append(input())
    NotaMaior=n[0]
    NotaMenor=n[0]
for i in range(a):
    if n[i]<NotaMenor:
        NotaMenor=n[i]
    if n[i]>NotaMaior:
        NotaMaior=n[i]
QtdNotaMaior=n.count(NotaMaior)
QtdNotaMenor=n.count(NotaMenor)
print 'Maior nota:',NotaMaior,'Quantidade de alunos que tiraram a maior nota:',QtdNotaMaior
print 'Menor nota:',NotaMenor,'Quantidade de alunos que tiraram a menor nota:',QtdNotaMenor