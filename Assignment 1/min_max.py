# Input:- An Array of numbers A[0:n]
# Output:- Min and Max of all the numbers in the array A


def min_max(A, l, h):
	
	if( l < (h-1) ):	# ==> We have more than two elements.
	
		# Induction step is that we can solve the problem half its size.

		mi1, ma1 = min_max(A, l, (l + h)/2)	# making progress
		mi2, ma2 = min_max(A, ((l + h)/2) + 1, h) # making progress

		mi = min(mi1, mi2) # maintaining
		ma = max(ma1, ma2) # maintaining

		return mi, ma

	else:	# Base case:- we can find the min and max for two or lesser elements.
		if A[l] > A[h]:
			return A[l], A[h]
		else:
			return A[h], A[l]

# Input:-
n = input("Enter size of the array: ")

print "\nEnter the elements of the array:-"

A = n * []

for i in range(n):
	print "Element A[" , i, "]: ",
	A.append( input() )


mi, ma = min_max(A, 0, n-1)

# Output:-
print mi, ma
