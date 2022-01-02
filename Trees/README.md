## Trees

### Binary Tree

- At most 2 children per node
- Exactly 1 root
- Exactly 1 path between root and any node
- **[Edge case]** An empty tree can also be a binary tree

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### Fundamental coding problems

- [Depth First Values](depthFirstValues.py)
- [Breadth First Values](breadthFirstValues.py)

### Code snippets (Python)

- Height of a binary tree

```python
def height(root):
    if not root:
        return -1

    return max(1 + height(root.left), 1 + height(root.right))
```

- Lowest common ancestor (Binary Tree)

```python
def lca(root, p, q):
    if not root: return None
    if root == p or root == q: return root

    left_lca = lca(root.left, p, q)
    right_lca = lca(root.right, p, q)

    if left_lca and right_lca: return root
    return left_lca if left_lca else right_lca
```

- Lowest common ancestor (Binary Search Tree)

```python
def lca(root, p, q):
    if root.val > p.val and root.val > q.val:
        return lca(root.left, p, q)
    if root.val < p.val and root.val < q.val:
        return lca(root.right, p, q)

    return root
```

- Prune a Binary Tree (delete a target node)

```python
def prune_tree(root, target):
    if root.left: root.left = prune_tree(root.left, target)
    if root.right: root.right = prune_tree(root.right, target)

    if root.val == target and not (root.left and root.right): return None
    return root

```
