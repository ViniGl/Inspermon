from lista_de_pkm import pokemon as pkm
from ataques import ataques
import random
from CPU import CPU
import os 
import time
from inventario import inventario
import pygame

#Falta o level
def engine_luta(pokemon_lutador,valor_lista):
	#Parametros
	ataques()
	valor_lista=int(valor_lista)
	poke_lutador=inventario.pokemons_capturados[valor_lista-1]
	pokemon_cpu=random.choice(pkm)
	level=1
	nome_pkm=pokemon_lutador[0]
	if int(inventario.pokemons_capturados[valor_lista-1][3])<=0:
		vida_jogador=0
	elif int(inventario.pokemons_capturados[valor_lista-1][3])<int((((int(pokemon_lutador[3])*2*level)/100))+level+10):
		vida_jogador=int(inventario.pokemons_capturados[valor_lista-1][3])
	else:	
		vida_jogador=int((((int(pokemon_lutador[3])*2*level)/100))+level+10)
	ataque_jogador=int((pokemon_lutador[4]))
	defesa_jogador=int((pokemon_lutador[5]))
	vida_cpu=int(CPU(pokemon_cpu)[2])
	defesa_cpu=int(CPU(pokemon_cpu)[4])
	ataque_cpu=int(CPU(pokemon_cpu)[3])

	if vida_jogador<=0:
		os.system('cls')
		print("Seu {} esta fraco, leve-o paro o pokecenter!".format(nome_pkm))
		time.sleep(1.5)
		os.system('cls')
	#Loop da luta
	while vida_jogador>0 and vida_cpu>0:
		os.system('cls')
		print("{}:{}".format(nome_pkm,vida_jogador))
		print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		escolha=input('Lutar, fugir ou capturar:').lower()
		os.system('cls')
		print("{}:{}".format(nome_pkm,vida_jogador))
		print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		while escolha !='lutar' and escolha!='fugir' and escolha!='capturar':
			escolha=input('Lutar, fugir ou capturar?')
			os.system('cls')
			print("{}:{}".format(nome_pkm,vida_jogador))
			print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		escolha.lower()
		if escolha=='lutar':
			escolha_atk=input('Escolha seu ataque(1 a 4):')
			os.system('cls')
			print("{}:{}".format(nome_pkm,vida_jogador))
			print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
			os.system('cls')
			while escolha_atk!='1' and escolha_atk!='2' and escolha_atk!='3'and escolha_atk!='4':
					escolha_atk=int(input('Escolha seu ataque(1 a 4):'))
					os.system('cls')
					print("{}:{}".format(nome_pkm,vida_jogador))
					print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
			if escolha_atk=='1':
				escolha_atk=pokemon_lutador[9]
			elif escolha_atk=='2':
				escolha_atk=pokemon_lutador[10]
			elif escolha_atk=='3':
				escolha_atk=pokemon_lutador[11]
			elif escolha_atk=='4':
				escolha_atk=pokemon_lutador[12]
			escolha_atk_cpu=random.choice(CPU(pokemon_cpu)[5:8])
			#Equacoes de dano
			vida_cpu=int(vida_cpu-(((((2*level/5)+2)*escolha_atk*(ataque_jogador/defesa_cpu))+2)/50))
			vida_jogador=int(vida_jogador-((((2*level/5)+2)*escolha_atk_cpu*(ataque_cpu/defesa_jogador)+2)/50))
			#Fim da luta
			if vida_cpu<=0:
				inventario.pokemons_capturados[valor_lista-1].pop(2)
				inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
				os.system('cls')
				print('Jogador venceu!')
				
				time.sleep(1)
				pygame.mixer.music.stop()
				os.system('cls')
				break
			if vida_jogador<=0:
				inventario.pokemons_capturados[valor_lista-1].pop(2)
				inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
				os.system('cls')
				print('Cpu venceu!')
				time.sleep(1)
				pygame.mixer.music.stop()
				os.system('cls')
				break
		if escolha=='fugir':
			inventario.pokemons_capturados[valor_lista-1].pop(2)
			inventario.pokemons_capturados[valor_lista-1].insert(2,vida_jogador)
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
			else	:
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
				






