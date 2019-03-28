# Program to implement basic operations in a binary tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Inorder traversal of binary tree (or Breadth-first Search)
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

# Delete the deepest node in the tree
def deleteDeepest(root, nodeToDelete):
    q = []
    q.append(root)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if temp.right:
            if temp.right == nodeToDelete:
                temp.right = None
                del(nodeToDelete)
                return
            else:
                q.append(temp.right)

        if temp.left:
            if temp.left == nodeToDelete:
                temp.left = None
                del(nodeToDelete)
                return
            else:
                q.append(temp.left)

# Delete a given node
def deleteNode(root, val):
    q = []
    q.append(root)

    key_node = Node(None)

    while(len(q)):
        temp = q[0]
        q.pop(0)

        if temp.val == val:
            key_node = temp

        if temp.left:
            q.append(temp.left)

        if temp.right:
            q.append(temp.right)

    x = temp.val
    deleteDeepest(root, temp)
    key_node.val = x


def main():
    root = Node(13)
    # Create left sub-tree
    root.left = Node(12)
    root.left.left = Node(4)
    root.left.right = Node(19)
    # Create right sub-tree
    root.right = Node(10)
    root.right.left = Node(16)

    print("Here is the initial tree (Inorder traversal):")
    inorder(root)

    insert_key = int(input("\nEnter the node value to be inserted: "))
    insertNode(root, insert_key)
    print("Inorder traversal after insertion:")
    inorder(root)

    delete_key = int(input("\nEnter the node value to be deleted: "))
    deleteNode(root, delete_key)
    # After deletion
    print("Inorder traversal after deletion:")
    inorder(root)

if __name__ == "__main__":
    main()