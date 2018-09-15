import random
import time
from tqdm import tqdm

def partition( A, l, u):

	x = A[u]
		
	i = l
	j = u - 1

	while i <= j:
		if A[i] <= x:
			i += 1	#Maintaining definition
		elif A[j] > x:
			j -= 1	#Maintaining definition
		else:
			A[i], A[j] = A[j], A[i]	#Making progress
			i += 1		#Maintaining definition
			j -= 1		#Maintaining definition	

	A[i], A[u] = A[u], A[i]

	return i

def partition_rand( A, l, u):

	p = int( random.uniform(l, u) )
	
	A[u], A[p] = A[p], A[u]

	x = A[u]
	i = l
	j = u - 1

	while i <= j:
		if A[i] <= x:
			i += 1	#Maintaining definition
		elif A[j] > x:
			j -= 1	#Maintaining definition
		else:
			A[i], A[j] = A[j], A[i]	#Making progress
			i += 1		#Maintaining definition
			j -= 1		#Maintaining definition	

	A[i], A[u] = A[u], A[i]

	return i

def partition_med( A, l, u):

	mid = int ( ( l + u ) / 2 )
	
	if ( A[l] > A[u] ):
		A[l], A[u] = A[u], A[l]
	
	if ( A[l] > A[mid]):
		A[l], A[mid] = A[mid], A[l]

	if( A[mid] < A[u] ):
		A[mid], A[u] = A[u], A[mid]

	
	x = A[u]
		
	i = l
	j = u - 1

	while i <= j:
		if A[i] <= x:
			i += 1
		elif A[j] > x:
			j -= 1
		else:
			A[i], A[j] = A[j], A[i]
			i += 1
			j -= 1	

	A[i], A[u] = A[u], A[i]

	return i

def k_smallest(k, A, l, u, n):

	if n == 0:
		p = partition(A, l, u)
	elif n == 1:
		p = partition_rand(A, l, u)
	elif n == 2:
		p = partition_med(A, l, u)

	if p == k:
		return ( A[p] )
	elif p < k:
		k_smallest( k, A, p + 1, u, n)
	else:
		k_smallest( k, A, l, p - 1, n)

#print ("\n\nProgram prints the k-th smallest number: ")

#n = 10

for n in tqdm (range(10, 1000000, 1000) ):

	#n = int( input ("Enter size of the array: ") )

	A = n * []

	#r = int( input( ("Enter range: " ) ) )
		
	r = 10000

	for i in range( n ):
		A.append(  int ( random.uniform(1, r ) ) )

	#k = int( input( ("Enter value for k (lesser than n): ") ) )

	k = int ( random.uniform(1, n) )
	
	#print ( n )	
	#print ( k )

	k = k - 1		# Array indices start from 0 and go till n - 1

	print ( n, " ", k, " ", end = '')
#	print (n, " ", end = '')

	for i in range( 3 ):
		start = time.clock()

		k_smallest(k, A, 0, n - 1, i)

		print(time.clock() - start, " ", end = '')
	
	print()

#	if n < 10000:
#		n = n * 10
#	else:
#	n = n + 1000
