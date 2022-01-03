'''
Tree Minimum Value

Inputs: 
[root: Node]

Time complexity: O(n)
Space complexity: O(n)
'''

def max_path_sum(root):
    if not root:
        return float('-inf')

    if not root.left and not root.right:
        return root.val

    left_sum = max_path_sum(root.left)
    right_sum = max_path_sum(root.right)

    return root.val + max(left_sum, right_sum)



def test_case_0(func):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    return func(a) # -> 18

def test_case_1(func):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \      
    # 20   15
    #      / \
    #     1  3

    return func(a) # -> 59

def test_case_2(func):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    
    a = Node(-1)
    b = Node(-6)
    c = Node(-5)
    d = Node(-3)
    e = Node(0)
    f = Node(-13)
    g = Node(-1)
    h = Node(-2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #        -1
    #      /   \
    #    -6    -5
    #   /  \     \
    # -3   0    -13
    #     /       \
    #    -1       -2

    return func(a) # -> -8

def test_case_3(func):
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    
    a = Node(42)

    #        42

    return func(a) # -> 42

def main():
    assert test_case_0(max_path_sum) == 18, 'Test case 1 - failed'
    print("Test case 1 - passed")
    assert test_case_1(max_path_sum) == 59, 'Test case 2 - failed'
    print("Test case 2 - passed")
    assert test_case_2(max_path_sum) == -8, 'Test case 3 - failed'
    print("Test case 3 - passed")
    assert test_case_3(max_path_sum) == 42, 'Test case 4 - failed'
    print("Test case 4 - passed")

    print ("All test cases passed!!")

if __name__ == '__main__':
    main()