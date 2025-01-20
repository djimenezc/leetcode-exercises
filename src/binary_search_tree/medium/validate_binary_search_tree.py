"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


class Solution:

    def __init__(self):
        self.prev = float('-inf')
        self.isValid = True

    def inorder(self, root: Optional[TreeNode]) -> None:
        if not self.isValid or not root:
            return

        self.inorder(root.left)

        if self.prev >= root.val:
            self.isValid = False
            return
        self.prev = root.val

        self.inorder(root.right)

    # Approach:
    # Perform an inorder traversal of the tree.
    # During the inorder traversal of a BST, node values should be visited in ascending order.
    # Keep track of the previous node's value (prev) during traversal and compare it with the current node's value.
    # If any node's value is less than or equal to the previous node's value, the tree is not a valid BST.
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')  # Reset prev for each call
        self.isValid = True  # Reset isValid for each call
        self.inorder(root)
        return self.isValid

    # Intuition
    # Check range of each node.
    # When we go left, update maxinum value only. A minimum number will be the same number from parent.
    #
    # On the other hand, when we go right, update minimum number only. A maximum number will be
    # the same number from parent.
    # Complexity
    # Time complexity: O(n)
    # Space complexity: O(n)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True

            if not (minimum < node.val < maximum):
                return False

            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)

        return valid(root, float("-inf"), float("inf"))


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([2, 1, 3]), True),
    (build_tree([5, 1, 4, None, None, 3, 6]), False),
])
def test_merge(root, expected_output):
    solution = Solution()
    output = solution.isValidBST(root)

    assert output == expected_output
    output = solution.isValidBST2(root)

    assert output == expected_output
