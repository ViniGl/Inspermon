from lista_de_pkm import pokemon as pkm
from ataques import ataques
import random
from CPU import CPU
import os 
import time
#Falta o level
def engine_luta(pokemon_escolhido):
	pokemon_cpu=random.choice(pkm)
	level=1
	nome_pkm=pokemon_escolhido[0]
	vida_jogador=int((((int(pokemon_escolhido[1])*2*level)/100))+level+10)
	ataque_jogador=int((pokemon_escolhido[2]))
	defesa_jogador=int((pokemon_escolhido[3]))
	ataque1=pokemon_escolhido[6]
	ataque2=pokemon_escolhido[7]
	ataque3=pokemon_escolhido[8]
	ataque4=pokemon_escolhido[9]
	pkm_cpu=CPU(pokemon_cpu)[1]
	vida_cpu=int(CPU(pokemon_cpu)[2])
	defesa_cpu=int(CPU(pokemon_cpu)[4])
	ataque_cpu=int(CPU(pokemon_cpu)[3])
	while vida_jogador>0 or vida_cpu>0:
		ataques()
		os.system('cls')
		print("{}:{}".format(nome_pkm,vida_jogador))
		print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		escolha=input('Lutar ou fugir:')
		os.system('cls')
		print("{}:{}".format(nome_pkm,vida_jogador))
		print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		while escolha !='lutar' and escolha!='fugir':
			escolha=input('Lutar ou fugir?')
			os.system('cls')
			print("{}:{}".format(nome_pkm,vida_jogador))
			print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
		escolha.lower()
		if escolha=='lutar':
			escolha_atk=input('Escolha seu ataque(1 a 4):')
			os.system('cls')
			print("{}:{}".format(nome_pkm,vida_jogador))
			print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
			while escolha_atk!='1' and escolha_atk!='2' and escolha_atk!='3'and escolha_atk!='4':
					escolha_atk=int(input('Escolha seu ataque(1 a 4):'))
					os.system('cls')
					print("{}:{}".format(nome_pkm,vida_jogador))
					print('{}:{}'.format(CPU(pokemon_cpu)[1],vida_cpu))
			if escolha_atk=='1':
				escolha_atk=pokemon_escolhido[6]
			elif escolha_atk=='2':
				escolha_atk=pokemon_escolhido[7]
			elif escolha_atk=='3':
				escolha_atk=pokemon_escolhido[8]
			elif escolha_atk=='4':
				escolha_atk=pokemon_escolhido[9]
			escolha_atk_cpu=random.choice(CPU(pokemon_cpu)[5:8])	
			vida_cpu=int(vida_cpu-(((((2*level/5)+2)*escolha_atk*(ataque_jogador/defesa_cpu))+2)/50))			#Equacao de dano 
			vida_jogador=int(vida_jogador-((((2*level/5)+2)*escolha_atk_cpu*(ataque_cpu/defesa_jogador)+2)/50))
			if vida_cpu<=0:
				os.system('cls')
				print('Jogador venceu!')
				time.sleep(1)
				os.system('cls')
				break
			if vida_jogador<=0:
				os.system('cls')
				print('Cpu venceu!')
				time.sleep(1)
				os.system('cls')
				break
		if escolha=='fugir':
			os.system('cls')
			print('Voce fugiu')
			time.sleep(1)
			os.system('cls')
			break

		






