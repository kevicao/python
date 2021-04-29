class Node(object):
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None

def collect(node, data, depth = 0):
	if not node:
		return None

	if depth not in data:
		data[depth] = []

	data[depth].append(node.val)

	collect(node.left, data, depth+1)
	collect(node.right, data, depth+1)

def avg_by_depth(node):
	data = {}
	collect(node, data)

	result = []

	i = 0
	while i in data:
		nums = data[i]
		avg = sum(nums)/len(nums)
		result.append(avg)
		i += 1

	return result

#######improve the space

def collect(node, data, depth = 0):
	if not node:
		return None

	if depth not in data:
		data[depth] = (node.val, 1)
	else:
		data[depth] = (data[depth][0] + node.val, data[depth][1] + 1)

	# data[depth].append(node.val)

	collect(node.left, data, depth+1)
	collect(node.right, data, depth+1)

def avg_by_depth(node):
	data = {}
	collect(node, data)

	result = []

	i = 0
	while i in data:
		# nums = data[i]
		avg = data[i][0]/data[i][1]
		result.append(avg)
		i += 1

	return result