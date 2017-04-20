#PokeCenter
from lista_de_pkm import pokemon as pkm
from inventario import inventario
def pokecenter():
		if inventario.pokebolas<7:
			print('Inventario de pokebolas reestabelecido')
			inventario.pokebolas=7
		if inventario.pocao_vida<10:
			inventario.pocao_vida=10
			print('Inventario de pocoes de vida reeestabelecido')
		else:
			print('Inventario cheio')
		for pokes in range(len(inventario.pokemons_capturados)):
			level=int(inventario.pokemons_capturados[len(inventario.pokemons_capturados)-1][1])
			if int(inventario.pokemons_capturados[pokes][3])<int((((int(inventario.pokemons_capturados[pokes][2])*2*level)/100))+level+10):
				inventario.pokemons_capturados[pokes][3]=int((((int(inventario.pokemons_capturados[pokes][2])*2*level)/100))+level+10)
				print('Vida dos pokemons restaurada!')	

