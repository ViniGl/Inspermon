import json
import os

# def CarregarOuSave():
# 	carregar_comecar_b=True
# 	while carregar_comecar_b==True:
# 		carregar_comecar=int(input("O que voce deseja fazer, carregar o ultimo jogo (1) ou comecar do zero (2)?"))
# 		if carregar_comecar == 1:
# 			carregar_comecar_b=False
# 			file = open('nome.json','rb')
# 			jogo=file.readline()
# 			jogo_lido=jogo.decode()
# 			jogo_obj=json.loads(jogo_lido)


# 		elif carregar_comecar == 2:
# 			jogo_obj=['Joao','Marcelo']
# 			jogo_string = json.dumps(jogo_obj)
# 			file =  open('novojogo.json', 'wb')
# 			file.write(jogo_string.encode())
# 			file.close()
# 			file = open('novojogo.json','rb')
# 			jogo=file.readline()
# 			jogo_lido=jogo.decode()
# 			jogo_obj=json.loads(jogo_lido)
# 			carregar_comecar_b=False
# 	return jogo_obj

def Save12(jogo_obj):
	a=jogo_obj
	file = open('nome.json','wb')
	jogo_string=json.dumps(a)
	file.write(jogo_string.encode())
	file.close()
def Save13(insperdex):
	a=insperdex
	file = open('insperdex.json','wb')
	jogo_string=json.dumps(a)
	file.write(jogo_string.encode())
	file.close()

def LendoSave():
	file = open('nome.json' , 'rb')
	data_total = file.readline()
	data_nova= data_total
	datanova=data_nova.decode()
	obj= json.loads(datanova)
	file.close()
	return obj

def dex_load():
	file = open('insperdex.json' , 'rb')
	data_total = file.readline()
	data_nova= data_total
	datanova=data_nova.decode()
	obj= json.loads(datanova)
	file.close()
	return obj	