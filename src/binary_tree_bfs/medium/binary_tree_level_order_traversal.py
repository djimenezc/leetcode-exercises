"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, buildTree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            same_level = []

            for _ in range(len(q)):
                node = q.popleft()
                same_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(same_level)

        return res


@pytest.mark.parametrize('root, expected_output', [
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    (buildTree([3, 9, 20, None, None, 15, 7]), [[3], [9, 20], [15, 7]]),
    (buildTree([1]), [[1]]),
    (buildTree([]), []),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.levelOrder(root)

    assert output == expected_output
