import random
import time

def partition( A, I, l, u, r):
	"""
		mid = int ( ( l + u ) / 2 )
	
		if ( A[l] > A[u] ):
			A[l], A[u] = A[u], A[l]
			I[l], I[u] = I[u], I[l]

		if ( A[l] > A[mid]):
			A[l], A[mid] = A[mid], A[l]
			I[l], I[mid] = I[mid], I[l]

		if( A[mid] < A[u] ):
			A[mid], A[u] = A[u], A[mid]
			I[mid], I[u] = I[u], I[mid]
	"""
	x = A[u]
		
	i = l
	j = u - 1

	while i <= j:
		
		if (A[i] - A[u]) < r or (A[i] - A[u]) > -r:
			if ( I[ i ] * I[ u ] ) == 0:
				I[ i ] = I[ u ] = 0

		if (A[j] - A[u]) < r or (A[j] - A[u]) > -r:
			if ( I[ j ] * I[ u ] ) == 0:
				I[ j ] = I[ u ] = 0
		if A[i] <= x:
			i += 1
                
		elif A[j] > x:
			j -= 1

		else:
			A[i], A[j] = A[j], A[i]
			I[i], I[j] = I[j], I[i]

			i += 1
			j -= 1

	A[i], A[u] = A[u], A[i]
	I[i], I[u] = I[u], I[i]

	return i

def k_smallest(k, A, I, l, u, r):

	p = partition(A, I, l, u, r)

	if p == k:
		return ( A[p] )
	elif p < k:
		return k_smallest( k, A, I, p + 1, u, r)
	else:
		return k_smallest( k, A, I, l, p - 1, r)


for n in range(10, 20, 1):

	A = n * []

	rng = n

	for i in range( n ):
		A.append(  int ( random.uniform( 1, rng) ) )

	
	k = int( random.uniform(0, n - 1) )


	I = n * [1]

	I[ int (random.uniform( 0, n - 1))] = 0

	print ( A )
	print ( I )

	r = rng * 0.2

	k_smallest( k, A, I, 0, n - 1, r)

	print ( "Infected: ", I)
	inf = 0

	for i in I:
		if i == 0:
			inf = inf + 1

	print( n, " ", inf )
