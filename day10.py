def lookandsay(string):
	newstring = ""

	prevchar = ""	
	count = 0
	for char in string:
		if char == prevchar:
			count += 1
		else:
			if count != 0: newstring += str(count) + prevchar
			prevchar = char
			count = 1
	newstring += str(count) + prevchar

	return newstring

string = "1113222113"

for i in range(50):
	string = lookandsay(string)

print(len(string))