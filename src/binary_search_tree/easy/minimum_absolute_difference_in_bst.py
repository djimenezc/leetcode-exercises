"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two
different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105


Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
from collections import deque
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        values = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                values.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        values.sort()
        differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]

        return min(differences)

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        values = []

        while q:
            node = q.popleft()
            values.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        values.sort()

        min_difference: float = float("inf")
        for i in range(1, len(values)):
            min_difference = min(min_difference, values[i] - values[i - 1])
            if min_difference == 1:
                break

        return int(min_difference)


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([4, 2, 6, 1, 3]), 1),
    (build_tree([1, 0, 48, None, None, 12, 49]), 1),
    (build_tree([543, 384, 652, None, 445, None, 699]), 47),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.getMinimumDifference(root)

    assert output == expected_output
    output = solution.getMinimumDifference2(root)

    assert output == expected_output
