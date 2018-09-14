# Input: two positive numbers 'a' and 'b'
# Output: integers q and r such that a = bq + r and 0 <= r < b

a = input("Enter two positive integers.\na = ")
b = input("b = ")

# q and r variables that satisfy the equation a = bq + r and 0 <= r < b

# Initialization
q = 0	# Initially, for satisfying the equation,
r = a	# We put q = 0 and r = a so that a = b* q(=0) + r (=a) = a

# Loop Invariant is the equation a = bq + r
# Loop:-
while r > b:	# Bound function: (r - b) > 0; the loop breaks once r becomes lesser than b [ (r - b) < 0].
	r = r - b	# Maintaining definition
	q = q + 1	# of q and r and also making progress.

# Output:
print "Quotient: ", q
print "Remainder: ", r
