# Using dictionaries, it is easy to implement the adjacency list in Python. 
# In our implementation of the Graph abstract data type we will create two classes- 
# Graph, which holds the master list of vertices, and 
# Vertex, which will represent each vertex in the graph.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo:' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, source, target, cost=0):
        if source not in self.vertList:
            newVertex = self.addVertex(source)
        if target not in self.vertList:
            newVertex = self.addVertex(target)

        self.vertList[source].addNeighbor(target, cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

def main():
    g = Graph()
    # Add vertices
    for i in range(6):
        g.addVertex(i)

    # Add edges with weights
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)

    # Print the graph
    for v in g:
        for w in v.getConnections():
            print("( %d , %d )" % (v.getId(), w))

if __name__ == "__main__":
    main()