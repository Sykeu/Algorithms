#Input: String A[1:n]
#Output: reversed string (of A[1:n])

l = raw_input("Enter a String: ")
s = list(l)

#n denotes the size of the array
n = len(s) - 1

#i denotes the number of swaps made

#Initialize
i = 0	#At the start, number of swaps made are 0

#Loop Invariant:- The string remains a permutation of initial input.
#Loop:-
while i <= (n/2):	# Bound function: [ (n / 2) - i ] >= 0; the loop breaks once the number of swaps, i, becomes equal to half the number of elements in array, n / 2).

	s[i], s[n-i] = s[n-i], s[i] #Making progress
	i += 1	#Maintaining definition

#Output:
print "Reversed string is: " + str(s) + "\nNumber of swaps made are: ", i

