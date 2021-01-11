arquivo=open('/home/alunos/dados','w')
arquivo.write('5\n')
arquivo.write('6\n')
arquivo.close()
arquivo=open('/home/alunos/dados','r')
s1=arquivo.readline()
s2=arquivo.readline()
print s1
print s2
arquivo.close()
