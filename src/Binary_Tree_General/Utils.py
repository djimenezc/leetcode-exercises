import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(nodes: list) -> TreeNode:
    n = len(nodes)

    if n == 0:
        return None

    parentStack = collections.deque()
    root = TreeNode(nodes[0])
    curParent = root

    for i in range(1, n):
        if i % 2 == 1:
            if nodes[i] is not None:
                curParent.left = TreeNode(nodes[i])
                parentStack.append(curParent.left)
        else:
            if nodes[i] is not None:
                curParent.right = TreeNode(nodes[i])
                parentStack.append(curParent.right)

            curParent = parentStack.popleft()

    return root


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True  # Both are None
    if not p or not q:
        return False  # One is None and the other is not
    if p.val != q.val:
        return False  # Values are different

    # Recursively check left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
