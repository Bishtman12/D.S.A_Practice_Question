from queue import Queue
list = {'A': ['B', 'C'],
        'B': ['A','D','E'],
        'C': ['A','D'],
        'D': ['C','B','E'],
        'E': ['B','D']}
visited = {}
level = {}
parent = {}
bfs_output = []
queue = Queue()

for node in list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None
#putting A as the starting position in the queue.
s = 'A'
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get() # popping from queue
    bfs_output.append(u) # appending the popped element in the list
    print(u)

    for v in list[u]:# neighbours of u in the queue now
        if not visited[v]: # updating them if not visited already
            visited[v] = True
            parent[v] = u
            level[v] = level[u]+1
            queue.put(v) # putting the neighbours of v in the queue now

print(bfs_output)
print(f"Distance of E-->{level['E']}")
#path from node to source

v = 'E'
path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(f"Path to 'E'-->{path}")
