#Input: An array A[1:n] and a number x
#Output: The array A, and j ;1 <= j <=n such that for all i < j, A[i] <=x and for i >= j, A[i] > x

n = input("Enter size of the array: ")

A = [] * n

#Input:-
print "Enter elements of the array:"
for i in range(n):
	A.append( input() )

print "The Array A is: ",
for i in range(n):
	print A[i], " ",

x = input("\nEnter a number: ")

#The variables i and j denote the beginning and end of the un-processed part of the array.

#Initialize
i = 0	
j = n - 1	#Since the entire array is un-processed at the start.

#Loop Invariant is the fact that all the elements in A[0: (i - 1)] are <= x and all the elements in A[(j + 1), (n - 1)] are > x
#Loop:-
while i <= j:	# Bound Function: (j - i) > 0;	The Loop breaks once i becomes greater than j [(j - i) < 0].
	print i, j
	if A[i] <= x:
		i += 1	#Maintaining definition
	elif A[j] > x:
		j -= 1	#Maintaining definition
	else:
		A[i], A[j] = A[j], A[i]	#Making progress
		i += 1		#Maintaining definition
		j -= 1		#Maintaining definition
		print A


#Output:-
print "The Array A now is: ",
for i in range(n):
	print A[i], " ",

print "\nThe value of j is: ", j
