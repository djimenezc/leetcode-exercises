"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree, is_same_tree


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if not root:
            return

        # Process right subtree first
        self.flatten(root.right)

        # Process left subtree
        self.flatten(root.left)

        # Set the current node's right to prev and left to null
        root.right = self.prev
        root.left = None

        # Update prev to current node
        self.prev = root


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2, 5, 3, 4, None, 6]), build_tree([1, None, 2, None, 3, None, 4, None, 5, None, 6])),
    (build_tree([]), build_tree([])),
    (build_tree([0]), build_tree([0])),
])
def test_merge(root, expected_output):
    solution = Solution()
    solution.flatten(root)
    assert is_same_tree(root, expected_output)
