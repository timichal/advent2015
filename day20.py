from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

num = 600000

while True:
	num += 1
	factorlist = list(filter(lambda x: x*50 >= num, sorted(list(factors(num)))))
	if sum(factorlist)*11 >= 29000000:
		print(num)
		break