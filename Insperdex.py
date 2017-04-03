#InsperDex
from lista_de_pkm import pokemon as pkm
from ataques import ataques
def insperdex():
	ataques()
	a=int(input('Qual pokemon deseja buscar?'))
	for i in range(len(pkm)):
		print(pkm[i])
insperdex()