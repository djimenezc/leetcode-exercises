import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes: list) -> Optional[TreeNode]:
    n = len(nodes)

    if n == 0:
        return None

    parent_stack = collections.deque()
    root = TreeNode(nodes[0])
    cur_parent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                cur_parent.left = TreeNode(nodes[i])
                parent_stack.append(cur_parent.left)
        else:
            if nodes[i] is not None:
                cur_parent.right = TreeNode(nodes[i])
                parent_stack.append(cur_parent.right)

            cur_parent = parent_stack.popleft()

    return root


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other is not
    if p.val != q.val:
        return False  # Values are different

    # Recursively check left and right subtrees
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
