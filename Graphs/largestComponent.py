'''
Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.
'''

def largest_component(graph):
    '''
    Time: O(edges)
    Space: O(nodes)
    '''
    largest = 0
    visited = set()
    
    for node in graph:
        largest = max(largest, explore(graph, node, visited))
        
    return largest

def explore(graph, current, visited):
    if current in visited: return 0

    visited.add(current)
    component_size = 1
    
    for neighbor in graph[current]:
        component_size += explore(graph, neighbor, visited)
        
    return component_size

def main():    
    assert largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
    }) == 4
    print("Test case 1 - passed")

    assert largest_component({
    1: [2],
    2: [1,8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
    }) == 6
    print("Test case 2 - passed")

    assert largest_component({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
    }) == 5
    print("Test case 3 - passed")

    assert largest_component({}) == 0
    print("Test case 4 - passed")

    assert largest_component({
    0: [4,7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
    }) == 3
    print("Test case 5 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()