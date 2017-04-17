#Level
from lista_de_pkm import pokemon as pkm
from inventario import inventario
def level(poke_lutador):
	exp=pokemon_lutador[12]
	if int(pokemon_lutador[1])<=15:
		exp=exp+10
		if exp>=10*int(pokemon_lutador[1]):
			pokemon_lutador[1]=pokemon_lutador[1]+1
			pokemon_lutador[12]=0
		#Evolucao

	elif int(pokemon_lutador[1])<=30:
		exp=exp+20
		if exp>=10*int(pokemon_lutador[1]):
			pokemon_lutador[1]=pokemon_lutador[1]+1
			pokemon_lutador[12]=0
		if pokemon_lutador[1]==30:


			inventario.pokemons_capturados[valor_lista-1] 
	elif int(pokemon_lutador[1])<=50:
		exp=exp+35
