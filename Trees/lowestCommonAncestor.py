# Program to implement Lowest Common Ancestor problem
# Time complexity: O(n)
# Space complexity: O(n)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(tree, n1, n2):
    if n1.val == n2.val:
        return n1
    path_to_n1, path_to_n2 = [], []
    path_to_n1 = pathTo(tree, n1)
    path_to_n2 = pathTo(tree, n2)

    if path_to_n1 is None or path_to_n2 is None:
        return None

    prev = None
    while len(path_to_n1) != 0 and len(path_to_n2) != 0:
        s = path_to_n1.pop()
        t = path_to_n2.pop()

        if s.val == t.val:
            prev = s
        else:
            break
    return prev.val

def pathTo(tree, n):
    if tree is None:
        return None
    if tree.val == n.val:
        return [tree]
    
    left = pathTo(tree.left, n)
    right = pathTo(tree.right, n)

    if left is not None:
        left.append(tree)
        return left

    if right is not None:
        right.append(tree)
        return right

    return None

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)

    assert lca(root, Node(3), Node(4)) == 1, "Test case failure"
    assert lca(root, Node(5), Node(6)) == 3, "Test case failure"

    print("All test cases passed.")

if __name__ == "__main__":
    main()