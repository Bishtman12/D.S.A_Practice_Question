class Graph:
    def __init__(self,Vertices):
        self.V = Vertices
        self.graph = []

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])

    def print_g(self):
        print(self.graph)

    def union(self,parent,rank,x,y):
        xroot = self.find(parent,x) # locating the root node
        yroot = self.find(parent,y)

        if rank[xroot] < rank[yroot]: # assign the root which has maximum height
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else: # if height are same then assign either and increase the height by one
            parent[yroot] = xroot
            rank[xroot] += 1

    def print_kruskal(self,result):
        cost = 0
        print("Edges in MST:")
        for u,v,w in result:
            cost += w
            print(f"{u}--{v}--->{w}")
        print(f"Cost-->{cost}")

    def kruskal(self):
        result = []
        i,e = 0,0 # i -> index in the graph e->index of result arr

        # sort the array acc to weights
        self.graph = sorted(self.graph, key = lambda x:x[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node) # every node points to itself
            rank.append(0) # level is 0

        while e<self.V-1:# picking the smallest weighted edge
            u,v,w = self.graph[i]
            i += 1
            x = self.find(parent,u)
            y = self.find(parent,v)

            # if parent of both are diff then no cycle, add in the result
            if x!=y:
                e += 1
                result.append([u,v,w])
                self.union(parent,rank,x,y) # assign the parents and rank.
        self.print_kruskal(result)



g = Graph(6)
g.addEdge(0,1,12)
g.addEdge(1, 2,15)
g.addEdge(1, 3,12)
g.addEdge(2, 4,13)
g.addEdge(2, 5,5)
g.addEdge(3, 2,6)
g.addEdge(3,4,6)
g.kruskal()
