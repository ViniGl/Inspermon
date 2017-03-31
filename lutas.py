from lista_de_pkm import pokemon as pkm
from ataques import ataques
import random
import os 
#Falta o level
def engine_luta():
	vida_jogador=int(pkm[0][1])				#Vida, atk e defesa serao escolhidos a partir do pokemon selecionado
	ataque_jogador=int(pkm[0][2])
	defesa_jogador=int(pkm[0][3])
	vida_cpu=int(pkm[6][1])
	defesa_cpu=int(pkm[6][2])
	ataque_cpu=int(pkm[6][3])
	level=1
	while vida_jogador>0 or vida_cpu>0:
		os.system('cls')
		print (vida_jogador)
		print(vida_cpu)
		escolha=input('Lutar ou fugir:')
		os.system('cls')
		print (vida_jogador)
		print(vida_cpu)
		while escolha !='lutar' and escolha!='fugir':
			escolha=input('Lutar ou fugir?')
			os.system('cls')
			print (vida_jogador)
			print(vida_cpu)
		escolha.lower()
		if escolha=='lutar':
			escolha_atk=input('Escolha seu ataque(1 a 4):')
			os.system('cls')
			print (vida_jogador)
			print(vida_cpu)
			while escolha_atk!='1' and escolha_atk!='2' and escolha_atk!='3'and escolha_atk!='4':
					escolha_atk=input('Escolha seu ataque(1 a 4):')
					os.system('cls')
					print (vida_jogador)
					print(vida_cpu)
			if escolha_atk=='1':
				escolha_atk=pkm[0][4]
			elif escolha_atk=='2':
				escolha_atk=pkm[0][5]
			elif escolha_atk=='3':
				escolha_atk=pkm[0][6]
			elif escolha_atk=='4':
				escolha_atk=pkm[0][7]
			escolha_atk_cpu=random.choice(ataques())
			vida_cpu=vida_cpu-int((((((2*level/5)+2)*escolha_atk*(ataque_jogador/defesa_cpu))+2)/50))					#Equacao de dano 
			vida_jogador=vida_jogador-int(((((2*level/5)+2)*escolha_atk_cpu*(ataque_cpu/defesa_jogador)+2)/50))
			if vida_cpu<=0:
				os.system('cls')
				print('Jogador venceu!')
				break
			if vida_jogador<=0:
				os.system('cls')
				print('Cpu venceu!')
				break
		if escolha=='fugir':
			os.system('cls')
			print('Voce fugiu')
			break
engine_luta()