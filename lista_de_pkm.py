with open("pkm.txt", "r") as arquivo:
	lista_de_nomes=[]
	for linha in arquivo :
		lista_de_nomes.append(linha)	
lista1=(lista_de_nomes)
listanova=[]
x=0
while x<len(lista1):
	itens=lista1[x].split()
	listanova.append(itens)
	x=x+1
	print(itens)