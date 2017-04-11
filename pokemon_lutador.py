from lista_de_pkm import pokemon as pkm
from inventario import inventario
class pkm_selecionado:
	def selecao():
		selecao_pkm=int(input("Escolha seu Pokemon: "))
		return selecao_pkm
	level=1
	nome=inventario.pokemons_capturados[selecao()-1][0]
	vida=int((((int(inventario.pokemons_capturados[selecao()-1][2])*2*level)/100))+level+10)
	ataque=int((inventario.pokemons_capturados[selecao()-1][3]))
	defesa=int((inventario.pokemons_capturados[selecao()-1][4]))