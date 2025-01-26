"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
 adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import Optional

import pytest

from ..Utils import TreeNode, build_tree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def path_sum_target(node: Optional[TreeNode], acc: int, target: int):
            if not node:
                return False
            elif not node.left and not node.right:
                # print(f'target {node.val + acc}')
                return node.val + acc == target
            else:
                return (path_sum_target(node.left, acc + node.val, target)
                        or path_sum_target(node.right, acc + node.val, target))

        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        return path_sum_target(root.left, root.val, targetSum) or path_sum_target(root.right, root.val, targetSum)

    def hasPathSum2(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # is a leaf
        if not root.left and not root.right:
            return targetSum == root.val

        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)

        return left_sum or right_sum


solution = Solution()


@pytest.mark.parametrize('root, targetSum, expected_output', [
    (build_tree([1]), 1, True),
    (build_tree([1, 2]), 1, False),
    (build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22, True),
    (build_tree([5, None, 5]), 10, True),
    (build_tree([1, 2, 3]), 5, False),
    (build_tree([]), 0, False),
])
class TestCase:
    def test_0(self, root, targetSum, expected_output):
        output = solution.hasPathSum(root, targetSum)

        assert output == expected_output

    def test_2(self, root, targetSum, expected_output):
        output = solution.hasPathSum2(root, targetSum)

        assert output == expected_output
