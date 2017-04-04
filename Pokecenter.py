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