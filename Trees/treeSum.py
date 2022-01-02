'''
Tree Sum

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
def treeSum(root: Node):
    if not root:
        return 0

    queue = [root]
    result = 0

    while queue:
        current = queue.pop(0)

        result += current.val

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return result

# Recursive
def treeSumRecursive(root: Node):
    if not root:
        return 0

    return root.val + treeSumRecursive(root.left) + treeSumRecursive(root.right)

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

    assert treeSum(None) == 0, 'Test case 1 - failed'
    print("Test case 1 - passed")
    assert treeSum(a) == 28, 'Test case 2 - failed'
    print("Test case 2 - passed")

    assert treeSumRecursive(None) == 0, 'Test case 3 - failed'
    print("Test case 3 - passed")
    assert treeSumRecursive(a) == 28, 'Test case 4 - failed'
    print("Test case 4 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()