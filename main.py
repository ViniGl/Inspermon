# from ____ import reset_save
# jogar=int(input("Se quiser jogar digite 0 se quiser resetar 1"))
# reset_save(jogar)
from lista_de_pkm import pokemon
pokemons_capturados=[pokemon[0],pokemon[1],pokemon[2]]
x=1
escolhab=False
pokemonb=False
while escolhab==False:
	oquefazer=input("O que voce deseja fazer, dormir ou andar?")
	escolha=oquefazer.lower()
	if escolha == "andar":
		for i in pokemons_capturados:
			print(i[0] + " ""(""{}""" ")".format(x))
			x+=1
		while pokemonb==False:
			a=int(input("Escolha seu Pokemon:  "))
			if a<= len(pokemons_capturados):
				if a==1:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
				elif a==2:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
				elif a==3:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
				elif a==4:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
				elif a==5:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
				elif a==6:
					print("{} foi escolhido".format(pokemons_capturados[a-1][0]))
					pokemonb=True
			else:
				pokemonb=False
		escolhab=True
	elif escolha == "dormir":
		print("dormir")
		escolhab=True
	else:
		escolhab=False

	

