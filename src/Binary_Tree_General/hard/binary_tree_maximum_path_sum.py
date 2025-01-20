"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an
 edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need
 to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.



Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.


Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


class Solution:

    # Intuition:
    # The problem requires finding the maximum path sum in a binary tree. A path in a binary tree is defined as
    # any sequence of nodes from some starting node to any node in the tree along the parent-child connections.
    # The path sum of a path is the sum of the node values along that path.
    # Complexity
    # Time complexity: The DFS algorithm visits each node in the binary tree once, so the time complexity is O(n),
    # where n is the number of nodes in the tree.
    # Space complexity: The space complexity is O(h), where h is the height of the binary tree.
    # This space is used for the recursive call stack during the DFS traversal.
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]  # Initialize a list to store the result

        # To solve this problem, we employ a depth-first search (DFS) approach to traverse the binary tree while
        # keeping track of the maximum path sum encountered so far. We define a recursive function DFS that
        # calculates the maximum path sum starting from the current node.
        def DFS(root):
            # Base case: return 0 if the node is None
            if not root:
                return 0

            # Recursive calculation for left and right subtrees
            # Ensure that negative values are not considered (max(0, ...))
            lmax = max(0, DFS(root.left))
            rmax = max(0, DFS(root.right))

            # Update the overall maximum path sum
            ans[0] = max(ans[0], root.val + lmax + rmax)

            # Return the maximum path sum that starts from the current node
            return root.val + max(lmax, rmax)

        # Call the DFS function on the root node
        DFS(root)

        # Return the final maximum path sum
        return ans[0]


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2, 3]), 6),
    (build_tree([-10, 9, 20, None, None, 15, 7]), 42)
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.maxPathSum(root)

    assert output == expected_output
