aprovado=0
recuperacao=0
reprovado=0
notasala=0
print 'informe o numero de alunos da sala'
alunos=input()
for i in range (1, alunos+1):
   print 'Digite as notas do aluno ',i
   n1=input()
   n2=input()
   nf=(n1+n2)/2.0
   notasala=notasala+nf
   if nf>=7:
      aprovado=aprovado + 1
   if 3<=nf<7:
      recuperacao=recuperacao + 1
   if nf<3:
      reprovado=reprovado + 1
print 'Aprovados:',aprovado
print 'Recuperacao:',recuperacao
print 'Reprovados:',reprovado 
print 'Media da sala:',notasala/alunos
