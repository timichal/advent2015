from itertools import combinations
containers = []

with open("day17") as file:
	for line in file:
		containers.append(int(line.strip()))

valid = 0
for contno in range(1,len(containers)+1):
	for i in combinations(containers,contno):
		if sum(i) == 150:
			print(i)
			valid += 1
print(valid)