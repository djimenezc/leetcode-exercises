"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

A binary tree is symmetric if:

Its left and right subtrees have the same structure.
The values in the left and right subtrees mirror each other.

We can solve this using recursion or iteration:

Recursive Approach:

Compare the left and right subtrees of the root.
For two subtrees to be mirrors:
Their root values must be equal.
The left subtree of one must be a mirror of the right subtree of the other, and vice versa.
Recursively check this condition for all nodes.
Iterative Approach:

Use a queue to perform a level-order traversal, checking symmetry at each level.
Push pairs of nodes to the queue for comparison.

"""
from typing import Optional

import pytest
from ..Utils import TreeNode, buildTree, isSameTree
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t1 and not t2:  # Both are None
            return True
        if not t1 or not t2:  # One is None and the other is not
            return False
        return (t1.val == t2.val and
                self.isMirror(t1.left, t2.right) and
                self.isMirror(t1.right, t2.left))

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([root.left, root.right])
        while queue:
            t1 = queue.popleft()
            t2 = queue.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True


@pytest.mark.parametrize('root, expected_output', [
    (buildTree([1, 2, 2]), True),
    (buildTree([1, 2, 3]), False),
    (buildTree([1, 2, 2, 3, 4, 4, 3]), True),
    (buildTree([1, 2, 2, None, 3, None, 3]), False),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.isSymmetric(root)

    assert output == expected_output
    output = solution.isSymmetric2(root)

    assert output == expected_output
