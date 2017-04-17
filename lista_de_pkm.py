#Lista stats de cada pokemon
#Ordem:Nome[0], level[1], Hp[2],Hp_temp[3], Atk[4], Def[5],Type[6], Evolucao[7],Ataque1[8],ataque2[9],ataque3[10],ataque4[11],exp[12]
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


