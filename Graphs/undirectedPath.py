'''
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
'''

def build_graph(edges):
	graph = {}
	
	for u, v in edges:
		graph.setdefault(u, []).append(v)
		graph.setdefault(v, []).append(u)
		
	return graph

def has_path(graph, src, dst, visited):
	if src == dst: return True
	if src in visited: return False

	visited.add(src)

	for neighbor in graph[src]:
		if has_path(graph, neighbor, dst, visited):
			return True
		
	return False

def undirected_path(edges, node_A, node_B):
	'''
    Time: O(edges)
    Space: O(nodes)
    '''
	graph = build_graph(edges)
	return has_path(graph, node_A, node_B, set())

def main():
    edges = [
		('i', 'j'),
		('k', 'i'),
		('m', 'k'),
		('k', 'l'),
		('o', 'n')
	]

    assert undirected_path(edges, 'j', 'm') == True
    print("Test case 1 - passed")

    assert undirected_path(edges, 'm', 'j') == True
    print("Test case 2 - passed")

    assert undirected_path(edges, 'l', 'j') == True
    print("Test case 3 - passed")

    assert undirected_path(edges, 'k', 'o') == False
    print("Test case 4 - passed")

    assert undirected_path(edges, 'i', 'o') == False
    print("Test case 5 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()