#This program implements recursive merge sort.

def merge( A, l,  h):

	C = (h - l) * []

	i = l
	j =  ( (l + h) / 2) +  1

	k = j

	while( i < k and j <= h):

		if( A[i] < A[j]):

			C.append( A[i])
			i += 1
		else:
			C.append( A[j])
			j += 1


	while(i < k):
		C.append( A[i])
		i += 1

	while(j <= h):
		C.append( A[j])
		j += 1

	j = 0

	while( l <= h):
		A[l] = C[j]
		j += 1
		l += 1

def m_sort(A, l, h):

	if l == h:	# Base case: we have only one element; nothing to do.
		return

	else:
		# Induction step is that we know to solve a problem half the size.

		m_sort( A, l, (l + h)/2)	# making progress
		m_sort(A, (l + h)/2 + 1, h)	# making progress

		merge(A, l, h)			# maintaining definition.


n = input("Enter number of elements in the array: ")

A = n * []

print "Enter elements in the array:-"

for i in range(n):
	A.append(input("Enter A[", i, "]: "))

print "The Array A is: ", A

m_sort(A, l, h)

print "Array A after merge sort: ", A
