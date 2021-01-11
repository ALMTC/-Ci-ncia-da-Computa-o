salario = []
SalarioTotal = 0
maior = 0
menor = 0
print 'Digite a quantidade de funcionarios da empresa. Maximo 100'
n = input()
for i in range(n):
    print 'Digite o salario do funcionario', i + 1
    salario.append(input())
    SalarioTotal = SalarioTotal + salario[i]
SalarioMeido = SalarioTotal / float(n)
salario10 = SalarioMeido + SalarioMeido * 10 / 100.0
for i in range(n):
    if salario[i] > salario10:
        maior = maior + 1
    elif salario[i] < salario10:
        menor = menor + 1
print 'Salario maior que a media mais 10%:',maior
print 'Salario menor que a media mais 10%:',menor