"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.


Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque
from functools import reduce
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, buildTree


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        map_nodes_by_levels = {0: [root.val]}

        def get_nodes_by_level(node, level):
            if not map_nodes_by_levels.get(level, False) and (node.left or node.right):
                map_nodes_by_levels[level] = []

            if node.left:
                map_nodes_by_levels[level].append(node.left.val)
                get_nodes_by_level(node.left, level + 1)
            if node.right:
                map_nodes_by_levels[level].append(node.right.val)
                get_nodes_by_level(node.right, level + 1)

        get_nodes_by_level(root, 1)

        def calculate_average(lst):
            # print(f'hello {lst}')
            total_sum = reduce((lambda x=0, y=0: x + y), lst, 0)  # Sum the elements using reduce
            # total_sum = 0  # Sum the elements using reduce
            count = len(lst)
            return total_sum / count if count > 0 else 0  # Avoid division by zero

        # Calculate averages for each list in the map
        averages = [calculate_average(value) for key, value in map_nodes_by_levels.items()]

        return averages

    # BFS
    def averageOfLevels2(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            qlen = len(q)
            row = 0
            for i in range(qlen):
                node = q.popleft()
                row += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(row / qlen)
        return ans


@pytest.mark.parametrize('root, expected_output', [
    (buildTree([3, 9, 20, None, None, 15, 7]), [3.00000, 14.50000, 11.00000]),
    (buildTree([3, 9, 20, 15, 7]), [3.00000, 14.50000, 11.00000]),
    (buildTree([3, 9, 20, 15, 7, 15, 3]), [3.00000, 14.50000, 10.00000]),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.averageOfLevels(root)

    assert output == expected_output
    output = solution.averageOfLevels2(root)

    assert output == expected_output
