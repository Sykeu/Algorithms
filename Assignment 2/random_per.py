#Input: An array A[0 : n-1]
#Output: A random permutation of the elements of A.

import random

DATA = 0
KEY = 1

def partition( A, l, u):
	p = u - 1
	x = A[u][KEY]
	
	i = l
	j = u - 1

	while i <= j:
		if A[i][KEY] <= x:
			i += 1	#Maintaining definition
		elif A[j][KEY] > x:
			j -= 1	#Maintaining definition
		else:
			A[i], A[j] = A[j], A[i]	#Making progress
			i += 1		#Maintaining definition
			j -= 1		#Maintaining definition	

	p = i

	A[p], A[u] = A[u], A[p]

	return p

#This function sorts the array using the quick sort algorithm.
def qsort( A, l, u):

	# Base case is when we have only one element; we dont need to do anything

	if( l < u):
		# induction step is that we know how to solve the problem that is half its size or smaller.
		p = partition(A, l, u)	

		#Loop Invariant: p gives the correct place of the element A[u] in the sorted list.
		qsort(A, l, p - 1)
		qsort(A, p + 1, u)

n = int( input("Enter size of the array: ") )

A = n * []

print ("Enter elements of the array: ")

p = n * n * n

for i in range( n ):

	A.append( [ int ( input() ), random.uniform(1, p) ] )

print (A)

qsort( A, 0, n - 1)

print ( "Random permutation: ", [ A[i][DATA] for i in range(n) ] )
