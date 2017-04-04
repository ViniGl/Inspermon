# from ____ import reset_save
# jogar=int(input("Se quiser jogar digite 0 se quiser resetar 1"))
# reset_save(jogar)
from lista_de_pkm import pokemon as pkm
from lutas import engine_luta
import os 
import time
os.system('cls')

nome_jogador1=input("Qual o seu nome treinador pokemon? ")
nome_jogador=nome_jogador1.title()
time.sleep(2)
os.system('cls')
print("Seja Bem Vindo {}, pronto para se tornar o treinador pokemon mais respeitado da historia?".format(nome_jogador))
time.sleep(4)
print("Agora vamos comecar a nossa dura jornada pelo mundo dos InsperMons!")
time.sleep(4)
os.system('cls')


pokemons_capturados=[pkm[0],pkm[3],pkm[6],pkm[20],pkm[12]]
x=1
escolhab=False
pokemonb=False
while escolhab==False:
	pokemonb=False
	oquefazer=input("{} o que voce gostaria fazer, dormir ou andar?".format(nome_jogador))
	os.system('cls')
	escolha=oquefazer.lower()
	if escolha == "andar":
		x=1
		for i in pokemons_capturados:
			print(i[0] + " ""(""{}""" ")".format(x))
			x+=1
		while pokemonb==False:
			pokemon_escolhido=int(input("Escolha seu Pokemon: "))
			os.system('cls')
			if pokemon_escolhido <= len(pokemons_capturados):
				a=(pokemons_capturados[pokemon_escolhido-1])
				if pokemon_escolhido==1:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					engine_luta(a)
				elif pokemon_escolhido==2:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					engine_luta(a)
				elif pokemon_escolhido==3:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					engine_luta(a)
				elif pokemon_escolhido==4:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					engine_luta(a)
				elif pokemon_escolhido==5:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					engine_luta(a)
				elif pokemon_escolhido==6:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
			else:
				pokemonb=False					
		escolhab=False
	elif escolha == "dormir":
		print("Boa noite!")
		time.sleep(1)
		os.system('cls')
		escolhab=True
	else:
		escolhab=False

	

