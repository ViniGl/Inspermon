from lista_de_pkm import pokemon as pkm
from ataques import ataques
import random
from CPU import CPU
import os 
import time
from inventario import inventario
import pygame
from Levelling import level_up
from Insperdex import insperdex
#Falta o level
def engine_luta(pokemon_lutador,valor_lista):
	#Parametros
	ataques()
	valor_lista=int(valor_lista)
	poke_lutador=inventario.pokemons_capturados[valor_lista-1]
	level=int(pokemon_lutador[1])
	nome_pkm=pokemon_lutador[0]
	if int(inventario.pokemons_capturados[valor_lista-1][3])<=0:
		vida_jogador=0
	elif int(inventario.pokemons_capturados[valor_lista-1][3])<int((((int(pokemon_lutador[3])*2*level)/100))+level+10):
		vida_jogador=int(inventario.pokemons_capturados[valor_lista-1][3])
	else:	
		vida_jogador=int((((int(pokemon_lutador[3])*2*level)/100))+level+10)
	lista_cpu_pokes=[]
	lista2_cpu_pokes=[]
	if level<10:
		for i in range(len(pkm)):
			if pkm[i][7]=='ev1':
				lista_cpu_pokes.append(pkm[i])
		pokemon_cpu=random.choice(lista_cpu_pokes)	
	
	if level>=10:
		for u in range(len(pkm)):
			if pkm[i][7]=='ev2' or pkm[i][7]=='ev3':
				lista2_cpu_pokes.append(pkm[i])
		pokemon_cpu=random.choice(lista2_cpu_pokes)	
	CPU(pokemon_cpu,poke_lutador)
	ataque_jogador=int((pokemon_lutador[4]))
	defesa_jogador=int((pokemon_lutador[5]))
	vida_cpu=int(CPU(pokemon_cpu,poke_lutador)[2])
	defesa_cpu=int(CPU(pokemon_cpu,poke_lutador)[4])
	ataque_cpu=int(CPU(pokemon_cpu,poke_lutador)[3])
	level_cpu=int(CPU(pokemon_cpu,poke_lutador)[9])
	insperdex.pkm_encontrados.append(pokemon_cpu)

	if vida_jogador<=0:
		os.system('cls')
		print("Seu {} esta fraco, leve-o paro o pokecenter!".format(nome_pkm))
		time.sleep(1.5)
		os.system('cls')
	#Loop da luta
	while vida_jogador>0 and vida_cpu>0:
		os.system('cls')
		print("{} (Level:{}) HP:{}".format(nome_pkm,level,vida_jogador))
		print('{} (Level:{}) HP:{}'.format(CPU(pokemon_cpu,poke_lutador)[1],level_cpu,vida_cpu))
		escolha=input('Lutar, curar, fugir ou capturar:').lower()
		os.system('cls')
		print("{} (Level:{}) HP:{}".format(nome_pkm,level,vida_jogador)) 
		print('{} (Level:{}) HP:{}'.format(CPU(pokemon_cpu,poke_lutador)[1],level_cpu,vida_cpu))
		
		while escolha !='lutar' and escolha!='fugir' and escolha!='capturar' and escolha!='curar':
			escolha=input('Lutar, curar, fugir ou capturar?')
			os.system('cls')
			print("{} (Level:{}) HP:{}".format(nome_pkm,level,vida_jogador))
			print('{} (Level:{}) HP:{}'.format(CPU(pokemon_cpu,poke_lutador)[1],level_cpu,vida_cpu))
		escolha.lower()
		
		if escolha=='lutar':
			escolha_atk=input('Escolha seu ataque(1 a 4):')
			os.system('cls')
			print("{} (Level:{}) HP:{}".format(nome_pkm,level,vida_jogador))
			print('{} (Level:{}) HP:{}'.format(CPU(pokemon_cpu,poke_lutador)[1],level_cpu,vida_cpu))
			os.system('cls')
			
			while escolha_atk!='1' and escolha_atk!='2' and escolha_atk!='3'and escolha_atk!='4':
					escolha_atk=int(input('Escolha seu ataque(1 a 4):'))
					os.system('cls')
					print("{} (Level:{}) HP:{}".format(nome_pkm,level,vida_jogador))
					print('{} (Level:{}) HP:{}'.format(CPU(pokemon_cpu,poke_lutador)[1],level_cpu,vida_cpu))
		
			if escolha_atk=='1':
				escolha_atk=pokemon_lutador[9]
		
			elif escolha_atk=='2':
				escolha_atk=pokemon_lutador[10]
		
			elif escolha_atk=='3':
				escolha_atk=pokemon_lutador[11]
		
			elif escolha_atk=='4':
				escolha_atk=pokemon_lutador[12]
			
			escolha_atk_cpu=random.choice(CPU(pokemon_cpu,poke_lutador)[5:8])
			#Equacoes de dano
			vida_cpu=int(vida_cpu-(((((2*level/5)+2)*escolha_atk*(ataque_jogador/defesa_cpu))+2)/50))
			vida_jogador=int(vida_jogador-((((2*level/5)+2)*escolha_atk_cpu*(ataque_cpu/defesa_jogador)+2)/50))
		
			#Fim da luta
			if vida_cpu<=0:
				inventario.pokemons_capturados[valor_lista-1].pop(3)
				inventario.pokemons_capturados[valor_lista-1].insert(3,vida_jogador)
				os.system('cls')
				print('Jogador venceu!')
				time.sleep(1)
				level_up(pokemon_lutador,valor_lista)
				time.sleep(1)
				pygame.mixer.music.stop()
				os.system('cls')
				break
			
			if vida_jogador<=0:
				inventario.pokemons_capturados[valor_lista-1].pop(3)
				inventario.pokemons_capturados[valor_lista-1].insert(3,vida_jogador)
				os.system('cls')
				print('Cpu venceu!')
				time.sleep(1)
				pygame.mixer.music.stop()
				os.system('cls')
				break
		
		if escolha=='fugir':
			inventario.pokemons_capturados[valor_lista-1].pop(3)
			inventario.pokemons_capturados[valor_lista-1].insert(3,vida_jogador)
			os.system('cls')
			print('Voce fugiu')
			time.sleep(1)
			pygame.mixer.music.stop()
			os.system('cls')
			break
	
		# Captura
		if escolha=='capturar':
			if inventario.pokebolas<=0:
				print('Voce nao possui pokebolas')
			a=random.randrange(0,20,1)
			
			if a<=20 and a>=0:
				os.system('cls')
				inventario.pokemons_capturados.append(pokemon_cpu)
				print("{} esta tentando escapar".format(pokemon_cpu[0]))
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print("Voce Capturou {} ! Parabens!!!".format(pokemon_cpu[0]))
				inventario.pokemons_capturados[valor_lista-1].pop(2)
				inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
				inventario.pokebolas=inventario.pokebolas-1
				
				time.sleep(3)
				pygame.mixer.music.stop()
				os.system('cls')
				break
			
			if a>20 and a<=55:
				os.system('cls')
				print("{} esta tentando escapar".format(pokemon_cpu[0]))
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print("{} escapou da pokebola! Mas continua na luta!".format(pokemon_cpu[0]))
				inventario.pokemons_capturados[valor_lista-1].pop(2)
				inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
				inventario.pokebolas=inventario.pokebolas-1
				time.sleep(3)
				pygame.mixer.music.stop()
				os.system('cls')
		
			else:
				os.system('cls')
				print("{} esta tentando escapar".format(pokemon_cpu[0]))
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print(". . .")
				time.sleep(2)
				os.system('cls')
				print("{} escapou da pokebola! E fugiu da luta".format(pokemon_cpu[0]))
				inventario.pokemons_capturados[valor_lista-1].pop(2)
				inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
				inventario.pokebolas=inventario.pokebolas-1
				time.sleep(3)
				pygame.mixer.music.stop()
				os.system('cls')
				break
		
		if escolha=='curar':
			if inventario.pocao_vida>0:
				vida_jogador=int((((int(pokemon_lutador[3])*2*level)/100))+level+10)	
				inventario.pocao_vida=inventario.pocao_vida-1
			else:
				print('Voce nao possui pocoes de vida.')	
				time.sleep(1)





