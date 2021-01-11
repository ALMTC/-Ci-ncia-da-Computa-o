def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)


valor=input('Digite o valor')
print fib(valor)
