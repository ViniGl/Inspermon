#Lista stats de cada pokemon
#Ordem:Nome[0], Hp[1],Hp_temp[2], Atk[3], Def[4],Type[5], Evolucao[6],Ataque1[7],ataque2[8],ataque3[9],ataque4[10]
with open("pkm1.txt", "r") as arquivo:
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


