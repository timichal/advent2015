field = []
with open("day18") as file:
	for line in file:
		field.append(line.strip())

field[0] = "#"+''.join(field[0][1:-1])+"#"
field[len(field)-1] = "#"+''.join(field[len(field)-1][1:-1])+"#"

def animate(field, broken=0):

	newfield = []
	for x, row in enumerate(field):
		newrow = ""
		for y, light in enumerate(row):
			neighbors = 0
			
			if x-1 >= 0:
				if field[x-1][y] == "#": neighbors += 1
			if x+1 < len(field):
				if field[x+1][y] == "#": neighbors += 1
			if y-1 >= 0:
				if field[x][y-1] == "#": neighbors += 1
			if y+1 < len(field):
				if field[x][y+1] == "#": neighbors += 1
			if x-1 >= 0 and y-1 >= 0:
				if field[x-1][y-1] == "#": neighbors += 1
			if x-1 >= 0 and y+1 < len(field):
				if field[x-1][y+1] == "#": neighbors += 1
			if x+1 < len(field) and y-1 >= 0:
				if field[x+1][y-1] == "#": neighbors += 1
			if x+1 < len(field) and y+1 < len(field):
				if field[x+1][y+1] == "#": neighbors += 1

			if light == "#":
				if neighbors == 2 or neighbors == 3:
					newrow += "#"
				else:
					newrow += "."
			elif light == ".":
				if neighbors == 3:
					newrow += "#"
				else:
					newrow += "."
		newfield.append(newrow)

	if broken:
		newfield[0] = "#"+''.join(newfield[0][1:-1])+"#"
		newfield[len(newfield)-1] = "#"+''.join(newfield[len(newfield)-1][1:-1])+"#"

	return newfield

for i in range(100):
	field = animate(field, broken=1)

countable_field = ''.join(field)
litcount = 0
for light in countable_field:
 	if light == "#":
 		litcount += 1 
print(litcount)