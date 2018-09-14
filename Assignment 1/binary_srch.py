# Input: A sorted Array A[0 : (n-1)] and a number x
# Output: The (rightmost) occurence of x in A (if it at all it is there)

# We use the paradigm of Decrease and Conquer.
import math

# l and h point to the start and end of the array (to be done) respectively.
# m = Ceil( (l + h) / 2 )

# Input:-
n = input("Enter number of elements in the (sorted) array: ") #Size of the array from the user

A = [] * n

print "Enter elements of the array (in sorted order):-"

for i in range( n ):
	A.append( input() )

x = input("Enter the element you want to search for: ")

# Initializing:-
l = 0
h = (n - 1)

# Loop Invariant:-
# If x belongs to A <=> x belongs to A[l:h]

# Loop:-
while l != h:	# Bound function: (h - l) > 0; The loop breaks once the l becomes equal to h [ ( h - l) = 0].

	m = int (math.ceil( (l + h) / 2.0 )) # Maintaining Definition

	if A[m] > x:
		h = m - 1	# Making progress
	else:
		l = m		# Making progress

# Output:-
if A[l] == x:	# When l == h, => x belongs to A[l:l] = A[l]
	print "Rightmost occurence of ", x, " in A is ", l
else:
	print x, " not found in A"
