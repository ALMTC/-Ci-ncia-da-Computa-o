arquivo=open('/home/alunos/dados','w')
arquivo.write('5')
arquivo.write('6\n')
arquivo.write('7\n')
arquivo.close()
arquivo=open('/home/alunos/dados','r')
s=arquivo.read()
arquivo.close()
print s
