def media(a,b,c):
	total=0
	k=0
	for i in range(a):
		if l[i]['olhos']==b:
			if l[i]['cabelo']==c:
				k=k+1
				total=total+l[i]['idade']
	MediaIdade=total/k
	return MediaIdade
def Maior(a):
	k=0
	for i in range(a):
		if l[i]['idade']>k:
			k=l[i]['idade']
	return k


l=[]
print 'Digite a quantidade de habitantes'
a=input()
for i in range (a):
	dic={}
	dic['sexo']=raw_input('Digite o sexo: Masculino(m) Feminino(f):')
	dic['olhos']=raw_input('Digite a cor dos olhos:Castanho(c); Verde(v); Azul(a); Preto(p); Outros(o):')	
	dic['cabelo']=raw_input('Digite a cor do cabelo:Castanho(c); Loiro(l); Ruivo(r); Outros(o):')
	dic['idade']=input('Digite a idade:')
	l.append(dic)
b=raw_input('Digite a cor de olhos a ser verificada:Castanho(c);Verde(v);Azul(a);Preto(p); Outros(o):')
c=raw_input('Digite a cor do cabelo a ser verificado:Castanho(c); Loiro(l); Ruivo(r); Outros(o):')
print 'Media das idades:',media(a,b,c)
print 'Maior idade:',Maior(a)
