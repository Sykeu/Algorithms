#Input: An array A[ 0: (n - 1) ]
#Output: A random permutation of A[ 0: (n - 1) ]

import random

n = int( input("Enter size of the array: " ) ) 

A = n * []

print ("Enter elements of the array:")

for i in range( n ):
	A.append( int( input() ))

for i in range( n ):
	k = int ( random.uniform( i, (n - 1) ) )

	A[i], A[k] = A[k], A[i]

print ("Random permutation: ", A)
