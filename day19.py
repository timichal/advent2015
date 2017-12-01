replacements = []

with open("day19") as file:
	for line in file:
		if "=>" in line:
			replacement = line.strip().split(" => ")
			replacements.append(replacement)
		elif line.strip() != "":
			molecule = line

generated_molecules = []

for replacement in replacements:
	for position in range(len(molecule)):
		if molecule[position:position+len(replacement[0])] == replacement[0]:
			generated_molecules.append(molecule[0:position] + replacement[1] + molecule[position+len(replacement[0]):])
generated_molecules = set(generated_molecules)
#print(len(generated_molecules))

#part 2

def defabricate(molecule):
	rules = [0]
	target = "e"
	molecule_mod = molecule
	step = 0

	while molecule_mod != target:
		current_replacement = replacements[rules[step]]
		if current_replacement[1] in molecule_mod:
			molecule_mod = molecule_mod.replace(current_replacement[1], current_replacement[0], 1) 
			step += 1
			rules.append(0)
			print(molecule_mod)
		else: 
			rules[step] += 1
	return len(rules)-1

replacements.sort(key=lambda x: len(x[1]), reverse=True)
print(replacements)
generated_molecules = defabricate(molecule)
print(generated_molecules)

