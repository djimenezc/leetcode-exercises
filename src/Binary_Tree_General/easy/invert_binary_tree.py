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
"""
from typing import Optional

import pytest
from ..Utils import TreeNode, buildTree, isSameTree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        temp_node = root.left
        root.left = root.right
        root.right = temp_node
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root


@pytest.mark.parametrize('root, expected_output', [
    (buildTree([1, None, 2]), buildTree([1, 2, None])),
    (buildTree([2, 1, 3]), buildTree([2, 3, 1])),
    (buildTree([4, 2, 7, 1, 3, 6, 9]), buildTree([4, 7, 2, 9, 6, 3, 1])),
    ([], []),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.invertTree(root)

    assert isSameTree(output, expected_output)
