from queue import Queue
class Graph:  # using adjacency list
	def __init__(self, vertex=None, is_directed=False):
		self.list = {}
		self.is_directed = is_directed
		self.Time = 0
		self.vertex = vertex

	def add_vertex(self, vertex):
		if self.vertex == None:
			self.list[vertex] = []
		else:
			self.list[vertex] = []

	def print_list(self):  # print(self.list)
		for i in self.list:
			print(f"{i}-->{self.list[i]}")

	def add_edge(self, u, v):
		if self.checkedge(u, v) is False:
			return
		self.list[u].append(v)
		if self.is_directed is False:
			self.list[v].append(u)

	def remove_vertex(self, u):
		flag = False
		if u in self.list:
			self.list.pop(u)
			flag = True
		for i in self.list.keys():
			if u in self.list[i]:
				self.list[i].remove(u)
		if not flag:
			return 'No Vertex Found'
		else:
			return f"Deleted Vertex {u}"

	def checkedge(self, u, v):

		if v in self.list[u] and u in self.list[v]:
			return False
		else:
			return True

	def degree(self, vertex):
		return len(self.list[vertex])

	def isEmpty(self):
		return len(self.list) == 0

	def size(self):
		return len(self.list)

	def remove_edge(self, u, v):
		if v in self.list[u]:
			self.list[u].remove(v)
			self.list[v].remove(u)
			return f'Deleted Edge-> {u}--{v}'
		return 'No Edge Found'

	def bfs(self, start):
		visited = {}
		parent = {}
		level = {}
		ans = []
		queue = Queue()
		for i in self.list:
			visited[i] = False
			parent[i] = None
			level[i] = -1
		s = start
		visited[s] = True
		level[s] = 1
		queue.put(s)
		while not queue.empty():  # while the queue is not empty
			u = queue.get()  # popping from queue
			ans.append(u)
			for i in self.list[u]:
				if not visited[i]:
					visited[i] = True
					parent[i] = u
					level[i] = level[u] + 1
					queue.put(i)
		return ans

	def bfs_parent(self, start):
		visited = {}
		parent = {}
		level = {}
		ans = []
		queue = Queue()
		for i in self.list:
			visited[i] = False
			parent[i] = None
			level[i] = -1
		s = start
		visited[s] = True
		level[s] = 1
		queue.put(s)
		while not queue.empty():  # while the queue is not empty
			u = queue.get()  # popping from queue
			ans.append(u)
			for i in self.list[u]:
				if not visited[i]:
					visited[i] = True
					parent[i] = u
					level[i] = level[u] + 1
					queue.put(i)
		return parent

	def bfs_level(self, start):
		visited = {}
		parent = {}
		level = {}
		ans = []
		queue = Queue()
		for i in self.list:
			visited[i] = False
			parent[i] = None
			level[i] = -1
		s = start
		visited[s] = True
		level[s] = 1
		queue.put(s)
		while not queue.empty():  # while the queue is not empty
			u = queue.get()  # popping from queue
			ans.append(u)
			for i in self.list[u]:
				if not visited[i]:
					visited[i] = True
					parent[i] = u
					level[i] = level[u] + 1
					queue.put(i)
		return level

	def short_path(self, start, end):
		path = []
		parent = self.bfs_parent(start)
		while end is not None:
			path.append(end)
			end = parent[end]
		path.reverse()
		return path

	# find bfs for every node then search for the highest level.
	def diameter(self): # of the list is always greater than the max. level and smaller than 2*maxlevel
		if self.isEmpty():
			return "Empty List"
		highest = 0
		for i in self.list.keys():
			cur = self.findmax(i)
			if cur>highest:
				highest = cur
		return 2*highest

	def diameter_vertex(self,u,v): # it will be on a particular bfs for 'A'
		a = self.bfs_level('A')
		u_reach = a[u]
		v_reach = a[v]
		return(u_reach+v_reach-2) # as the level is taken as 1

	def findmax(self,i):
		level = self.bfs_level(i)
		return max(level.values())

	def bipartite(self): # check if there is an edge which is at the same level (odd-cycles)
		visited = {}
		level = {}
		queue = Queue()
		for node in self.list.keys():
			visited[node] = False
			level[node] = -1
		s = 'A'
		visited[s] = True
		level[s] = 1
		queue.put(s)

		while not queue.empty():
			u = queue.get() # popped element
			for v in self.list[u]:
				if visited[v] and level[u] == level[v]:
					return False
				if not visited[v]:
					visited[v] = True
					level[v] = level[u] + 1
					queue.put(v)
		return True

	def dfs_helper(self, v, color,parent,time,ans):
		color[v] = 'G' # when it is visited once then grey
		time[v][0] = self.Time
		ans.append(v)
		for node in self.list[v]:
			if color[node] =='W':
				parent[node] = v
				self.dfs_helper(node,color,parent,time,ans)
		color[v] = "B"
		time[v][1] = self.Time
		self.Time += 1

	def DFS(self, start):
		ans = []
		color = {}
		parent = {}
		time = {}
		for nodes in self.list:
			color[nodes] = 'W'
			parent[nodes] = None
			time[nodes] = [1,-1]
		self.dfs_helper(start,color,parent,time,ans)
		return ans


	def dfs_stacks(self,start):
		ans = []
		visited= {}
		for nodes in self.list:
			visited[nodes] = False
		temp = [start]
		visited[start] = True
		while len(temp)>0:
			u = temp.pop() # popping the top most element of the stack
			ans.append(u) # getting it in the ans
			for j in self.list[u]: # for neighbours of the popped element
				if visited[j] == False: # if not visited then append them in j
					temp.append(j)
					visited[j] = True
				else:
					continue
		return ans

	def Bridge(self):
		visited = {}
		parent = {}
		disc = {}
		low = {}
		for nodes in self.list:
			visited[nodes] = False
			parent[nodes] = None
			disc[nodes] = -1
			low[nodes] = -1
		for v in self.list:
			if not visited[i]:
				self.bridge_helper(v, visited, parent, disc, low)

	def bridge_helper(self, u, visited, parent, disc, low):
		visited[u] = True
		disc[u] = self.Time
		low[u] = self.Time
		self.Time += 1

		for v in self.list[u]:
			if not visited[v]:
				parent[v] = u
				self.bridge_helper(v, visited, parent, disc, low)
				low[u] = min(low[v], low[u])
				if low[v] > disc[u]:  # u, v is a bridge
					print((u,v) , end=" ")
			elif v != parent[u]:
				low[u] = min(low[u], disc[v])

