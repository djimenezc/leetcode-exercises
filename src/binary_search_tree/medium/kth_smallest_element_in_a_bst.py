"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all
the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth
smallest frequently, how would you optimize?

Intuition :
1. A Binary Search Tree (BST) is structured such that:
- The left subtree contains values smaller than the root.
- The right subtree contains values larger than the root.
2.An inorder traversal of a BST yields values in sorted order. This makes it straightforward to extract the ( k )-th
smallest value by counting nodes as we traverse the tree.

Approaches :
1. Simple Inorder Traversal (Recursive or Iterative)
Perform a full inorder traversal and stop as soon as the ( k )-th smallest element is reached.

2. Follow-Up Optimization (Dynamic BST Modifications)
If the BST is frequently modified (insertions or deletions), augment the tree nodes to include the size of
the subtree rooted at each node. This allows us to perform an ( O(\log n) )-time search for the ( k )-th
smallest element without a full traversal.
"""
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


class Solution:

    # Time Complexity:
    # Inorder Traversal:
    # O(n) for a full traversal.
    # O(k) if we stop as soon as the k -th element is found.
    # Augmented Tree (Follow-Up):
    # O(log n) for each query if subtree sizes are maintained.
    # Space Complexity:
    # O(h) , where h is the height of the tree (due to the recursive call stack or iterative stack).
    # slower than implementation 2
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            # Traverse left subtree
            yield from inorder(node.left)
            # Visit current node
            yield node.val
            # Traverse right subtree
            yield from inorder(node.right)

        # Iterate through inorder traversal and find the k-th smallest
        gen = inorder(root)
        for _ in range(k):
            result = next(gen)

        return result

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def Trav(x):
            if x == None:
                arr.append(0)
            if x.left:
                Trav(x.left)
            if x:
                arr.append(x.val)
            if x.right:
                Trav(x.right)

        Trav(root)
        return arr[k - 1]


@pytest.mark.parametrize('root, k, expected_output', [
    (build_tree([3, 1, 4, None, 2]), 1, 1),
    (build_tree([5, 3, 6, 2, 4, None, None, 1]), 3, 3),
])
def test_merge(root, k, expected_output):
    solution = Solution()
    output = solution.kthSmallest(root, k)

    assert output == expected_output
    output = solution.kthSmallest2(root, k)

    assert output == expected_output
