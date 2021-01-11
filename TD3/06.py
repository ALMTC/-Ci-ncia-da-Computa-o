lucro10=[]
lucro1030=[]
lucro30=[]
for i in range(5):
    print 'Digite o nome do produto'
    n=raw_input()
    print 'Digite o custo do produto'
    c=input()
    print 'Digite o preco do prodduto'
    p=input()
    lucro=p-c
    if lucro<(c*10/100.0):
        lucro10.append(n)
    elif (c*10/100.0)<=lucro<=(c*30/100.0):
        lucro1030.append(n)
    elif lucro>(c*30/100.0):
        lucro30.append(n)
print 'Lucro abaixo de 10%:',lucro10
print 'Lucro entre 10% e 30%:',lucro1030
print 'Lucro acima de 30%:',lucro30