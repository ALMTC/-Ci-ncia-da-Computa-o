def Fat(n):
	if n==0:
		return 1
	return n*Fat(n-1)
	
n=input('Digite o Valor de n:')
print Fat(n)
