print 'Digite a velocidade media'
v=input()
print 'Digite o tempo de viagem em horas'
t=input()
print 'Digite a quantidade de quilometros por litro'
q=input()
s=v*t
c=s/q
print 'O veiculo percorreu ' + str(s) + 'km e gastou ' + str(c) + ' litros de conbustivel'