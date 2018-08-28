'''
Implementation of Depth-first search & Breadth-first search
'''
from collections import defaultdict

class graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(set)

    # function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].add(v)

    # function to implement DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        # mark the current node as visited and print it
        visited.add(start)
        print(start,)

        # recurse for all the adjacent vertices to this vertex
        for next in self.graph[start] - visited:
            self.dfs(next, visited)
        # return visited

    # function to implement BFS
    def bfs(self, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            print(vertex, end = " ")
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(self.graph[vertex] - visited)

# Driver code
# Create a graph given in the above diagram
g = graph()
g.add_edge('0', '1')
g.add_edge('0', '2')
g.add_edge('1', '2')
g.add_edge('2', '0')
g.add_edge('2', '3')
g.add_edge('3', '3')
 
print ("Following is DFS from (starting from vertex 2)")
g.dfs('2')

print ("Following is Breadth-first traversal from (starting from vertex 2)")
g.bfs('2')