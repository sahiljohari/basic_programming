# Coding problems and notes

This repository maintains solutions of my practice problems along with implementation of Data structures and algorithms. It contains notes on how to approach different kinds of problems in a technical interview, purely based on my own personal experience.

---

### Code snippets (Python)

These are some of the code snippets that come in handy during a coding interview with certain common operations

- Get top k elements from a dictionary

```python
sorted(dict, k = dict.get, reverse=True)[:k]
```

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
