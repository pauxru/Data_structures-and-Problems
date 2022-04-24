
# Tutorial from: https://www.youtube.com/watch?v=tWVWeAqZ0WU&ab_channel=freeCodeCamp.org

"""
append() - is used to add elements to the top of the stack
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
insert(-1, item) - inserts item at the end of the list to form a queue
"""

graph = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}


# The iterative approach of the depth first
def depthFirstPrint(graph, source):
	stack = [source]

	while len(stack) > 0:
		current = stack.pop()
		print(current)

		for neighbor in graph[current]:
			stack.append(neighbor)


# depthFirstPrint(graph, 'a') # Answer: acebdf


# The iterative approach of the breadth first
def breadthFirstPrint(graph, source):
	queue = [source]

	while len(queue) > 0:
		current = queue.pop()
		print(current)

		for neighbor in graph[current]:
			queue.insert(-1, neighbor)


# breadthFirstPrint(graph, 'a')


# We want to check if there is a path between two given nodes in the graph
# Using the depth first approach recurssively
def has_path(graph, src, dst): # src - source/starting point and dst is destination
	stack = [src]

	if src == dst:
		print("Yes")
		return True

	for neighbor in graph[src]:
		if has_path(graph, neighbor, dst) is True:
			return True
	print("No")
	return False


# has_path(graph, 'e', 'd')

# Using the depth first approach iteratively
def hasPath(graph, src, dst):
	stack = graph[src]

	while len(stack) > 0:
		current = stack.pop()
		if current == dst:
			print("Yes")
			return True
		for neighbor in graph[current]:
			stack.append(neighbor)
	print("No")
	return False

# hasPath(graph, 'e', 'd')


# Using the breadth first approach iteratively
def hasPath_breadth(graph, src, dst):
	queue = graph[src]

	while len(queue) > 0:
		current = queue.pop()
		if current == dst:
			print("Yes")
			return True
		for neighbor in graph[current]:
			queue.insert(-1, neighbor)
	print("No")
	return False


# hasPath_breadth(graph, 'a', 'd')

# Unidirectional graphs
# given the edges as the following. These are the line connection of the nodes
edges1 = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]

edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]


# We need to build the graph here
def build_graph (edges):
	graph = {}

	for edge in edges:
		[a, b] = edge
		if a not in graph: graph[a] = []
		if b not in graph: graph[b] = []
		graph[a].append(b)
		graph[b].append(a) # since this is a undirected graph
	return graph


# We are also checking if a node has been visited to prevent infinite loop
def undirectedPath(graph, src, dst, visited):

	if src == dst:
		return True
	if src in visited: return False
	visited.add(src)

	for neighbor in graph[src]:
			if undirectedPath(graph, neighbor, dst, visited) is True:

				return True

	return False


# visited = set()
# print(build_graph(edges1))
# print("Has path: ",undirectedPath(build_graph(edges1), 'k', 'l', visited))  # -> true
# print("Path: ",visited)




# Connected components

components = ({
	0: [4, 7],
	1: [],
	2: [],
	3: [6],
	4: [0],
	6: [3],
	7: [0],
	8: []
})  # -> 5


def connected_components_count(components):
	visited = set()
	cnt = 0
	for node in components:
		# print(node)
		if explore(components, node, visited) is True:
			cnt +=1
	return cnt


def explore(graph, current, visited):
	if current in visited: return False
	visited.add(current)
	for neighbor in graph[current]:
		explore(graph, neighbor, visited)
	return True

# print(connected_components_count(components))


largest_component = ({
	3: [],
	4: [6],
	6: [4, 5, 7, 8],
	8: [6],
	7: [6],
	5: [6],
	1: [2],
	2: [1]
})  # -> 5
# Largest component in a graph


def largest_components(graph):
	visited = set()
	longest = 0
	for node in graph:
		size = explore_size(graph, node, visited)
		if size > longest: longest = size

	return longest


def explore_size(graph, node, visited):
	if node in visited: return 0

	visited.add(node)
	size = 1
	for neighbor in graph[node]:
		size += explore_size(graph, neighbor, visited)

	return size

# print(largest_components (largest_component))



# Shortest path between nodes

edges1 = [
	['a', 'c'],
	['a', 'b'],
	['c', 'b'],
	['c', 'd'],
	['b', 'd'],
	['e', 'd'],
	['g', 'f']
]


def shortest_path (edges, nodeA, nodeB):
	graph = build_graph1(edges)
	visited = set([nodeA])
	queue = [[nodeA, 0]]

	while len(queue) > 0:
		[node, distance] = queue.pop(0)
		if node == nodeB: return distance

		for neighbor in graph[node]:
			if neighbor not in visited:
				visited.add(neighbor)
				queue.append([neighbor, distance + 1])
	return -1


def build_graph1(edges):
	graph = {}

	for edge in edges:
		[a, b] = edge
		if a not in graph: graph[a] = []
		if b not in graph: graph[b] = []

		graph[a].append(b)
		graph[b].append(a)
	return graph


# print(shortest_path(edges1, 'b', 'g')) # -> -1


#Island count

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


def island_count(grid):
	r= 0
	c= 0
	count = 0
	visited = set()
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if explore_island(grid, r, c, visited) is True:
				count += 1
	return count


def explore_island(grid, r, c, visited):

	rowInbounds = 0 <= r and r < len(grid)
	colInbounds = 0 <= c and c < len(grid[0])
	if not rowInbounds or not colInbounds: return False

	if grid[r][c] == 'W': return False

	pos = str(r) + ',' + str(c)
	if pos in visited: return False
	visited.add(pos)

	explore_island(grid, r - 1, c, visited)
	explore_island(grid, r + 1, c, visited)
	explore_island(grid, r, c - 1, visited)
	explore_island(grid, r, c + 1, visited)

	return True


print(island_count(grid))










