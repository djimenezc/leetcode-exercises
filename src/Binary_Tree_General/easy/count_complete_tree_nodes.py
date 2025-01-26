"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive
at the last level h.

Design an algorithm that runs in less than O(n) time complexity.



Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1


Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
from typing import Optional

import pytest

from ..Utils import TreeNode, build_tree


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:  # leaf
            return 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def countNodes2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)

    def countNodes3(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def depth(root):
            height = 0
            while root:
                height += 1
                root = root.left

            return height

        ld = depth(root.left)
        rd = depth(root.right)

        if ld == rd:
            return 1 + ((2 ** ld) - 1) + self.countNodes(root.right)
        else:
            return 1 + ((2 ** rd) - 1) + self.countNodes(root.left)

    def countNodes4(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height, right_height = 0, 0
        curr = root

        while curr:
            left_height += 1
            curr = curr.left
        curr = root

        while curr:
            right_height += 1
            curr = curr.right

        if left_height == right_height:
            return pow(2, left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


solution = Solution()


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2]), 2),
    (build_tree([1, 2, 3]), 3),
    (build_tree([1, 2, 3, 4, 5, 6]), 6),
    (build_tree([]), 0),
    (build_tree([1]), 1),
])
class TestCase:
    def test_0(self, root, expected_output):
        output = solution.countNodes(root)
        assert output == expected_output

    def test_1(self, root, expected_output):
        output = solution.countNodes2(root)
        assert output == expected_output

    def test_2(self, root, expected_output):
        output = solution.countNodes3(root)
        assert output == expected_output

    def test_3(self, root, expected_output):
        output = solution.countNodes4(root)

        assert output == expected_output
