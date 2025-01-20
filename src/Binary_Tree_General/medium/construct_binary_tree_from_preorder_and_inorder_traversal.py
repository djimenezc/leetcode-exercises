"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.



Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]


Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.

Intuition
Think about how we traverse a tree in preorder and inorder.

Approach
I'll show you 2 ways to solve question.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]

Solution 1

There is a hint in preorder array, because the first number(= 3) is definitely root node.

⭐️ Points

Where is 3 in inorder array?

inorder = [9,3,15,20,7]

We can find 3 at index 1 in inorder array, that means left side of 3 in inorder array is all left nodes of 3 in the tree, because inorder traversal is like left, root and right. We ususally find left nodes before we find root node.

I believe now you can guess. All right numbers of 3 in inorder array should be all right nodes.

left nodes: 9
root: 3
right nodes: 15,20,7

Solution 1 is O(n 2) time. Let me improve it.

"""
import collections
from collections import deque
from typing import Optional, List

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree, is_same_tree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)

        def build(preorder, inorder):
            if inorder:
                idx = inorder.index(preorder.popleft())
                root = TreeNode(inorder[idx])

                root.left = build(preorder, inorder[:idx])
                root.right = build(preorder, inorder[idx + 1:])

                return root

        return build(preorder, inorder)

    # Time complexity: O(n)
    # Space complexity: O(n)
    # Problem of solution 1 is that we iterate through all numbers to find the target index with this code.
    #
    # idx = inorder.index(preorder.popleft())
    # That's why we create mapping of key and value in inorder array with HashMap before we start recursion,
    # so that we can access the target index with O(1) time instead of O(n) time.
    #
    # mapping = {9:0, 3:1, 15:2, 20:3, 7:4}
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        mapping = {}

        for i in range(len(inorder)):
            mapping[inorder[i]] = i

        preorder = deque(preorder)

        def build(start, end):
            if start > end: return None

            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]

            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)

            return root

        return build(0, len(preorder) - 1)


@pytest.mark.parametrize('preorder, inorder, expected_output', [
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], build_tree([3, 9, 20, None, None, 15, 7])),
    ([-1], [-1], build_tree([-1]),),
])
def test_merge(preorder, inorder, expected_output):
    solution = Solution()
    output = solution.buildTree(preorder, inorder)

    assert is_same_tree(output, expected_output)
    output = solution.buildTree2(preorder, inorder)

    assert is_same_tree(output, expected_output)
