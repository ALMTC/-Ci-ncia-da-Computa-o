print 'Digite o numero a ser adivinhado'
n = input()
t = 1
print 'Chute'
c = input() 
if c < n:
   print 'E menor q o numero'
if c > n:
   print 'E maior q o numero'
while c != n:
   print 'Chute'
   c = input()
   t = t + 1
   if c < n:
      print 'E menor q o numero'
   if c > n:
      print 'E maior q o numero'
if c == n:
   print 'Acertou em: ', t, 'tentativas'
