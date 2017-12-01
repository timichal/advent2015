string = "hepxxzaa"

def firstreq(string):
	ordstr = [ord(char) for char in string]

	for k in range(len(ordstr)-2):
		if ordstr[k+2] == ordstr[k+1] + 1 == ordstr[k] + 2:
			return True

def secondreq(string):
	if any(char in string for char in ["i", "o", "l"]):
		return False
	else:
		return True

def thirdreq(string):
	for k in range(len(string)-1):
		if string[k] == string[k+1]: 
			for i in range(len(string)-k-3):
				if string[i+k+2] == string[i+k+3]:
					return True

while True:
	if firstreq(string) and secondreq(string) and thirdreq(string):
		break

	if string[-1] != "z":
		string = string[:-1] + chr(ord(string[-1])+1)
	else:
		zcount = 0
		while True:
			if all(char == "z" for char in string[-(zcount+1):]):
				zcount += 1
				if zcount == len(string):
					break
			else:
				break
		if zcount == len(string):
			string = "a" * (zcount+1)
		else:
			string = string[:-(zcount+1)] + chr(ord(string[-(zcount+1)])+1) + "a"*zcount

print(string)