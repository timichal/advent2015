instructions = []
with open("day23") as file:
	for line in file:
		instructions.append(line.strip())
print(instructions)

register = {"a": 1, "b": 0}

startpoint = 0
while True:
	for instruction in instructions[startpoint:]:
		print(instruction, end=" ")
		if instruction.startswith("inc"): 
			register[instruction[4]] += 1
		if instruction.startswith("jmp"):
				startpoint = instructions.index(instruction) + int(instruction[-3:])
				break			
		if instruction.startswith("jio"):
			if register[instruction[4]] == 1:
				startpoint = instructions.index(instruction) + int(instruction[-3:])
				break
		if instruction.startswith("jie"):
			if register[instruction[4]] % 2 == 0:
				startpoint = instructions.index(instruction) + int(instruction[-3:])
				break
		if instruction.startswith("hlf"):
			register[instruction[4]] *= 0.5
		if instruction.startswith("tpl"):
			register[instruction[4]] *= 3
	if startpoint >= len(instructions):
		break
print(register)