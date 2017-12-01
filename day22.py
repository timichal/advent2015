from itertools import product

def fight(cast):
	mana = 500
	playerHP = 50
	bossHP = 58
	bossDmg = 9

	#effects
	shield = False
	shield_timer = 0
	poison = False
	poison_timer = 0
	recharge = False
	recharge_timer = 0

	turn = "player"
	while True:
		playerHP -= 1
		#print("Player HP", playerHP, "mana", mana, "| boss HP", bossHP)
		if shield: 
			shield_timer -= 1
		if poison: 
			bossHP -= 3
			poison_timer -= 1
			if bossHP <= 0: return True
		if recharge:
			mana += 101
			recharge_timer -= 1
		if turn == "player":
			#print("Player turn")
			if len(cast) > 0:
				spell = cast.pop(0)
			else:
				return False
			#print("Casting", spell)
			if spell == "Poison":
				mana -= 173
				if mana < 0: return "OOM"
				poison = True
				poison_timer = 6
			elif spell == "Magic Missile":
				mana -= 53
				if mana < 0: return "OOM"				
				bossHP -= 4
			elif spell == "Recharge":
				mana -= 229
				if mana < 0: return "OOM"				
				recharge = True
				recharge_timer = 5
			elif spell == "Shield":
				mana -= 113
				if mana < 0: return "OOM"				
				shield = True
				shield_timer = 6
			elif spell == "Drain":
				mana -= 73
				if mana < 0: return "OOM"				
				bossHP -= 2
				playerHP += 2
			if bossHP <= 0:
				return True
			turn = "boss"
		elif turn == "boss":
			#print("Boss turn")
			playerHP = playerHP - (bossDmg - 7) if shield else playerHP - bossDmg
			turn = "player"
			if playerHP <= 0:
				return False

		if shield_timer == 0: shield = False
		if poison_timer == 0: poison = False
		if recharge_timer == 0: recharge = False

depth = 9
spells = {"Magic Missile": 53, "Drain": 73, "Shield": 113, "Poison": 173, "Recharge": 229}
castlist = list(product(spells,repeat=depth))

mincost = 9999
for cast in castlist:
	manacost = sum(spells[spell] for spell in cast)
	if fight(list(cast)) == True:
		mincost = min(mincost, manacost)
print(mincost)