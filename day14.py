# name, speed, secs, restsecs
reindeer = []

with open("day14") as file:
	for line in file:
		deer = []
		deer.append(line.split(" ")[0])
		deer.append(int(line.split(" km/s")[0][-2:].strip()))
		deer.append(int(line.split(" seconds")[0][-2:].strip()))
		deer.append(int(line.split(" rest for ")[1][:3].strip()))
		seccounter = 0
		deer.append(seccounter)
		state = "fly" #fly, rest
		deer.append(state)
		score = 0
		deer.append(score)
		score_part2 = 0
		deer.append(score_part2)
		reindeer.append(deer)

#reindeer = [['Comet',14,10,127,0,'fly',0,0], ['Dancer',16,11,162,0,'fly',0,0]]
print(reindeer)		
sec = 1
while sec <= 2503:
	#part 1
	for deer in reindeer:
		if deer[5] == 'fly':
			if deer[4] != deer[2]:
				deer[6] += deer[1]
				deer[4] += 1
			if deer[4] == deer[2]:
				deer[5] = 'rest'
				deer[4] = 0
		elif deer[5] == 'rest':
			if deer[4] != deer[3]:
				deer[4] += 1
			if deer[4] == deer[3]:
				deer[5] = 'fly'
				deer[4] = 0

	# part 2
	maxdist = max([deer[6] for deer in reindeer])
	for deer in reindeer:
		if maxdist == deer[6]: 
			deer[7] += 1
	sec += 1

print(reindeer)
