from lista_de_pkm import pokemon as pkm
from ataques import ataques
import random
from CPU import CPU
import os 
import time
from inventario import inventario

#Falta o level
def engine_luta(pokemon_lutador):
	#Parametros
	ataques()
	pokemon_cpu=random.choice(pkm)
	level=1
	nome_pkm=pokemon_lutador[0]
	vida_jogador=int((((int(pokemon_lutador[2])*2*level)/100))+level+10)
	ataque_jogador=int((pokemon_lutador[3]))
	defesa_jogador=int((pokemon_lutador[4]))
	vida_cpu=int(CPU(pokemon_cpu)[2])
	defesa_cpu=int(CPU(pokemon_cpu)[4])
	ataque_cpu=int(CPU(pokemon_cpu)[3])


	#Loop da luta
	while vida_jogador>0 or vida_cpu>0:
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
				escolha_atk=pokemon_lutador[7]
			elif escolha_atk=='2':
				escolha_atk=pokemon_lutador[8]
			elif escolha_atk=='3':
				escolha_atk=pokemon_lutador[9]
			elif escolha_atk=='4':
				escolha_atk=pokemon_lutador[10]
			escolha_atk_cpu=random.choice(CPU(pokemon_cpu)[5:8])
			#Equacoes de dano
			vida_cpu=int(vida_cpu-(((((2*level/5)+2)*escolha_atk*(ataque_jogador/defesa_cpu))+2)/50))
			vida_jogador=int(vida_jogador-((((2*level/5)+2)*escolha_atk_cpu*(ataque_cpu/defesa_jogador)+2)/50))
			#Fim da luta
			if vida_cpu<=0:
				pokemon_lutador.pop(2)
				pokemon_lutador.insert(2,vida_jogador)
				os.system('cls')
				print('Jogador venceu!')
				time.sleep(1)
				os.system('cls')
				break
			if vida_jogador<=0:
				pokemon_lutador.pop(2)
				pokemon_lutador.insert(2,vida_jogador)
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
		if escolha=='capturar':
			a=random.randrange(0,100,1)
			if a<=20 and a>=0:
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
				time.sleep(3)
				os.system('cls')
				break
			if a>20 and a<=55:
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
				time.sleep(3)
				os.system('cls')
			else:
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
				time.sleep(3)
				os.system('cls')
				break

		






