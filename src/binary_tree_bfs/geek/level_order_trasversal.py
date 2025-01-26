"""
Breadth-First Search (BFS) algorithms: BFS explores all nodes at the present depth before moving on to nodes at
the next depth level. It is typically implemented using a queue. BFS in a binary tree is commonly referred to as
Level Order Traversal.
"""

import pytest


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# In-order DFS: Left, Root, Right
def in_order_dfs(node, res):
    if node is None:
        return
    in_order_dfs(node.left, res)
    print(node.data, end=' ')
    res.append(node.data)
    in_order_dfs(node.right, res)


# Pre-order DFS: Root, Left, Right
def pre_order_dfs(node, res):
    if node is None:
        return
    print(node.data, end=' ')
    res.append(node.data)
    pre_order_dfs(node.left, res)
    pre_order_dfs(node.right, res)


# Post-order DFS: Left, Right, Root
def post_order_dfs(node, res):
    if node is None:
        return
    post_order_dfs(node.left, res)
    post_order_dfs(node.right, res)
    print(node.data, end=' ')
    res.append(node.data)


# BFS: Level order traversal
def bfs(root, res):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
def test_merge(s, t, expected_output):
    # Creating the tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    print("In-order DFS: ", end='')
    res = []
    in_order_dfs(root, res)
    assert res == [5, 3, 2, 4]

    print("\nPre-order DFS: ", end='')
    res = []
    pre_order_dfs(root, res)
    assert res == [2, 3, 5, 4]

    print("\nPost-order DFS: ", end='')
    res = []
    post_order_dfs(root, res)
    assert res == [5, 3, 4, 2]

    print("\nLevel order: ", end='')
    res = []
    bfs(root, res)
    assert res == [2, 3, 4, 5]
