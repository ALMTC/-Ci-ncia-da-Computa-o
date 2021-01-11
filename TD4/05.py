def tempo(x):
    return x/3600.0
k=0
for i in range(10):
    print'Digite o tempo gasto(em segundos) na terefa',i
    k=k+input()
print 'Tempo em horas:',tempo(k)