dicionario = {}
print 'Digite o nome do vendedor'
dicionario['nome']=raw_input()
print 'Digite o CPF do vendedor'
dicionario['CPF']=input()
print 'Digite o salario do vendedor'
dicionario['salario']=input()
print 'Digite o valor das vendas do vendedor'
dicionario['vendas']=input()
if dicionario['vendas']>10000:
	dicionario['gerente']='sim'
	dicionario['salario']=dicionario['salario']+(dicionario['salario']*10/100)
	print dicionario
else:
	dicionario['gerente']='nao'
	print dicionario
