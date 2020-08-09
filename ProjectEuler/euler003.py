import math

def get_biggest_prime_factor(n):
	while n%2 == 0:
		n = n/2

	primed = False
	while not primed:
		primed = True
		for i in range(3, int(math.ceil(math.sqrt(n)))+1, 2):
			if n%i == 0:
				n = n/i
				primed = False
				break

	return int(n)
			

t = int(input())

for _ in range(t):
	n = int(input())
	print(get_biggest_prime_factor(n))
	