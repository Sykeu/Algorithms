TRAVERSE = 1
PRINT = 0
DATA = 0
LEFT = 1
RIGHT = 2
PARENT = 3

def push( stk, element):
	stk.append( element )

	return stk

def pop( stk ):
	if stk == []:
		print ("Error Stack is empty!")
		return
	else:
		element = stk[ len( stk ) - 1]
		del stk[ len( stk ) - 1]

	return stk, element

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

def inorder( root ):

	#Loop Invariant:- The Stack contains the tuple of nodes we want to print or traverse and the action that needs
	#		  to be taken, i.e, traverse or print.

	stk = []
	
	stk = push( stk, [root, TRAVERSE])

	while  stk != []:
		stk, [node, action] = pop( stk )

		if node == None:
			continue
		elif action == TRAVERSE:
			stk = push( stk, [node[RIGHT], TRAVERSE])
			stk = push( stk, [node, PRINT])
			stk = push( stk, [node[LEFT], TRAVERSE])
		else:
			print ( node[DATA] )

def postorder( root ):

	#Loop Invariant:- The Stack contains the tuple of nodes we want to print or traverse and the action that needs
	#		  to be taken, i.e, traverse or print.

	stk = []

	stk = push( stk, [root, TRAVERSE])

	while stk != []:
		stk, [node, action] = pop( stk )

		if node == None:
			continue
		elif action == TRAVERSE:
			stk = push( stk, [node, PRINT])
			stk = push( stk, [node[RIGHT], TRAVERSE])
			stk = push( stk, [node[LEFT], TRAVERSE])
		else:
			print( node[ DATA ] )

def preorder( root ):

	#Loop Invariant:- The Stack contains the root of the subtrees we want to traverse.

	stk = []

	stk = push( stk, root)

	while stk != []:
		stk, node = pop( stk )

		if node == None:
			continue
		else:
			print ( node[DATA] )
			stk = push( stk, node[RIGHT] )
			stk = push( stk, node[LEFT] )

root = None

ch = 'y'

while ch == 'y':

	print ("\n\n1. Insert element.\n2. Print tree.\n3. Pre-order.\n4. In-order.\n5. Post-order.\n6. Exit.")
	
	i = input("Enter choice (1 - 5): ")

	if i == '6':
		ch = 'n'

	elif i == '1':

		d = input("Enter number you want to insert: ")
		root = insert(root, int(d))

	elif i == '2':

		print (root)

	elif i == '3':

		preorder(root)

	elif i == '4':

		inorder(root)

	elif i == '5':

		postorder(root)
