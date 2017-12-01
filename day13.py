from itertools import permutations
relations = []
with open("day13") as file:
	for line in file:
		line = line.strip().split()
		person = line[0]
		units = int(line[3])
		if line[2] == "lose": units = -units
		person2 = line[-1][:-1]
		relations.append((person, person2, units))

people = list(set(relation[0] for relation in relations))

# adding myself for part 2
people.append("Me")
relations.extend([("Me", person, 0) for person in people])
relations.extend([(person, "Me", 0) for person in people])

maxscore = 0

for seating in list(permutations(people,len(people))):
	score = 0
	for position, person in enumerate(seating):
		for relation in relations:
			if person == relation[0]:
				if seating[position-1] == relation[1]:
					score += relation[2]
				if position != len(seating)-1:
					if seating[position+1] == relation[1]:
						score += relation[2]
				else:
					if seating[0] == relation[1]:
						score += relation[2]
	maxscore = max(maxscore, score)
print(maxscore)