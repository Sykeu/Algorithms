#Input: An array A[0 : (n-1)]
#Output: Sorted array A with the number x in the correct place

def insertion(A, h):
	i = h

	while i != 0 and A[i - 1] > A[i]:
		A[i - 1], A[i] = A[i], A[i - 1]
		i -= 1

n = input("Enter size of the array: ") #n denotes the size of the array

A = n * []

#Input:-
print "Enter elements of the array:"
for i in range(n):
	A.append( input() )

print "The Array A is: ", A

#Initialization:
#All elements in the array till the index i are sorted.
i = 0 #Since one element by itself is sorted.

#Loop Invariant:-
#The elements that were in A[0:i] continue to remain between 0 and i after every iteration of the loop and are sorted.

#Loop:-
while i != n - 1:	# Bound function: [(n - 1) - i] > 0; the loop breaks once i becomes equal to (n - 1) [ {( n - 1) - i} < 0].
	insertion(A, i + 1)	#Making progress, increasing the size of the array.
	i += 1	 #Maintaining definition.


#Output:-
print A
