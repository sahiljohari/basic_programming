# Program to implement Lowest Common Ancestor problem

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(tree, n1, n2):
    if n1 == n2:
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

        if s == t:
            prev = s
        else:
            break
    return prev

def pathTo(tree, n):
    if tree is None:
        return None
    if tree == n:
        s = []
        s.append(tree)
        return s
    
    left, right = [], []
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

    n1 = Node(3)
    n2 = Node(4)

    print(lca(root, n1, n2))

if __name__ == "__main__":
    main()