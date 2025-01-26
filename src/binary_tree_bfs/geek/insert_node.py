"""
Inserting elements means add a new node into the binary tree. As we know that there is no such ordering of elements
in the binary tree, So we do not have to worry about the ordering of node in the binary tree.
We would first create a root node in case of empty tree. Then subsequent insertions involve iteratively searching
for an empty place at each level of the tree. When an empty left or right child is found then new node is inserted
there. By convention, insertion always starts with the left child node.
"""

from collections import deque

import pytest


class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# Function to insert a new node in the binary tree
def insert(root, key):
    if root is None:
        return Node(key)

    # Create a queue for level order traversal
    queue = deque([root])

    while queue:
        temp = queue.popleft()

        # If left child is empty, insert the new node here
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        # If right child is empty, insert the new node here
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)

    return root


# Function to delete a node from the binary tree
def deleteNode(root, val):
    if root is None:
        return None

    # Use a queue to perform BFS
    queue = deque([root])
    target = None

    # Find the target node
    while queue:
        curr = queue.popleft()

        if curr.data == val:
            target = curr
            break
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    if target is None:
        return root

    # Find the deepest rightmost node and its parent
    last_node = None
    last_parent = None
    queue = deque([(root, None)])

    while queue:
        curr, parent = queue.popleft()
        last_node = curr
        last_parent = parent

        if curr.left:
            queue.append((curr.left, curr))
        if curr.right:
            queue.append((curr.right, curr))

    # Replace target's value with the last node's value
    target.data = last_node.data

    # Remove the last node
    if last_parent:
        if last_parent.left == last_node:
            last_parent.left = None
        else:
            last_parent.right = None
    else:
        return None
    return root


# In-order traversal
def inorder(root, node_list):
    if root is None:
        return
    inorder(root.left, node_list)
    print(root.data, end=" ")
    node_list.append(root.data)
    inorder(root.right, node_list)


@pytest.mark.parametrize('s, t, expected_output', [
    ("aaaaaa", "bbaaaa", True),
])
class TestCase:
    def test_insert(self, s, t, expected_output):
        root = Node(2)
        root.left = Node(3)
        root.right = Node(4)
        root.left.left = Node(5)

        print("Inorder traversal before insertion: ", end="")
        res = []
        inorder(root, res)
        assert res == [5, 3, 2, 4]
        print()

        key = 6
        root = insert(root, key)

        print("Inorder traversal after insertion: ", end="")
        res = []
        inorder(root, res)
        assert res == [5, 3, 6, 2, 4]

    def test_delete(self, s, t, expected_output):
        root = Node(2)
        root.left = Node(3)
        root.right = Node(4)
        root.left.left = Node(5)
        root.left.right = Node(6)

        res = []
        print("Original tree (in-order): ", end="")
        inorder(root, res)

        assert res == [5, 3, 6, 2, 4]

        val_to_del = 3
        root = deleteNode(root, val_to_del)

        print(f"Tree after deleting {val_to_del} (in-order): ", end="")
        res = []
        inorder(root, res)
        assert res == [5, 6, 2, 4]
