#Finding the number of primes between 1 and 'n' - given by user.
#Using Sieve of Eratosthenes

import math as m

n = input("Enter a number: ")

sq_n = (int) (m.sqrt(n) + 1)

prime = (n + 1) * [ True ]

p_count = 0

for i in range (2, sq_n):
	
	if prime[i]:
		j = (i * i)

		while j <= n:
			prime[j] = False
			j = j + i

		p_count += 1

while( i <= n):
	if(prime[i]):
		p_count += 1

	i += 1


print "count = ", p_count
