'''
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.
'''

def explore(graph, current, visited):
    if current in visited: return False
    
    visited.add(current)
    
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
        
    return True

def connected_components_count(graph):
    '''
    Time: O(edges)
    Space: O(nodes)
    '''
    count = 0
    visited = set()

    for node in graph:
        if explore(graph, node, visited):
            count += 1
        
    return count

def main():    
    assert connected_components_count({
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }) == 2
    print("Test case 1 - passed")

    assert connected_components_count({
    1: [2],
    2: [1,8],
    6: [7],
    9: [8],
    7: [6, 8],
    8: [9, 7, 2]
    }) == 1
    print("Test case 2 - passed")

    assert connected_components_count({
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
    }) == 3
    print("Test case 3 - passed")

    assert connected_components_count({}) == 0
    print("Test case 4 - passed")

    assert connected_components_count({
    0: [4,7],
    1: [],
    2: [],
    3: [6],
    4: [0],
    6: [3],
    7: [0],
    8: []
    }) == 5
    print("Test case 5 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()