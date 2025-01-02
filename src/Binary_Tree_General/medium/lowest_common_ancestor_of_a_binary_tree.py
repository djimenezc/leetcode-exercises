"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, buildTree


class Solution:

    # Approach:
    # Core Idea
    # Instead of traversing the tree multiple times or maintaining extra data structures like parent pointers or
    # ancestor sets, we directly calculate the LCA during a single DFS traversal.
    #
    # Key Insight:
    #
    # If a node has both ( p ) and ( q ) in its left and right subtrees, then it is the LCA.
    # If a node itself is ( p ) or ( q ), it could be the LCA (if the other node is below it in one of its subtrees).
    # DFS Behavior:
    #
    # Traverse the tree using DFS.
    # For each node:
    # Check its left and right subtrees recursively.
    # If both subtrees return a non-null value, the current node is the LCA.
    # Otherwise, return the non-null child (it might be the potential LCA).
    # Early Stopping:
    #
    # If a node is ( p ) or ( q ), return it immediately without further recursion.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            # Base case: null node
            if not node:
                return None

            # If the current node is either p or q, return it
            if node == p or node == q:
                return node

            # Recur for left and right children
            left = dfs(node.left)
            right = dfs(node.right)

            # If both left and right return a non-null value, current node is LCA
            if left and right:
                return node

            # Otherwise, return the non-null child (or null if both are null)
            return left if left else right

        # Start the DFS from the root
        return dfs(root)

    def path(self, root: Optional[TreeNode], ans: List[int], x: int) -> bool:
        if root is None:
            return False

        ans.append(root.val)

        if root.val == x:
            return True

        if self.path(root.left, ans, x) or self.path(root.right, ans, x):
            return True

        ans.pop()
        return False

    # Intuition
    # The problem asks for the lowest common ancestor (LCA) of two nodes in a binary tree. Initially,
    # my thought was to find the paths from the root to the two given nodes, and then compare the paths to identify
    # the last common node. This node would be the LCA. By leveraging recursion, we can trace the path from the root
    # to each of the target nodes and collect the values in a list.
    #
    # Approach
    # Path Finding:
    #
    # Recursively traverse the binary tree to find the paths from the root to the two nodes (p and q).
    # Maintain a list of node values encountered on the path.
    # If the target node is found, return true and retain the current path in the list.
    # If the target is not found in both the left and right subtrees, backtrack by removing the last added node.
    # Compare Paths:
    #
    # After finding the paths to p and q, compare the paths step by step.
    # The last node that is common in both paths is the LCA.
    # Return this node as the result.
    # Complexity
    # Time complexity:
    #
    # Finding the path to a node takes O(n) time, where n is the number of nodes in the tree. Since we do this for
    # both nodes p and q, the total time complexity is O(n) + O(n) = O(n).
    # Space complexity:
    #
    # We store the path for both nodes, which in the worst case could be the depth of the tree (i.e., O(h)), where h
    # is the height of the tree. In the worst case, the height is O(n) for a skewed tree,
    # making the space complexity O(n).
    # In the best case, if the tree is balanced, the space complexity would be O(log n) due to the height
    # being logarithmic.
    def lowestCommonAncestor2(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode:
        pathp, pathq = [], []

        self.path(root, pathp, p.val)
        self.path(root, pathq, q.val)

        i = 0
        while i < len(pathp) and i < len(pathq):
            if pathp[i] != pathq[i]:
                break
            i += 1

        return TreeNode(pathp[i - 1])


@pytest.mark.parametrize('root, p, q, expected_output', [
    (buildTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), buildTree([5]), buildTree([1]), 3),
    (buildTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]), buildTree([5]), buildTree([4]), 5),
    (buildTree([1, 2]), buildTree([1]), buildTree([2]), 1),
])
def test_merge(root, p, q, expected_output):
    solution = Solution()
    output = solution.lowestCommonAncestor2(root, p, q)

    assert output.val == expected_output
