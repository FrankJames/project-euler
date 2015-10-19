# PROBLEM DESCRIPTION
# Starting in the top left corner of a 2x2 grid, and only being able 
# to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20x20 grid?

# NOTES: 
# So we can model this using a tree, but there is a maximum depth to the right and left sides

# Basically, we need to find the number of different sequences to get to 
# X=10 and Y=10, by incrementing each bucket by one

from Queue import Queue

class XYTree:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.right = None
		self.left = None

	def createXNode(self):
		return XYTree(self.x + 1, self.y)

	def createYNode(self):
		return XYTree(self.x, self.y + 1)

	def addNextLayerWithLimit(self, limit):
		if self.right is None and self.left is None:
			self.right = self.createXNode()
			self.left = self.createYNode()
		else:
			if self.x < limit:
				self.right.addNextLayerWithLimit(limit)
			if self.y < limit:
				self.left.addNextLayerWithLimit(limit)

	def __str__(self):
		return "x: " + str(self.x) + ", y: " + str(self.y)

def findPossibilitiesInSquareGrid(d):
	a = XYTree(0, 0)
	# the only amount of moves that will end at the correct coordinate
	# is 2 times the grid length, because we are moving from the top left
	# to the bottom right addNextLayerWithLimit
	for x in range(2 * d):
		a.addNextLayerWithLimit(d)
		print "created layer "  + str(x)
	print "finished creating tree, now traversing it"

	# BFS to find only the nodes that are at the correct end coordinates
	# and then places those nodes into a bucket
	q = Queue()
	q.put(a)
	endBucket = []
	while not q.empty():
		node = q.get()
		if node.x == d and node.y == d:
			endBucket.append(node)
		if node.right is not None and node.left is not None:
			q.put(node.right)
			q.put(node.left)
	return len(endBucket)

print findPossibilitiesInSquareGrid(10)

# def paths(x):
# 	if x <= 0:
# 		return 0
# 	else:
# 		return 2 ** x + (paths(x-1) * paths(x-2))

# print paths(1)
# print paths(2)
# print paths(3)
# print paths(4)
# print paths(5)

# a = XYTree(0, 0)
# print a
# a.addNextLayer()
# print a.right
# print a.left
# a.addNextLayer()
# print a.right
# print a.right.right
# print a.right.left
# print a.left.right
# print a.left.left


