from functools import reduce
ingredients = []

with open("day15") as file:
	for line in file:
		if line.strip() != "":
			ingredient = []
			ingredient.append(line.split(":")[0])
			for i in range(5):
				ingredient.append(int(line.split(",")[i][-2:].strip()))
			ingredients.append(ingredient)

def mixtures(n, total):
    start = total if n == 1 else 0

    for i in range(start, total+1):
        left = total - i
        if n-1:
            for y in mixtures(n-1, left):
           		yield [i] + y
        else:
            yield [i]

totlist = []
for tup in mixtures(4,100):
	inglist = []
	for i, ingredient in enumerate(ingredients):
		inglist.append(list(map(lambda x: tup[i]*x,ingredient[1:])))
	inglist = [max(0,sum(x)) for x in zip(*inglist)]
	calories = inglist.pop()
	if calories == 500:
		totlist.append(reduce((lambda x, y: x*y), inglist))
print(max(totlist))

