'''
Tree Minimum Value

Inputs: 
[root: Node]

Time complexity: O(n)
Space complexity: O(n)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative
def treeMinValue(root: Node):
    stack = [root]
    smallest = float('inf')

    while stack:
        current = stack.pop()
        
        smallest = min(smallest, current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return smallest

# Recursive
def treeMinValueRecursive(root: Node):
    if not root:
        return float('inf')

    return min(root.val, treeMinValueRecursive(root.left), treeMinValueRecursive(root.right))

def main():
    # Test tree
    a = Node(2)
    b = Node(7)
    c = Node(9)
    d = Node(1)
    e = Node(6)
    f = Node(3)

    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f

    assert treeMinValue(a) == 1, 'Test case 1 - failed'
    print("Test case 1 - passed")
    
    assert treeMinValueRecursive(a) == 1, 'Test case 2 - failed'
    print("Test case 2 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()