from itertools import permutations
from functools import reduce
packages = []
with open("day24") as file:
	for line in file:
		packages.append(int(line.strip()))

def equalizer(packages):
	grweight = int(sum(packages)/4)
	packs = 4
	packages = permutations(packages,packs)
	for package in packages:
		if sum(package) == grweight:
			print(package, reduce((lambda x, y: x*y), package))

equalizer(packages)