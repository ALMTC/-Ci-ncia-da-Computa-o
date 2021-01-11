sGerente = []
sFuncionario = []
nsGerente = []
nsFuncionario = []
gastoatual = 0
gastonovo = 0
gerentemaisqmedianovo = 0
gerentemaisqmediaatual = 0
print 'digite a quantidade de gerente(s)'
g = input()
for i in range(g):
    print 'Digite o salario do gerente', i + 1
    sGerente.append(input())
    gastoatual = gastoatual + sGerente[i]
    nsGerente.append(sGerente[i] + (sGerente[i] * 10 / 100))
    gastonovo = gastonovo + nsGerente[i]
print 'Digite a quantidade de funcionarios nao gerentes'
f = input()
for u in range(f):
    print 'Digite o salario do funcionario', u + 1
    sFuncionario.append(input())
    gastoatual = gastoatual + sFuncionario[u]
    nsFuncionario.append(sFuncionario[u] + sFuncionario[u] * 5 / 100)
    gastonovo = gastonovo + nsGerente[u]
print 'Gasto altual:', gastoatual
print 'Novo gasto:', gastonovo
for i in range(g):
    if sGerente[i] > gastoatual / float(g + f):
        gerentemaisqmediaatual = gerentemaisqmediaatual + 1
    if nsGerente[i] > gastonovo / float(g + f):
        gerentemaisqmedianovo = gerentemaisqmedianovo + 1
print 'Gerentes com salario maior que a media atual:', gerentemaisqmediaatual
print 'Gerentes com salario maior que a media nova:', gerentemaisqmedianovo
