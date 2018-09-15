DATA = 0
LEFT = 1
RIGHT = 2
PARENT = 3

def push(stk, element):

	if stk == None:
		stk = [element]
	else:	
		stk.append(element)
	
	return stk

def pop(stk):
	top = None

	if stk != None and stk != []:
		top = stk[ len( stk) - 1]
		del stk[ len( stk) - 1]

	return stk, top

def insert(root, element):
	
	if root == None:
		root = [element, None, None, None]
		
		return root
	else:

		while root != None:

			if root[DATA] <= element:
				
				if root[RIGHT] == None:

					root[RIGHT] = [element, None, None, root]

					break
				else:
					root = root[RIGHT]
			else:
				if root[LEFT] == None:

					root[LEFT] = [element, None, None, root]
					break
				else:
					root = root[LEFT]

		while root[PARENT] != None:
			root = root[PARENT]

		return root

def inorder(root):

	stk = []

	while root != None or stk != []:

		if root != None:
			stk = push(stk, root)
			root = root[LEFT]
		else:
			stk, root = pop(stk)

			print root[DATA]
		
			root = root[RIGHT]
'''
def postorder(root):

	stk = []

	while root != None or stk != []:

		if root != None:
			stk = push(stk, root)
			root = root[LEFT]
		else:
			stk, root = pop(stk)

			if root[RIGHT] != None:
				root = root[RIGHT]'''
root = None

ch = 'y'

while ch == 'y':
	print "\n\n1. Insert element.\n2. Print tree.\n3. Pre-order.\n4. In-order.\n5. Post-order.\6. Exit."
	
	i = input("Enter choice (1 - 5): ")

	if i == 6:

		ch = 'n'

	elif i == 1:

		d = input("Enter number you want to insert: ")
		root = insert(root, d)

	elif i == 2:

		print root

	#elif i == 3:

	#	preoder(root)

	elif i == 4:

		inorder(root)

	#elif i == 5:

	#	postorder(root)
