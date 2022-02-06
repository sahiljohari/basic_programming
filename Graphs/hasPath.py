'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). 
The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
'''

# depth-first
def has_path(graph, src, dst):
    '''
    Time: O(edges)
    Space: O(nodes)
    '''
    if src == dst: return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst):
            return True
    
    return False

# breadth-first
def has_path_bfs(graph, src, dst):
    '''
    Time: O(edges)
    Space: O(nodes)
    '''
    queue = [src]
    
    while queue:
        current = queue.pop(0)
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
        
    return False

def main():
    # Test graph
    graph = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    assert has_path(graph, 'f', 'k') == True
    assert has_path_bfs(graph, 'f', 'k') == True
    print("Test case 1 - passed")

    assert has_path(graph, 'f', 'j') == False
    assert has_path_bfs(graph, 'f', 'j') == False
    print("Test case 2 - passed")

    assert has_path(graph, 'i', 'h') == True
    assert has_path_bfs(graph, 'i', 'h') == True
    print("Test case 3 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()