'''
Depth First Traversal

Time complexity: O(n)
Space complexity: O(n)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative
def depthFirstValues(root: Node):
    if not root:
        return []


    stack = [root]
    result = []

    while stack:
        current = stack.pop()

        # visit the node
        result.append(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return result

# Recursive (Preorder)
def depthFirstRecursive(root: Node):
    if not root:
        return []

    left = depthFirstRecursive(root.left)
    right = depthFirstRecursive(root.right)

    return [root.val] + left + right


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

    assert depthFirstValues(None) == []
    assert depthFirstValues(a) == ['a', 'b', 'd', 'e', 'c', 'f']

    assert depthFirstRecursive(None) == []
    assert depthFirstRecursive(a) == ['a', 'b', 'd', 'e', 'c', 'f']

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()