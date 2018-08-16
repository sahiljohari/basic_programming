# Program to implement Binary Search Tree data structure

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# --Helper functions--
# Creates a new node    
def createNode(val):
    node = Node(val)
    node.left = node.right = None

    return node

# Finds the minimum node in a tree/sub-tree
def find_min(root):
    current = root
    # loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

# Traverses in-order on a binary search tree
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, " ")
        inorder(root.right)

# --Binary Search Tree methods--
# Inserts a node into the tree
def insert_node(root, val):
    if root is None:
        root = createNode(val)
    elif val <= root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root

# Deletes a node from the tree
def delete_node(root, val):
    if root is None:
        return root
    elif val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        # This is the hard part
        # case 1 - no child
        if root.left is None and root.right is None:
            root = None
        # case 2 - One child
        elif root.left is None:
            temp = root
            root = root.right
            del temp
        elif root.right is None:
            temp = root
            root = root.left
            del temp
        # case 3 - 2 children nodes
        else:
            temp = find_min(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)
    return root

# Searches for a node
def search_node(root, val):
    if root is None:
        return False
    elif root.val == val:
        return True
    elif val <= root.left:
        return search_node(root.left, val)
    elif val > root.right:
        return search_node(root.right, val)

if __name__=="__main__":
    root = None
    root = insert_node(root, 50)
    root = insert_node(root, 30)
    root = insert_node(root, 20)
    root = insert_node(root, 40)
    root = insert_node(root, 70)
    root = insert_node(root, 60)
    root = insert_node(root, 80)
    
    print("Inorder traversal of the given tree")
    inorder(root)
    
    print("\nDelete 20")
    root = delete_node(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 30")
    root = delete_node(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)
    
    print("\nDelete 50")
    root = delete_node(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)