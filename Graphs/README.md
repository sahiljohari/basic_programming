## Graphs

- graph = nodes + edges
- describes relations between things
- types: directed; undirected
- represented as: adjacency list or adjacency matrix

An example fo adjacency list:

```python
{
    a: [b,c],
    b: [d],
    c: [e],
    d: [],
    e: [b],
    f: [d]
}
```

- Graphs can be traversed in 2 ways: depth-first and breadth-first

#### Depth-first traversal

- Uses a stack

Iterative code

```python
def depth_first_traversal(graph, source):
    stack = [ source ]

    while stack:
        current = stack.pop()
        print(current)

        for neighbor in graph[current]:
            stack.append(neighbor)
```

Recursive code

```python
def depth_first_traversal(graph, source):
    print(source)

    for neighbor in graph[source]:
        depth_first_traversal(graph, neighbor)
```

#### Breadth-first traversal

- Uses a queue

```python
def breadth_first_traversal(graph, source):
    queue = [ source ]

    while queue:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            queue.append(neighbor)
```

### Fundamental coding problems

- [Has Path](hasPath.py)
- [Undirected Path](undirectedPath.py)
- [Connected Components Count](connectedComponentsCount.py)
- [Largest Component](largestComponent.py)
- [Shortest Path](shortestPath.py)
