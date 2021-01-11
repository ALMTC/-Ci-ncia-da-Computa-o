print 'Digite o valor da hora aula'
a=input()
print 'numero de aulas dadas no mes'
b=input()
print 'percentual de desconto do INSS'
c=input()
bruto=a*b
desconto=(bruto*c)/100.0
liquido=bruto-desconto
print 'Salario Bruto ' + str(bruto)
print 'Desconto ' + str(desconto)
print 'Salario Liquido ' + str(liquido)
