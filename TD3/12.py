salarionovo=[]
FuncionarioAumento=[]
for i in range(3):
    print 'Digite o tempo de trabalho do funcionario', i
    tempo=input()
    print 'Digite o salario do funcionario', i
    salario=input()
    if tempo > 5 and salario < 1000:
        salarionovo.append(salario + (salario * 35 / 100.0))
        FuncionarioAumento.append(i)
    elif tempo > 5 or salario < 1000:
        salarionovo.append(salario + (salario * 10 / 100.0))
        FuncionarioAumento.append(i)
print 'Funcionarios que receberam aumento:',FuncionarioAumento
print 'Valor dos novos salarios respectivamente:',salarionovo