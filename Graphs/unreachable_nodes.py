'''
You have been given a graph consisting of N nodes and M edges. The nodes in this graph are enumerated from 1 to N . 
The graph can consist of self-loops as well as multiple edges. This graph consists of a special node called the head node. 
You need to consider this and the entry point of this graph. You need to find and print the number of nodes that are unreachable 
from this head node.

*Input Format*:
The first line consists of a 2 integers N and M denoting the number of nodes and edges in this graph. 
The next M lines consist of 2 integers a and b denoting an undirected edge between node a and b. 
The next line consists of a single integer x denoting the index of the head node.

*Output Format*:
You need to print a single integer denoting the number of nodes that are unreachable from the given head node.
'''

from dfs_bfs import graph

N, M = 10, 10
g = graph()
g.add_edge('8', '1')
g.add_edge('8', '3')
g.add_edge('7', '4')
g.add_edge('7', '5')
g.add_edge('2', '6')
g.add_edge('10', '7')
g.add_edge('2', '8')
g.add_edge('10', '9')
g.add_edge('2', '10')
g.add_edge('5', '10')
start_vertex = '2'
nodes = g.dfs(start_vertex)

print('Total unreachable nodes: ', N-len(nodes))
