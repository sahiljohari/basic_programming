'''
Breadth First Traversal

Time complexity: O(n)
Space complexity: O(n)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative
def breadthFirstValues(root: Node):
    if not root:
        return []


    queue = [root]
    result = []

    while queue:
        current = queue.pop(0)

        # visit the node
        result.append(current.val)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return result

def main():
    # Test tree
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f

    assert breadthFirstValues(None) == []
    print("Test case 1 - passed")
    assert breadthFirstValues(a) == ['a', 'b', 'c', 'd', 'e', 'f']
    print("Test case 2 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()