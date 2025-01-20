"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.



Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.


Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 9
The depth of the tree will not exceed 10.
"""
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


class Solution:

    # Intuition
    # Multiply 10 to create the next digit.
    # Time complexity: O(n)
    # n is number of nodes in the input tree
    #
    # Space complexity: O(h) or O(n)
    # h is height of the input tree
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, num):
            if not node:
                return 0

            num = num * 10 + node.val

            # if a leaf
            if not node.left and not node.right:
                return num

            return dfs(node.left, num) + dfs(node.right, num)

        return dfs(root, 0)


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2, 3]), 25),
    (build_tree([4, 9, 0, 5, 1]), 1026),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.sumNumbers(root)

    assert output == expected_output
