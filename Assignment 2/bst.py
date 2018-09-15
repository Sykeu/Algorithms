DATA = 0
LEFT = 1
RIGHT = 2

def insert( root, element):
	if root == None:
		root = [element, None, None]

	else:
		if root[DATA] <= element:

			root[RIGHT] = insert(root[RIGHT], element)

		else:

			root[LEFT] =  insert(root[LEFT], element)

	return root

def preoder( root):
	
	if root != None:

		print root[DATA]

		preorder( root[LEFT] )
		preorder( root[RIGHT] )

def inorder( root):
	
	if root != None:

		inorder( root[LEFT] )

		print root[DATA]

		inorder( root[RIGHT] )

def postorder(root)

	if root != None:
	
		postorder( root[LEFT] )
		postorder( root[RIGHT] )

		print root[DATA]

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

	elif i == 3:

		preoder(root)

	elif i == 4:

		inorder(root)

	elif i == 5:

		postorder(root)
