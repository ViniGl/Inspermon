#inventario
import pickle 
from lista_de_pkm import pokemon as pkm
import os
import time
from FuncaoSave import Save12
from FuncaoSave import LendoSave
import pygame
from tkinter import *

class inventario:
	os.system('cls')
	file = 'pkmsong1.mp3'
	file2='pkmfight.mp3'
	root = Tk()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	root.mainloop()
	fazeroq=int(input("Continuar jogo salvo (1) ou comecar novo jogo(2)?"))
	if fazeroq==2:
		os.remove('nome.json')
		pokemons_capturados=[]
		nome_jogador=input("Qual o seu nome treinador pokemon? ")
		nome_jogador1=nome_jogador.title()
		os.system('cls')
		print("Seja Bem Vindo {}, pronto para se tornar o treinador pokemon mais respeitado da historia?".format(nome_jogador1))
		time.sleep(4)
		os.system('cls')
		print("Agora vamos comecar a nossa dura jornada pelo mundo dos InsperMons!")
		time.sleep(4)
		os.system('cls')
		print ('{}  (1)\n{}  (2)\n{}  (3)' .format(pkm[0][0],pkm[3][0],pkm[6][0]))
		pokemon_inicial=int(input('Escolha seu primeiro pokemon:'))
		if pokemon_inicial==1:
			pokemon_inicial=0
		elif pokemon_inicial==2:
			pokemon_inicial=3
		elif pokemon_inicial==3:
			pokemon_inicial=6
		pokemons_capturados.append(pkm[pokemon_inicial])
		Save12(pokemons_capturados)
		pokebolas=7
		os.system('cls')
	if fazeroq==1:
		pokemons_capturados=LendoSave()
		print("Seja Bem Vindo de Volta")
		time.sleep(2)
	pokebolas=7
	pocao_vida=7		
		




