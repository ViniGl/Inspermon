#cpu
from lista_de_pkm import pokemon as pkm
import random
from ataques import ataques
def CPU(pokemon_cpu):
	ataques()
	pokemon_cpu=pokemon_cpu
	level_cpu=int(pokemon_cpu[1])
	nome_cpu=pokemon_cpu[0]
	hp_cpu=(((int(pokemon_cpu[2])*2)*level_cpu)/100)+level_cpu+10
	ataque_cpu=pokemon_cpu[4]
	defesa_cpu=pokemon_cpu[5]
	golpe1=pokemon_cpu[9]
	golpe2=pokemon_cpu[10]
	golpe3=pokemon_cpu[11]
	golpe4=pokemon_cpu[12]
	return pokemon_cpu,nome_cpu,hp_cpu,ataque_cpu,defesa_cpu,golpe1,golpe2,golpe3,golpe4