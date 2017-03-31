# from ____ import reset_save
# jogar=int(input("Se quiser jogar digite 0 se quiser resetar 1"))
# reset_save(jogar)
from lista_de_pkm import pokemon as pkm
from lutas import engine_luta
import os 
from lutas import pokemon_lutador

os.system('cls')
pokemons_capturados=[pkm[0],pkm[3],pkm[6]]
x=1
escolhab=False
pokemonb=False
while escolhab==False:
	oquefazer=input("O que voce deseja fazer, dormir ou andar?")
	os.system('cls')
	escolha=oquefazer.lower()
	if escolha == "andar":
		for i in pokemons_capturados:
			print(i[0] + " ""(""{}""" ")".format(x))
			x+=1
		while pokemonb==False:
			pokemon_escolhido=int(input("Escolha seu Pokemon: "))
			a=list(pokemons_capturados[pokemon_escolhido-1])
			pokemon_lutador(a)
			os.system('cls')
			if pokemon_escolhido<= len(pokemons_capturados):
				if pokemon_escolhido==1:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				elif pokemon_escolhido==2:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				elif pokemon_escolhido==3:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				elif pokemon_escolhido==4:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				elif pokemon_escolhido==5:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				elif pokemon_escolhido==6:
					print("{} foi escolhido".format(pokemons_capturados[pokemon_escolhido-1][0]))
					pokemonb=True
				engine_luta(pokemon_escolhido)
			else:
				pokemonb=False
		escolhab=True
	elif escolha == "dormir":
		print("dormir")
		escolhab=True
	else:
		escolhab=False

	

