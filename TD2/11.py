for i in range (1, 6):
    print 'Digite os dois numeros inteiros possitivos'
    a = input()
    b = input()
    if a%2==0 or b%2==0:
        print 'Numeros pares no par de numeros',i
        if a%2==0:
            print a
        if b%2==0:
            print b
