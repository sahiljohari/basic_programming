'''
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return the length of the shortest path between A and B. 
Consider the length as the number of edges in the path, not the number of nodes. 
If there is no path between A and B, then return -1.
'''

from collections import deque

def shortest_path(edges, node_A, node_B):
    queue = deque([(node_A, 0)])
    graph = build_graph(edges)
    visited = set()
    
    while queue:
        current_node, distance = queue.popleft()

        if current_node == node_B:
            return distance

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(current_node)
                queue.append((neighbor, distance+1))
        
    return -1

def build_graph(edges):
	graph = {}
	
	for u, v in edges:
		graph.setdefault(u, []).append(v)
		graph.setdefault(v, []).append(u)
		
	return graph

def main():
    edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
    ]
    assert shortest_path(edges, 'w', 'z') == 2
    print("Test case 1 - passed")

    assert shortest_path(edges, 'y', 'x') == 1
    print("Test case 2 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()