notas=[]
NotaTotal=0
AcimadaMedia=0
NaMedia=0
AbaixodaMedia=0
print 'Digite a quantidade de alunos da tuma. Maximo 70'
n=input()
for i in range(n):
    print 'Digite a nota do aluno',i+1
    notas.append(input())
    NotaTotal=NotaTotal+notas[i]
    if notas[i]>7:
        AcimadaMedia=AcimadaMedia+1
    elif notas[i]==7:
        NaMedia=NaMedia+1
    elif notas[i]<7:
        AbaixodaMedia=AbaixodaMedia+1
print 'Media da sala:',NotaTotal/float(n)
print 'Acima da Media:',AcimadaMedia
print 'Na Media:',NaMedia
print 'Abaixo da Media:', AbaixodaMedia