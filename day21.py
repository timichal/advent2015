from itertools import product

def stockshop():
	stock = {}
	with open("day21") as file:
		for line in file:
			if ":" in line:
				category = line.split(":")[0]
				items = []
			elif line != "\n":
				item = line.strip().split("  ")
				item_clean = []
				item_clean.append(item[0])
				for col in item[1:]:
					if col != "":
						item_clean.append(int(col.strip()))
				items.append(item_clean)
			else:
				stock[category] = items
		stock[category] = items
	return stock

def fight(playerDmg=0, playerArmor=0):
	playerHP = 100
	bossHP = 104
	bossDmg = 8
	bossArmor = 1

	while True:
		# player turn
		bossHP = bossHP - (playerDmg-bossArmor)
		if bossHP <= 0:
			return True	

		# boss turn
		playerHP = playerHP - (bossDmg-playerArmor)
		if playerHP <= 0:
			return False

def equip_combinations(stock):
	combinations = []
	# 1 weapon, 0 armor, 0 rings
	combinations += stock["Weapons"]
	# 1 weapon, 0 armor, 1 ring
	combinations += product(stock["Weapons"], stock["Rings"])
	# 1 weapon, 0 armor, 2 rings
	combo_prefilter = product(stock["Weapons"], stock["Rings"], stock["Rings"])
	for combination in combo_prefilter:
		if combination[1] != combination[2]:
			combinations.append(combination)
	# 1 weapon, 1 armor, 0 rings
	combinations += product(stock["Weapons"], stock["Armor"])
	# 1 weapon, 1 armor, 1 ring
	combinations += product(stock["Weapons"], stock["Armor"], stock["Rings"])
	# 1 weapon, 1 armor, 2 rings
	combo_prefilter = product(stock["Weapons"], stock["Armor"], stock["Rings"], stock["Rings"])
	for combination in combo_prefilter:
		if combination[2] != combination[3]:
			combinations.append(combination)
	return combinations

def try_equipment(equipment):
	for equip in equipment:
		if type(equip) == list:
			yield [equip[1], equip [2], equip[3]]
		if type(equip) == tuple:
			yield [sum(i) for i in list(zip(*equip))[1:]]
		

stock = stockshop()

equipment = equip_combinations(stock)

mingold = 999
for equip in try_equipment(equipment):
	if fight(equip[1],equip[2]):
		mingold = min(mingold, equip[0])

print(mingold)

# part 2
maxgold = 0
for equip in try_equipment(equipment):
	if not fight(equip[1],equip[2]):
		maxgold = max(maxgold, equip[0])

print(maxgold)