nodes = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'),
		('B', 'C'),
		('C', 'D'),
		('D', 'E'),]
gp = Graph()
# list = {'A': ['B', 'C'],
#         'B': ['A','D','E'],
#         'C': ['A','D'],
#         'D': ['C','B','E'],
#         'E': ['B','D']}
rever_graph = Graph()
for i in nodes:
	gp.add_vertex(i)
	rever_graph.add_vertex(i)
for j in edges:
	gp.add_edge(j[0], j[1])
	rever_graph.add_edge(j[1],j[0])
gp.print_list()
rever_graph.print_list()
print(f"Degree--> {gp.degree('A')}\n")
print(f"List(Empty)--> {gp.isEmpty()}\n")
print(f"Size of List--> {gp.size()}\n")
# print(gp.remove_edge('D','E'))
# print(gp.remove_edge('A','C'))
# print(gp.remove_edge('B','D'))
# print(gp.remove_vertex('A'))
# gp.print_list()
print(f"BFS of 'A'(Connected Graph)-->{gp.bfs('A')}")
print(f"Shortest path-->{gp.short_path('A','E')}")
print(f"Diameter of the Graph-->{gp.diameter()}")
print(f"Diameter 'A' and 'B'-->{gp.diameter_vertex('A','E')}")
print(f"Graph(Bipartite) -->{gp.bipartite()}")
print(gp.DFS('A'))
print(gp.dfs_stacks('A'))

print("***************DIRECTED GRAPHS***************")
directed = Graph(is_directed=True)
for i in nodes:
	directed.add_vertex(i)
for j in edges:
	directed.add_edge(j[0], j[1])
directed.print_list()
print("Bridges are")
directed.Bridge()