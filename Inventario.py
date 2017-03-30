import pickle
pokebolas=0
pokemons_capturados=[]
pocao_vida=0
with open('inventario.pickle','wb') as inv:
		pickle.dump(pokebolas,inv)
		pickle.dump(pokemons_capturados,inv)
		pickle.dump(pocao_vida,inv)


	