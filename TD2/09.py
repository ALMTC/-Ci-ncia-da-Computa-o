porcentagem=1.5
salario=1000
print 'Salario no ano de: '
print '1995: 1000.0 R$'
print '1996: ',salario+(salario*1.5)/100.0
for i in range (1996, 2015):
   porcentagem=porcentagem*2
   acrescimo=(salario*porcentagem)/100
   print i,':',salario+acrescimo,'R$'
