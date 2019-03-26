# Program to implement basic operations in a binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder traversal of binary tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Insert a node in level order
def insertNode(root, val):
    # create a queue that stores root nodes at each level
    q = []
    q.append(root)

    while(len(q)):
        temp = q[0]
        q.pop(0)
        # check for node on the left and insert new node if empty
        if not temp.left:
            temp.left = Node(val)
            break
        else:
            q.append(temp.left)
        # check for node on the right and insert new node if empty
        if not temp.right:
            temp.right = Node(val)
            break
        else:
            q.append(temp.right)