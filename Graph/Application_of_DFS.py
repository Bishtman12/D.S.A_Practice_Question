# 1. Cyclic Graphs
# 2. Bridge
# 3. Connected Graph
# 4. Topological Sort
import random


class Graph:

    def __init__(self, isDirected=True):
        self.isDirected = isDirected
        self.list = {}
        self.Time = 0

    def add_vertex(self, v):
        if v in self.list:
            return "Vertex Already Present"
        self.list[v] = []

    def add_edge(self, u, v):  # if the edge is like u->v
        if self.check_edge(u, v):
            return f"Edge {u}->{v} already present"
        self.list[u].append(v)
        if self.isDirected is False:
            self.list[v].append(u)

    def check_edge(self, u, v):
        if v in self.list[u]:
            return True
        return False

    def DFS(self, v):
        if v not in self.list:
            return "NO VERTEX FOUND"
        ans = []
        color = {}  # W -> not visited G-> visited once and B-> visited twice
        parent = {}
        for nodes in self.list:
            color[nodes] = 'W'
            parent[nodes] = None
        self.DFS_helper(v, color, parent, ans)
        return ans

    def DFS_helper(self, v, color, parent, ans):
        color[v] = 'G'
        ans.append(v)
        for w in self.list[v]:
            if color[w] == 'W':  # nodes not even visited once then turn their color to the grey
                parent[w] = v
                self.DFS_helper(w, color, parent, ans)
        color[v] = 'B'

    def DFS_time(self, v):
        color = {}  # W -> not visited G-> visited once and B-> visited twice
        time = {}
        parent = {}
        for nodes in self.list:
            color[nodes] = 'W'
            time[nodes] = [-1, -1]
            parent[nodes] = None
        self.DFS_helper_time(v, color, time, parent)
        self.Time = 0
        return time

    def DFS_helper_time(self, v, color, time, parent):
        color[v] = 'G'
        time[v][0] = self.Time  # arrival time
        self.Time += 1
        for w in self.list[v]:
            if color[w] == 'W':  # nodes not even visited once then turn their color to the grey
                parent[w] = v
                self.DFS_helper_time(w, color, time, parent)
        color[v] = 'B'
        time[v][1] = self.Time
        self.Time += 1

    def print_list(self):  # print(self.list)
        for i in self.list:
            print(f"{i}-->{self.list[i]}")

    def cycle(self):  # if there is node which is already visited(g) and we also reach that node by dfs(adj) then cycle.
        color = {}
        parent = {}
        # generate a dict
        for i in self.list:
            color[i] = 'W'
            parent[i] = None
        is_Cyclic = False  # set the initial cycle to none

        for u in self.list.keys():  # for every vertex in the graph
            if color[u] == 'W':  # if not visited then do a dfs
                is_Cyclic = self.cycle_helper(u, color, parent)
                if is_Cyclic:  # if true then there is a cycle present in the graph
                    return True
                break
        return is_Cyclic

    def cycle_helper(self, u, color, parent):
        color[u] = 'G'
        for v in self.list[u]:  # checking the neighbours of u
            if color[v] == 'W':  # if not visited the call dfs on v
                cycle = self.cycle_helper(v, color, parent)
                if cycle:
                    return True
            elif color[v] == 'G':  # if the neighbour is alread visited then there is a cycle in the graph.
                return True
        color[u] = 'B'
        return False  # should return false then it will check for other vertex in case graph is not connected.

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
                    print((u, v), end=" ")
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def Topological_Sort(self):
        # Topological sorting is a linear ordering of vertices
        # such that for every directed edge u v,
        # vertex u comes before v in the ordering
        visited = {}
        stack = []
        for nodes in self.list:
            visited[nodes] = False

        for v in self.list:  # picking the first node from the list.
            if not visited[v]:
                self.Topo_helper(v, visited, stack)
        print(stack[::-1])  # print them in the reverse order

    def Topo_helper(self, v, visited, stack):
        visited[v] = True
        for u in self.list[v]:  # for neighbours of v
            if not visited[u]:  # if not visited then visited them
                self.Topo_helper(u, visited, stack)
        stack.append(v)  # append in the stack(top of the stack will be the last s
        return stack

    def strong_connected(self, edges):  # when there is a way to reach every vertex from any vertex
        v = random.choice(list(self.list.keys()))
        visited = {}
        for nodes in self.list:
            visited[nodes] = False
        check = self.DFS(v)
        if len(check) != len(self.list.keys()):
            return False
        # now do the transpose of every node then check the same condition again.

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'B'), ('A', 'C'),
         ('B', 'D'), ('B', 'E'),
         ('D', 'A'),
         ('C', 'B'), ('C', 'F'),
         ('E', 'F'),
         ]
rever_graph = Graph()
directed = Graph()
for i in nodes:
    rever_graph.add_vertex(i)
    directed.add_vertex(i)

for j in edges:
    directed.add_edge(j[0], j[1])
    rever_graph.add_edge(j[1], j[0])
rever_graph.print_list()
directed.print_list()
print(directed.DFS('A'))
print(directed.DFS_time('A'))
print(directed.cycle())
print("BRIDGES ARE:")
directed.Bridge()
print("\nTopo Sort:")
directed.Topological_Sort()
