#Grama, Fogo, Agua, Luta, normal, eletrico
from lista_de_pkm import pokemon as pkm
import random
def ataques():
	def grama():
		vine_whip=35#0	
		leaf_blade=70#1
		bullet_seed=10#2
		razor_leaf=55#3
		return vine_whip,leaf_blade,bullet_seed,razor_leaf
	def luta():
		jump_kick=70#4
		rock_smash=20#5
		triple_kick=30#6
		brick_break=75#7
		return jump_kick,rock_smash,triple_kick,brick_break
	def fogo():	
		ember=40#8
		fire_spin=15#9
		flame_wheel=60#10
		fire_punch=75#11
		return ember,fire_spin,flame_wheel,fire_punch
	def agua():
		bubble=20#12
		dive=60#13
		water_pulse=60#14
		bubblebeam=65#15
		return bubble,dive,water_pulse,bubblebeam
	def eletrico():
		thunder_bolt=95#16
		spark=65#17
		shock_wave=60#18
		thunderpunch=75#19
		return thunder_bolt,spark,shock_wave,thunderpunch
	def normal():
		cut=50#20
		egg_bomb=100#21
		mega_punch=80#22
		quick_attack=40#23
		return cut,egg_bomb,mega_punch,quick_attack

	for i in range(len(pkm)):
		if pkm[i][5]=='fogo' and pkm[i][6]=='ev1' and len(pkm[i])<12:
			a=random.sample(fogo(),2)
			b=random.sample(normal(),2)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='agua' and pkm[i][6]=='ev1'and len(pkm[i])<12:
			a=random.sample(agua(),2)
			b=random.sample(normal(),2)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='luta' and pkm[i][6]=='ev1'and len(pkm[i])<12:
			a=random.sample(luta(),2)
			b=random.sample(normal(),2)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='grama' and pkm[i][6]=='ev1'and len(pkm[i])<12:
			a=random.sample(grama(),2)
			b=random.sample(normal(),2)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='eletrico' and pkm[i][6]=='ev1'and len(pkm[i])<12:
			a=random.sample(eletrico(),2)
			b=random.sample(normal(),2)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='normal' and pkm[i][6]=='ev1'and len(pkm[i])<12:
			a=random.sample(normal(),4)
			c=pkm[i].extend(a)
		if pkm[i][5]=='fogo' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			a=random.sample(fogo(),3)
			b=random.sample(normal(),1)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)
		if pkm[i][5]=='agua' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			a=random.sample(agua(),3)
			b=random.sample(normal(),1)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)	
		if pkm[i][5]=='eletrico' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			a=random.sample(eletrico(),3)
			b=random.sample(normal(),1)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)			
		if pkm[i][5]=='grama' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			a=random.sample(grama(),3)
			b=random.sample(normal(),1)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)	
		if pkm[i][5]=='normal' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			b=random.sample(normal(),4)
			c=pkm[i].extend(b)		
		if pkm[i][5]=='luta' and pkm[i][6]=='ev2'and len(pkm[i])<12:
			a=random.sample(luta(),3)
			b=random.sample(normal(),1)
			c=pkm[i].extend(a)
			d=pkm[i].extend(b)	
		if pkm[i][5]=='fogo' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(fogo(),4)
			c=pkm[i].extend(a)	
		if pkm[i][5]=='luta' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(luta(),4)
			c=pkm[i].extend(a)	
		if pkm[i][5]=='agua' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(agua(),4)
			c=pkm[i].extend(a)			
		if pkm[i][5]=='grama' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(grama(),4)
			c=pkm[i].extend(a)
		if pkm[i][5]=='eletrico' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(eletrico(),4)
			c=pkm[i].extend(a)	
		if pkm[i][5]=='normal' and pkm[i][6]=='ev3'and len(pkm[i])<12:
			a=random.sample(luta(),4)
			c=pkm[i].extend(a)

ataques()