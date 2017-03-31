#Lista stats de cada pokemon
#Ordem:Nome[0], Hp[1], Atk[2], Def[3],atk1[4],atk2[5],atk3[6],atk4[7]
from ataques import ataques
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
#Ataques para cada pokemon
pokemon[0].append(ataques()[0])
pokemon[0].append(ataques()[1])
pokemon[0].append(ataques()[2])
pokemon[0].append(ataques()[3])
pokemon[3].append(ataques()[8])
pokemon[3].append(ataques()[9])
pokemon[3].append(ataques()[10])
pokemon[3].append(ataques()[11])
pokemon[3].append(ataques()[12])
pokemon[6].append(ataques()[13])
pokemon[6].append(ataques()[14])
pokemon[6].append(ataques()[15])

