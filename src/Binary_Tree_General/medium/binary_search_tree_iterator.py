"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.



Example 1:


Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    # return 3
bSTIterator.next();    # return 7
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 9
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 15
bSTIterator.hasNext(); # return True
bSTIterator.next();    # return 20
bSTIterator.hasNext(); # return False


Constraints:

The number of nodes in the tree is in the range [1, 105].
0 <= Node.val <= 106
At most 105 calls will be made to hasNext, and next.


Follow up:

Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?
"""
from typing import Optional

import pytest

from src.Binary_Tree_General.Utils import TreeNode, build_tree


# Use stack + on-the-go push and pop
# Here instead of creating the whole array in constructor, we use stack to maintain the part we have not traversed yet.
# As next is called, we will keep poping from stack.
#
# Complexity
# Time complexity: O(n)
# Space complexity: O(n) -> using stack
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        r = node.right
        while r:
            self.stack.append(r)
            r = r.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


@pytest.mark.parametrize('root, expected_output', [
    (build_tree([1, 2, 3]), 25),
])
def test_merge(root, expected_output):
    bst_iterator = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
    assert bst_iterator.next() == 3  # return 3
    assert bst_iterator.next() == 7  # return 7
    assert bst_iterator.hasNext() is True  # return True
    assert bst_iterator.next() == 9  # return 9
    assert bst_iterator.hasNext() is True  # return True
    assert bst_iterator.next() == 15  # return 15
    assert bst_iterator.hasNext() is True  # return True
    assert bst_iterator.next() == 20  # return 20
    assert bst_iterator.hasNext() is False  # return False
