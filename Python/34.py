def arquivoExiste(nomeArquivo):
    try:
        f = open(nomeArquivo, 'r')
        f.close()
        return True

    except:
        return False


def PegardoArquivo(arquivo, lista):
    f = open(arquivo, 'r')

    while True:
        a = f.readline()
        if a == '':
            break
        lista.append(int(a))

    f.close()

    return lista


def ColocarnoArquivo(arquivo, lista, qtd):
    f = open(arquivo, 'w')

    for i in range(qtd):
        f.write(str(lista[i]) + '\n')

    f.close()


codigo = []
nome = []
qtdvendas = []
preco = []
qtd = 0
if arquivoExiste('codigo.txt'):
    f = open('nome.txt', 'r')
    qtd = 0
    while True:
        a = f.readline()
        if a == '':
            break
        nome.append(a[:-1])
        qtd = qtd + 1
    f.close()
    PegardoArquivo('codigo.txt', codigo)
    PegardoArquivo('qtdvendas.txt', qtdvendas)
    PegardoArquivo('preco.txt', preco)

while True:
    print('Digite o numero da opcao desejada:')
    print('1 - Cadastrar produto')
    print('2 - Deletar produto')
    print('3 - Buscar produto pelo codigo')
    print('4 - Visualizar todas as informacoes de todos os produtos')
    print '5 - Mostrar todas as informacoes do(s) produto(s) com maior quantidade de vendas'
    print '6 - Mostrar todas as informacoes do(s) produto(s) com menor quantidade de vendas'
    print '7 - Calcular a soma da quantidade de vendas, a media da quantidade de vendas e a quantidade de produtos cadastrados'
    print '8 - Aumentar preco de um produto'
    print '9 - Diminuir preco de um produto'
    print '10 - Sair do programa'
    a = input()

    if a == 1:
        if qtd == 20:
            print 'numero maximo de produtos atingidos'
        b = input('Digite o codigo do produto:')
        if b in codigo:
            print 'Esse codigo ja existe. codigos ja existentes:', codigo
            b = input('Digite um codigo que ainda nao esteja na lista')
        codigo.append(b)
        nome.append(raw_input('Digite o nome do produto:'))
        qtdvendas.append(input('Digite a quantidade de produtos vendidos:'))
        preco.append(input('Digite o preco do produto:'))
        qtd = qtd + 1

    if a == 2:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            b = input('Digite o codigo do produto a ser deletado:')
            deletado=False
            for i in range(qtd):
                if b == codigo[i]:
                    deletado=i
            if deletado==False:
            	print 'Codigo nao existente'
            else:
		         codigo = codigo[0:deletado] + codigo[deletado + 1:qtd + 1]
		         nome = nome[0:deletado] + nome[deletado + 1:qtd + 1]
		         qtdvendas = qtdvendas[0:deletado] + qtdvendas[deletado + 1:qtd + 1]
		         preco = preco[0:deletado] + preco[deletado + 1:qtd + 1]
		         qtd = qtd - 1  

    if a == 3:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            b = input('Digite o codigo do produto a ser feito a busca:')
            for i in range(qtd):
                if b == codigo[i]:
                    c = i
            print 'Codigo:', codigo[c], '; Nome:', nome[c], '; Quantidade de vendas:', qtdvendas[c], '; Valor:', preco[
                c], 'R$'

    if a == 4:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            print 'Informacoes dos produtos:'
            for c in range(qtd):
                print 'Codigo:', codigo[c], '; Nome:', nome[c], '; Quantidade de vendas:', qtdvendas[c], '; Valor:', \
                    preco[c], 'R$'

    if a == 5:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            print 'Produto(s) com maior quantidade de vendas.'
            k = qtdvendas[0]
            for i in range(qtd):
                if k < qtdvendas[i]:
                    k = qtdvendas[i]
            for c in range(qtd):
                if k == qtdvendas[c]:
                    print 'Codigo:', codigo[c], '; Nome:', nome[c], '; Quantidade de vendas:', qtdvendas[c], '; Valor:', \
                        preco[c], 'R$'

    if a == 6:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            print 'Produto(s) com menor quantidade de vendas.'
            k = qtdvendas[0]
            for i in range(qtd):
                if k > qtdvendas[i]:
                    k = qtdvendas[i]
            for c in range(qtd):
                if k == qtdvendas[c]:
                    print 'Codigo:', codigo[c], '; Nome:', nome[c], '; Quantidade de vendas:', qtdvendas[c], '; Valor:', \
                        preco[c], 'R$'
    if a == 7:
        k = 0
        for i in range(qtd):
            k = k + qtdvendas[i]
        print 'Quantidade de produtos cadastrados:', qtd
        print 'Soma da quantidade de vendas:', k
        print 'Media da quantidade de vendas:', k / float(qtd)

    if a == 8 or a == 9:
        if codigo == []:
            print 'ainda nao possui produtos cadastrados'
        else:
            b = input('Digite o Codigo do produto a ter o preco alterado:')
            for i in range(qtd):
                if b == codigo[i]:
                    print 'Valor atual o produto:', preco[i], 'R$'
                    preco[i] = input('Digite o novo valor do produto:')
    if a == 10:
        ColocarnoArquivo('codigo.txt', codigo, qtd)
        ColocarnoArquivo('qtdvendas.txt', qtdvendas, qtd)
        ColocarnoArquivo('preco.txt', preco, qtd)
        ColocarnoArquivo('nome.txt', nome, qtd)
        break
