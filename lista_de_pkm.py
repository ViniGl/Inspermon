#Lista stats de cada pokemon
#Ordem:Nome[0], Hp[1], Atk[2], Def[3], Sp atk[4], sp def[5], speed[6]
with open("pkm.txt", "r") as arquivo:
	lista_de_nomes=[]
	for linha in arquivo :
		lista_de_nomes.append(linha)	
lista1=(lista_de_nomes)
pokemon=[]
x=0
while x<len(lista1):
	itens=lista1[x].split()
	pokemon.append(itens)
	x=x+1


