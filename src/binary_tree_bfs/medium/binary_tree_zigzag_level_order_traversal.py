"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
(i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree
from queue import Queue

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        res = []
        zigzag = False

        while queue:
            level = []
            n = len(queue)

            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if zigzag:
                level.reverse()

            res.append(level)
            zigzag = not zigzag

        return res

    # not too good
    # https://docs.python.org/3/library/queue.html
    def zigzagLevelOrder2(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = Queue()
        queue.put(root)
        output = []
        curr = []
        level = 0
        while not queue.empty():
            size = queue.qsize()
            curr = []
            for i in range(size):
                temp = queue.get()
                if level % 2 == 0:
                    curr.append(temp.val)
                else:
                    curr.insert(0, temp.val)
                if temp.left:
                    queue.put(temp.left)
                if temp.right:
                    queue.put(temp.right)
            level = not level
            output.append(curr)
        return output


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([3, 9, 20, None, None, 15, 7]), [[3], [20, 9], [15, 7]]),
    (build_tree([1]), [[1]]),
    (build_tree([]), []),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.zigzagLevelOrder(root)

    assert output == expected_output
