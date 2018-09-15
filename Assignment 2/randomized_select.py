import random
import time

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
		return k_smallest( k, A, p + 1, u, n)
	else:
		return k_smallest( k, A, l, p - 1, n)

def k_smallest_iter(k, A, l, u, n):

	while l < u:
		if n == 0:
			p = partition(A, l, u)
		elif n == 1:
			p = partition_rand(A, l, u)
		elif n == 2:
			p = partition_med(A, l, u)

		if p == k:
			break
		elif p < k:
			l = p + 1
		else:
			u = p - 1

	return ( A[p] )

print ("\n\nProgram prints the k-th smallest number: ")

n = int( input ("Enter size of the array: ") )

A = n * []

r = int( input( ("Enter range: " ) ) )

for i in range( n ):
	A.append(  int ( random.uniform(1, r ) ) )

k = int( input( ("Enter value for k (lesser than n): ") ) )

k = k - 1		# Array indices start from 0 and go till n - 1

print (A)

for i in range( 3 ):
	start = time.clock()

	j = ( k_smallest(k, A, 0, n - 1, i) )

	print (j)

	print( "Time taken: ", time.clock() - start)
