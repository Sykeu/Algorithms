# Input: A sorted array A[0: (n-1)] and a number x
# Output: Sorted array A with the number x in the correct place

n = input("Enter size of the array: ") # n denotes the size of the array

A = []

print "Enter elements of the sorted array:"
for i in range(n):
	A.append( input() )

A.sort()	# To insure the array is infact sorted

print "The Array A is: ",
for i in range(n):
	print A[i], " ",

x = input("\nEnter a number: ")

A.append(x) # inserting the number x at the end of the array

n += 1 # Since the size of the array increased by 1 after inserting x

# The variable i denotes the position of x

# initialization
i = n - 1	# initially the number x is in the (n-1)th postion

# Loop Invariant is the fact that all numbers between 0 and n continue to remain, need not be in same order.

# Loop:-
while i != 0 and A[i - 1] > A[i]:	# Bound function: i > 0; the loop breaks when i becomes 0.

	A[i], A[i - 1] = A[i - 1], A[i]	# Making progress
	i -= 1	# Mainting the definition of i


# Output:
print "The Array A now is: ", A
