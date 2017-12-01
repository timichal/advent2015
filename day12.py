def jsonunpacker(json):
	newjson = []

	for thing in json:
		if type(thing) == list:
			for member in thing:
				newjson.append(member)
		elif type(thing) == dict:
			if "red" not in thing.values():
				for value in thing.values():
					newjson.append(value)
		elif type(thing) == int:
			newjson.append(thing)
		elif type(thing) == str:
			pass
		else:
			print("oops")

	return newjson

import json
with open("day12.json") as file:
	for line in file:
		json = json.loads(line)

for i in range(8):
	json = jsonunpacker(json)

print(sum(json))