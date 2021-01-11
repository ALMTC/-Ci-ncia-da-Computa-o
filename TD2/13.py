veiculot=0
acidentemaior = 0
acidentemenor = 10000000
acidmenor2000 = 0
cidademenor2000 = 0
for i in range (1, 6):
    print 'Codigo da cidade'
    cod = raw_input()
    print 'Numero de veiculos de passeio:'
    veipass = input()
    veiculot = veiculot + veipass
    print 'Numero de acidentes de transito com vitimas:'
    acid = input()
    if acidentemaior < acid:
        acidentemaior = acid
        cidademaior = cod
    if acidentemenor > acid:
        acidentemenor = acid
        cidademenor = cod
    if veipass < 2000:
        acidmenor2000 = acidmenor2000 + acid
        cidademenor2000 = cidademenor2000 +1
print 'Maior e menor indice de acidentes de transito e a que cidades pertencem:'
print 'Maior', acidentemaior, 'Codigo da cidade:', cidademaior
print 'Menor', acidentemenor, 'Codigo da cidade:', cidademenor
print 'Media de veiculos nas cinco cidades juntas:', veiculot/5
print 'Media de acidentes nas cidades com menos de 2000 veiculos de passeio:', acidmenor2000 / float(cidademenor2000)
