print 'Digite os dois numeros iniciais da sequencia'
a=input()
b=input()
print 'Quantidade de numeros da sequencia'
n=input()
print 'Sequencia:'
print '1:',a
print '2:',b
for i in range(3,n+1):
   c=a+b
   print str(i) + ':',c
   a=b
   b=c 
