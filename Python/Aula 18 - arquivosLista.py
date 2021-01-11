def arquivoExiste(nomeArquivo):
  try:
    f = open(nomeArquivo, 'r')
    f.close()
    return True
  except:
    return False


lista = []
if(arquivoExiste('lista.txt')):
  f = open('lista.txt', 'r')
  qtd = 0
  while True:
    elemento = f.readline()
    if elemento == '':
      break
    lista.append(int(elemento))
    qtd = qtd + 1

  f.close()
  for i in range(qtd):
    print lista[i]

else:
  f = open('lista.txt', 'w')
  qtd = input('digite a quantidade de elementos: ')
  lista = []
  for i in range(qtd):
    print 'digite o elemento', i, 'da lista: '
    lista.append(input())

  for i in range(qtd):
    f.write(str(lista[i])+'\n')

  f.close()
  
