nome=[]
preco=[]
for i in range(5):
    print 'Digite o nome do produto',i+1
    nome.append(raw_input())
    print 'Digite o valor do produto',i+1
    preco.append(input())
k=0
for i in range(5):
    if preco[i]<50:
        k=k+1
print 'Quantidade de produtos com valor inferior a 50R$:',k
print 'Nome dos produtos com preco entre 50 e 100 R$:'
k=0
total=0
for i in range(5):
    if 50<preco[i]<100:
        print nome[i]
    if preco[i]>100:
        total=total+preco[i]
        k=k+1
print 'Media dos precos dos produtos com preco superior a 100R$:',total/float(k)