# from ____ import reset_save
# jogar=int(input("Se quiser jogar digite 0 se quiser resetar 1"))
# reset_save(jogar)
from lista_de_pkm import pokemon as pkm
from lutas import engine_luta
import os 
import time
from inventario import inventario
from Pokecenter import pokecenter
import random
import pickle
import pygame
from tkinter import *
#Pickle vida temp
#Saves
os.system('cls')
class nomes_salvos:
	jogadores_totais=0
	def jogadores(self,jogadores):
		self.jogadores=jogadores
		nomes_salvos.jogadores_totais+=1

#musica		
file = 'pkmsong1.mp3'
file2='pkmfight.mp3'
root = Tk()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
root.mainloop()

# nome_jogador=input("Qual o seu nome treinador pokemon? ")
# nome_jogador1=nome_jogador.title()
# os.system('cls')
# print("Seja Bem Vindo {}, pronto para se tornar o treinador pokemon mais respeitado da historia?".format(nome_jogador1))
# time.sleep(4)
# os.system('cls')
# print("Agora vamos comecar a nossa dura jornada pelo mundo dos InsperMons!")
# time.sleep(4)
# os.system('cls')
print ('{}  (1)\n{}  (2)\n{}  (3)' .format(pkm[0][0],pkm[3][0],pkm[6][0]))
pokemon_inicial=int(input('Escolha seu primeiro pokemon:'))
if pokemon_inicial==1:
	pokemon_inicial=0
elif pokemon_inicial==2:
	pokemon_inicial=3
elif pokemon_inicial==3:
	pokemon_inicial=6
inventario.pokemons_capturados.append(pkm[pokemon_inicial])
inventario.pokebolas=7
os.system('cls')

#Loop da parte principal
x=1
escolhab=False
pokemonb=False
while escolhab==False:
	pygame.mixer.music.unpause()
	pokemonb=False
	# oquefazer=input("{}, o que voce gostaria fazer? Andar, pokecenter, status ou dormir?".format(nome_jogador1))
	oquefazer=input("o que voce gostaria fazer? Andar, pokecenter, status ou dormir?")
	os.system('cls')
	escolha=oquefazer.lower()
	if escolha == "andar":
		while pokemonb==False:
			x=1
			for i in inventario.pokemons_capturados:
				print(i[0] + " ""(""{}""" ")".format(x))
				x+=1
			pokemon_escolhido=int(input("Escolha seu Pokemon: "))
			os.system('cls')
			if pokemon_escolhido <= len(inventario.pokemons_capturados):
				chance=random.randint(0,100)
				a=(inventario.pokemons_capturados[pokemon_escolhido-1])
				if pokemon_escolhido==1 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					pygame.mixer.music.pause()
					pygame.mixer.music.load(file2)
					pygame.mixer.music.play()
					engine_luta(a,pokemon_escolhido)
				elif pokemon_escolhido==2 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					pygame.mixer.music.pause()
					pygame.mixer.music.load(file2)
					pygame.mixer.music.play()	
					engine_luta(a,pokemon_escolhido)
				elif pokemon_escolhido==3 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					pygame.mixer.music.pause()
					pygame.mixer.music.load(file2)
					pygame.mixer.music.play()
					engine_luta(a,pokemon_escolhido)
				elif pokemon_escolhido==4 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					pygame.mixer.music.pause()
					pygame.mixer.music.load(file2)
					pygame.mixer.music.play()
					engine_luta(a,pokemon_escolhido)
				elif pokemon_escolhido==5 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
					pygame.mixer.music.pause()
					pygame.mixer.music.load(file2)
					pygame.mixer.music.play()
					engine_luta(a,pokemon_escolhido)
				elif pokemon_escolhido==6 and chance>=36:
					print("{} foi escolhido".format(inventario.pokemons_capturados[pokemon_escolhido-1][0]))
					time.sleep(1)
					pokemonb=True
				else:
					print('Nenhum pokemon encontrado')
					time.sleep(1.3)
					os.system('cls')
					pokemonb=True
			else:
				pokemonb=False					
		escolhab=False
	#Status
	elif escolha=='status':
		level=1
		print('Pokebolas:{}'.format(inventario.pokebolas))
		print('Pocoes de vida:{}'.format(inventario.pocao_vida))
		for pokes in range(len(inventario.pokemons_capturados)):
			if int(inventario.pokemons_capturados[pokes][3])<=0:
				vida=0
			elif int(inventario.pokemons_capturados[pokes][3])<int((((int(inventario.pokemons_capturados[pokes][3])*3*level)/100))+level+10):
				vida=int(inventario.pokemons_capturados[pokes][3])
			else:	
				vida=int((((int(inventario.pokemons_capturados[pokes][3])*2*level)/100))+level+10)
			print('{}:{}'.format(inventario.pokemons_capturados[pokes][0],vida))
		time.sleep (2)
		os.system('cls')
	#PokeCenter
	elif escolha=='pokecenter':
		pokecenter()
		time.sleep (1.5)
		os.system('cls')
	#Dormir
	elif escolha == "dormir":
		print("Boa noite!")
		time.sleep(1)
		os.system('cls')
		escolhab=True
	
	else:
		escolhab=False

	

