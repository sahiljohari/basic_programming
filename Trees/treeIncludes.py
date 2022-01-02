'''
Tree Includes

Inputs: 
[root: Node, target: str]

Time complexity: O(n)
Space complexity: O(n)
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Iterative
def treeIncludes(root: Node, target: str):
    if not root:
        return False

    queue = [root]

    while queue:
        current = queue.pop(0)

        if target == current.val:
            return True

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)
    
    return False

# Recursive
def treeIncludesRecursive(root: Node, target: str):
    if not root:
        return False

    if root.val == target:
        return True

    return treeIncludesRecursive(root.left, target) or treeIncludesRecursive(root.right, target)

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

    assert treeIncludes(None, 'a') == False
    print("Test case 1 - passed")
    assert treeIncludes(a, 'e') == True
    print("Test case 2 - passed")
    assert treeIncludes(a, 'z') == False
    print("Test case 3 - passed")

    assert treeIncludesRecursive(None, 'a') == False
    print("Test case 4 - passed")
    assert treeIncludesRecursive(a, 'e') == True
    print("Test case 5 - passed")
    assert treeIncludesRecursive(a, 'z') == False
    print("Test case 6 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()