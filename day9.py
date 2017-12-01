from itertools import permutations

lens = []

with open("day9") as file:
	for line in file:
		lens.append(line.strip().split(" = ")[0].split(" to ") + [int(line.strip().split(" = ")[1])])

cities = set([length[0] for length in lens] + [length[1] for length in lens])


dists = []

for perm in permutations(cities):
	dist = 0
	step = len(perm)
	while step > 1:
		for data in lens:
			if perm[-step] in data and perm [(-step)+1] in data:
				dist += data[2]
				break
		step -= 1	
	dists.append(dist)

print(max(dists))