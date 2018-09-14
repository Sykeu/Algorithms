#This program inputs an Array A[0: (n - 1)] and outputs A[0: (n - 1)] with all it's elements sorted in ascending order.
#This program uses recursive quick sort to sort the elements of A[0: (n - 1)].

#This function partitions the array A[l:u] such that for all  x < p, A[x] <= A[u] and for all x > p, A[x] > A[u] 

def partition( A, l, u):
	p = u - 1
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

	p = i

	A[p], A[u] = A[u], A[p]

	return p

#This function sorts the array using the quick sort algorithm.
def q_sort( A, l, u):

	# Base case is when we have only one element; we dont need to do anything

	if( l < u):
		# induction step is that we know how to solve the problem that is half its size or smaller.
		p = partition(A, l, u)	

		#Loop Invariant: p gives the correct place of the element A[u] in the sorted list.
		q_sort(A, l, p - 1)
		q_sort(A, p + 1, u)

#Program:-
n = input("Enter size of the array: ")

A = n * []

#Input:
print "Enter elements of the array:"
for i in range(n):
	A.append( input() )

print "The Array A is: ",
print A

#Initializations:
l = 0
u = n - 1

#Function call:
q_sort(A, l, u)

#Output:
print "The sorted array is: ", A
