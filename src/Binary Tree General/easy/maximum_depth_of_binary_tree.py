"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from typing import Optional

import pytest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(Solution.maxDepth(self, root.left), Solution.maxDepth(self, root.right))
        else:
            return 0

    # Key Idea :
    # The depth of a binary tree is the maximum depth among its left and right subtrees, plus 1 for the root node.
    # Using recursion, we compute the depth of the left and right subtrees and take the maximum.
    # Iterative DFS Approach :
    # Use a stack to store pairs of nodes and their depths.
    # Traverse the tree, updating the maximum depth whenever reaching a leaf node.
    # Complexity Analysis :
    # Time Complexity: O(n), where n is the number of nodes. Each node is visited exactly once.
    # Space Complexity:
    # Recursive: O(h), where h is the height of the tree (call stack).
    # Iterative: O(h), where h is the height of the tree (stack storage).
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth

    # To calculate the maximum depth we can use the Depth-First Search. We call a helper function recursively
    # and return the maximum depth between left and right branches.
    #
    # Time: O(N) - for DFS
    # Space: O(N) - for the recursive stack
    #
    # Runtime: 40 ms, faster than 89.54% of Python3 online submissions for Maximum Depth of Binary Tree.
    # Memory Usage: 16.3 MB, less than 18.15% of Python3 online submissions for Maximum Depth of Binary Tree.
    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

        return dfs(root, 0)


@pytest.mark.parametrize('root,expected_output', [
    # (TreeNode(3, TreeNode(9, None, None),
    #           TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None))), 3),
    (TreeNode(1, None, TreeNode(2, None, None)), 2),
    (TreeNode(1, None, None), 1),
    (None, 0),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.maxDepth(root)

    assert output == expected_output
    output = solution.maxDepth2(root)

    assert output == expected_output
    output = solution.maxDepth3(root)

    assert output == expected_output
