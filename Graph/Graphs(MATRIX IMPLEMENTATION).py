import random
# class Graph():
#     def __init__(self, size):
#         self.adjMatrix = []
#         for i in range(size):
#             self.adjMatrix.append([0 for i in range(size)]) # making a matrix of size 5*5 with 0
#         self.size = size
#
#     def add_edge(self, v1, v2):# then marking those values as 1 if they are present
#         self.adjMatrix[v1][v2] = 1
#         self.adjMatrix[v2][v1] = 1
#     def print_matrix(self):
#         print(self.adjMatrix)
#         return
# def main():
#     g = Graph(5)
#     g.add_edge(0, 1)
#     g.add_edge(0, 2)
#     g.add_edge(1, 2)
#     g.add_edge(2, 0)
#     g.add_edge(2, 3)
#
#     g.print_matrix()
#
#
# if __name__ == '__main__':
#     main()
import random
d = {'A': ['B'],
        'B': ['D', 'E'],
        'C': ['B', 'F'],
        'D': [],
        'E': ['F'],
        'F': []}

print(type(random.choice(list(d.keys()))))