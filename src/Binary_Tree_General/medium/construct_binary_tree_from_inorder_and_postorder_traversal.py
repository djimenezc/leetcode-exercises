"""
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder
is the postorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]


Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.




"""
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, buildTree, isSameTree


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return root

    def buildHelper(self, inorder, ins, inl, postorder, posts, postl, index):
        if posts > postl or ins > inl:
            return None

        # The last element of postorder is the root of the current subtree
        root = TreeNode(postorder[postl])

        # Find the index of the root in inorder traversal
        ind = index[root.val]

        # Number of nodes in the left subtree
        x = ind - ins

        # Recursively build the left and right subtrees
        root.left = self.buildHelper(inorder, ins, ind - 1, postorder, posts, posts + x - 1, index)
        root.right = self.buildHelper(inorder, ind + 1, inl, postorder, posts + x, postl - 1, index)

        return root

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Map the values to their indices in inorder traversal
        index = {val: i for i, val in enumerate(inorder)}

        # Build the tree using the helper function
        return self.buildHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, index)


@pytest.mark.parametrize('preorder, inorder, expected_output', [
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], buildTree([3, 9, 20, None, None, 15, 7])),
    ([-1], [-1], buildTree([-1]),),
])
def test_merge(preorder, inorder, expected_output):
    solution = Solution()
    output = solution.buildTree(preorder, inorder)

    assert isSameTree(output, expected_output)
    output = solution.buildTree2(preorder, inorder)

    assert isSameTree(output, expected_output)
