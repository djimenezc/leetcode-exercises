"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        elif p and not q:
            return False
        elif not p and q:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True  # Both are None
        if not p or not q:
            return False  # One is None and the other is not
        if p.val != q.val:
            return False  # Values are different

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


@pytest.mark.parametrize('p, q, expected_output', [
    (TreeNode(1, TreeNode(2, None, None), TreeNode(3, None)),
     TreeNode(1, TreeNode(2, None, None), TreeNode(3, None)), True),
    (TreeNode(1, TreeNode(2, None, None), None),
     TreeNode(1, None, TreeNode(2, None, None)), False),
    (TreeNode(1, TreeNode(2, None, None), TreeNode(1, None, None)),
     TreeNode(1, TreeNode(1, None, None), TreeNode(2, None, None)), False),
])
def test_merge(p, q, expected_output):
    solution = Solution()
    output = solution.isSameTree(p, q)

    assert output == expected_output
    output = solution.isSameTree2(p, q)

    assert output == expected_output
