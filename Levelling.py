#Level
from lista_de_pkm import pokemon as pkm
from inventario import inventario
import time
import os 
from evolucao import evolucao
def level_up(poke_lutador,n):
	pkm_evolucao=poke_lutador
	exp=[int(poke_lutador[8])]
	#Level 1-10
	if int(poke_lutador[1])<10:
		exp.append(10)		
		os.system('cls')
		print ('{} ganhou 10 exp!'.format(poke_lutador[0]))
		time.sleep(1)
		soma=sum(exp)	
	if soma>=10*int(poke_lutador[1]):
	 	poke_lutador[1]=int(poke_lutador[1])+1
	 	
	 	#Evolucao 1
	if int(poke_lutador[1])==10:
		os.system('cls')
		print('{} esta evoluindo!'.format(poke_lutador[0]))
		time.sleep(2)
		os.system('cls')
		print('.	.	.')
		time.sleep(2)
		os.system('cls')
		inventario.pokemons_capturados.pop(n-1)
		inventario.pokemons_capturados.insert(n-1,evolucao(pkm_evolucao))
		print('{} se transformou em {}'.format(poke_lutador[0],inventario.pokemons_capturados[n-1][0]))
		time.sleep(2)

	if int(poke_lutador[1])>=15:
		exp.append(20)		
		os.system('cls')
		print ('{} ganhou 10 exp!'.format(poke_lutador[0]))
		time.sleep(1)
		soma=sum(exp)	
	if soma>=5*int(poke_lutador[1]):
	 	poke_lutador[1]=int(poke_lutador[1])+1

	if int(poke_lutador[1])==17:
		os.system('cls')
		print('{} esta evoluindo!'.format(poke_lutador[0]))
		time.sleep(2)
		os.system('cls')
		print('.	.	.')
		time.sleep(2)
		os.system('cls')
		inventario.pokemons_capturados.pop(n-1)
		inventario.pokemons_capturados.insert(n-1,evolucao(pkm_evolucao))
		print('{} se transformou em {}'.format(poke_lutador[0],inventario.pokemons_capturados[n-1][0]))
		time.sleep(2)

	if int(poke_lutador[1])==20:
		int(poke_lutador[1])==20