# from ____ import reset_save
# jogar=int(input("Se quiser jogar digite 0 se quiser resetar 1"))
# reset_save(jogar)

escolhab=False
while escolhab==False:
	oquefazer=input("O que voce deseja fazer, dormir ou andar?")
	escolha=oquefazer.lower()
	if escolha in "andar":
		print("andou")
		escolhab=True

	elif escolha in "dormir":
		print("dormir")
		escolhab=True
	else:
		escolhab=False

	

